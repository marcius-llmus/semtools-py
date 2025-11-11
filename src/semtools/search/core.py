import asyncio
import os
from typing import List, Optional, Union

from model2vec import StaticModel

from ..workspace import Store, Workspace
from ..workspace.store import DocMeta, LineEmbedding, RankedLine
from .engine import SearchEngine
from .enums import EmbeddingModel
from .loader import DocumentLoader
from .models import SearchResult


async def _process_file_for_workspace(
    file_path: str, existing_docs: dict, searcher: "Searcher", ignore_case: bool
):
    """Async helper to check and process a single file for workspace update."""
    try:
        stat = await asyncio.to_thread(os.stat, file_path)
        current_meta = DocMeta(
            path=file_path, size_bytes=stat.st_size, mtime=int(stat.st_mtime)
        )
    except FileNotFoundError:
        return None, None

    existing_meta = existing_docs.get(file_path)
    if (
        not existing_meta
        or existing_meta.mtime != current_meta.mtime
        or existing_meta.size_bytes != current_meta.size_bytes
    ):

        def read_and_embed():
            """Read file and compute embeddings in a blocking thread."""
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = [line.rstrip("\n") for line in f.readlines()]
            except (IOError, UnicodeDecodeError):
                return [], None

            if not lines:
                return [], None

            lines_for_embedding = (
                [line.lower() for line in lines] if ignore_case else lines
            )
            embeddings = searcher.model.encode(lines_for_embedding)

            file_lines_to_upsert = [
                LineEmbedding(path=file_path, line_number=i, embedding=emb.tolist())
                for i, emb in enumerate(embeddings)
            ]
            return file_lines_to_upsert, current_meta

        lines_to_upsert, doc_to_upsert = await asyncio.to_thread(read_and_embed)
        return lines_to_upsert, doc_to_upsert

    return None, None


class Searcher:
    """
    Encapsulates the logic for semantic search.
    """

    def __init__(
        self,
        model: Optional[StaticModel] = None,
        model_name: EmbeddingModel = EmbeddingModel.POTION_MULTI_LINGUAL_128M,
    ):
        self.model = model or StaticModel.from_pretrained(model_name)

    def search(
        self,
        query: str,
        files: List[str],
        n_lines: int = 3,
        top_k: int = 3,
        max_distance: Optional[float] = None,
        ignore_case: bool = False,
    ) -> Union[List[SearchResult], List[RankedLine]]:
        """
        Orchestrates a search across files or stdin, dispatching to workspace or
        in-memory search as appropriate.
        """
        if os.getenv("SEMTOOLS_WORKSPACE") and files:
            return asyncio.run(
                self._search_with_workspace(
                    query, files, n_lines, top_k, max_distance, ignore_case
                )
            )
        return self._search_in_memory(
            query, files, n_lines, top_k, max_distance, ignore_case
        )

    def _search_in_memory(
        self,
        query: str,
        files: List[str],
        n_lines: int,
        top_k: int,
        max_distance: Optional[float],
        ignore_case: bool,
    ) -> List[SearchResult]:
        """Performs a standard, stateless search in memory."""
        processed_query = query.lower() if ignore_case else query

        query_embedding = self.model.encode([processed_query])[0]

        doc_loader = DocumentLoader(self.model, ignore_case=ignore_case)
        documents = doc_loader.load(files)

        if not documents:
            return []

        return SearchEngine.rank_results(
            documents, query_embedding, n_lines, top_k, max_distance
        )

    async def _search_with_workspace(
        self,
        query: str,
        files: List[str],
        n_lines: int,
        top_k: int,
        max_distance: Optional[float],
        ignore_case: bool,
    ) -> List[RankedLine]:
        """Handles the search logic when a workspace is active."""
        ws = Workspace.open()
        store = Store(ws.config.root_dir)

        # 1. Analyze document states concurrently
        existing_docs = await asyncio.to_thread(store.get_existing_docs, files)

        tasks = [
            _process_file_for_workspace(fp, existing_docs, self, ignore_case)
            for fp in files
        ]
        results = await asyncio.gather(*tasks)

        all_lines_to_upsert = [line for res in results if res[0] for line in res[0]]
        all_docs_to_upsert = [res[1] for res in results if res[1]]

        # 2. Update workspace if necessary (run in thread to not block)
        if all_lines_to_upsert:
            await asyncio.to_thread(store.upsert_line_embeddings, all_lines_to_upsert)
        if all_docs_to_upsert:
            await asyncio.to_thread(store.upsert_document_metadata, all_docs_to_upsert)

        # 3. Search the workspace
        processed_query = query.lower() if ignore_case else query
        query_embedding = await asyncio.to_thread(self.model.encode, [processed_query])
        return await asyncio.to_thread(
            store.search_line_embeddings, query_embedding[0].tolist(), files, top_k, max_distance
        )