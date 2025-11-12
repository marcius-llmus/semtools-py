import asyncio
import os
import aiofiles
import aiofiles.os
import numpy as np
from scipy.spatial.distance import cosine
from typing import List, Optional

from model2vec import StaticModel

from ..workspace import Store, Workspace
from ..workspace.store import DocMeta, LineEmbedding, RankedLine
from .enums import EmbeddingModel
from .loader import DocumentLoader
from .models import Document


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
        top_k: int = 3,
        max_distance: Optional[float] = None,
        ignore_case: bool = False,
    ) -> List[RankedLine]:
        """
        Orchestrates a search across files or stdin, dispatching to workspace or
        in-memory search as appropriate.
        """
        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        if os.getenv("SEMTOOLS_WORKSPACE") and files:
            return asyncio.run(
                self._search_with_workspace(
                    query, files, top_k, max_distance, ignore_case
                )
            )
        return self._search_in_memory(
            query, files, top_k, max_distance, ignore_case
        )

    @staticmethod
    def _rank_results(
        documents: List[Document],
        query_embedding: np.ndarray,
        top_k: int,
        max_distance: Optional[float],
    ) -> List[RankedLine]:
        """Performs the core search logic on a list of in-memory documents."""
        raw_results = []
        for doc in documents:
            for i, line_embedding in enumerate(doc.embeddings):
                distance = cosine(query_embedding, line_embedding)
                if max_distance is None or distance <= max_distance:
                    raw_results.append(
                        RankedLine(path=doc.path, line_number=i, distance=distance)
                    )

        raw_results.sort(key=lambda x: x.distance)

        final_results = raw_results if max_distance is not None else raw_results[:top_k]
        return final_results

    async def _encode_in_thread(
        self, lines: List[str], ignore_case: bool
    ) -> np.ndarray:
        """Asynchronously encodes lines by running the sync encoder in a thread."""
        lines_for_embedding = (
            [line.lower() for line in lines] if ignore_case else lines
        )
        return await asyncio.to_thread(self.model.encode, lines_for_embedding)

    def _search_in_memory(
        self,
        query: str,
        files: List[str],
        top_k: int,
        max_distance: Optional[float],
        ignore_case: bool,
    ) -> List[RankedLine]:
        """Performs a standard, stateless search in memory."""
        processed_query = query.lower() if ignore_case else query

        query_embedding = self.model.encode([processed_query])[0]

        doc_loader = DocumentLoader(self.model, ignore_case=ignore_case)
        documents = doc_loader.load(files)

        if not documents:
            return []

        return self._rank_results(
            documents, query_embedding, top_k, max_distance
        )

    async def _embed_lines_sync(self, lines: List[str], file_path: str, ignore_case: bool) -> List[LineEmbedding]:
        """Computes embeddings for a list of lines. Blocking."""
        embeddings = await self._encode_in_thread(lines, ignore_case)
        return [
            LineEmbedding(path=file_path, line_number=i, embedding=emb.tolist())  # noqa
            for i, emb in enumerate(embeddings)
        ]

    async def _process_file_for_workspace(
        self, file_path: str, existing_docs: dict, ignore_case: bool
    ):
        """Async helper to check and process a single file for workspace update."""
        try:
            stat = await aiofiles.os.stat(file_path)
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
            try:
                async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
                    lines = [line.rstrip("\n") for line in await f.readlines()]
            except (IOError, UnicodeDecodeError):
                return [], None

             
            if not lines: 
                return [], current_meta 
            lines_to_upsert = await self._embed_lines_sync(lines, file_path, ignore_case)

            return lines_to_upsert, current_meta

        return None, None

    async def _search_with_workspace(
        self,
        query: str,
        files: List[str],
        top_k: int,
        max_distance: Optional[float],
        ignore_case: bool,
    ) -> List[RankedLine]:
        """Handles the search logic when a workspace is active."""
        ws = Workspace.open()
        store = await Store.create(ws.config)

        # 1. Analyze document states concurrently
        existing_docs = await store.get_existing_docs(files)

        tasks = [
            self._process_file_for_workspace(fp, existing_docs, ignore_case)
            for fp in files
        ]
        results = await asyncio.gather(*tasks)

        all_lines_to_upsert = [line for res in results if res[0] for line in res[0]]
        all_docs_to_upsert = [res[1] for res in results if res[1]]

        # 2. Update workspace if necessary (run in thread to not block)
        if all_lines_to_upsert:
            await store.upsert_line_embeddings(all_lines_to_upsert)
        if all_docs_to_upsert:
            await store.upsert_document_metadata(all_docs_to_upsert)

        # 3. Search the workspace
        query_embedding = await self._encode_in_thread(
            [query], ignore_case
        )
        return await store.search_line_embeddings(
            query_embedding[0].tolist(), files, top_k, max_distance
        )