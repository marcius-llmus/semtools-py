import sys
from dataclasses import dataclass
from typing import List, Optional

import numpy as np
from model2vec import StaticModel
from scipy.spatial.distance import cosine

from .models import SearchResult


@dataclass
class _Document:
    """Internal representation of a file's content and embeddings."""

    file_path: str
    lines: List[str]
    embeddings: np.ndarray


class Searcher:
    """
    Encapsulates the logic for semantic search, mirroring the Rust implementation.
    """

    def __init__(self, model_name: str = "minishlab/potion-multilingual-128M"):
        self.model = StaticModel.from_pretrained(model_name)

    def search(
        self,
        query: str,
        files: List[str],
        n_lines: int = 3,
        top_k: int = 3,
        max_distance: Optional[float] = None,
        ignore_case: bool = False,
    ) -> List[SearchResult]:
        """
        Orchestrates a search across files or stdin, mirroring the Rust binary's logic.
        """
        processed_query = query.lower() if ignore_case else query
        query_embedding = self.model.encode([processed_query])[0]

        documents: List[_Document] = []
        if not files and not sys.stdin.isatty():
            stdin_lines = [line.rstrip("\n") for line in sys.stdin.readlines()]
            if stdin_lines:
                doc = self._create_document_from_lines(
                    "<stdin>", stdin_lines, ignore_case
                )
                if doc:
                    documents.append(doc)
        else:
            for file_path in files:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        lines = [line.rstrip("\n") for line in f.readlines()]
                    doc = self._create_document_from_lines(
                        file_path, lines, ignore_case
                    )
                    if doc:
                        documents.append(doc)
                except (IOError, UnicodeDecodeError):
                    continue

        return self._search_documents(
            documents, query_embedding, n_lines, top_k, max_distance
        )

    def _create_document_from_lines(
        self, file_path: str, lines: List[str], ignore_case: bool
    ) -> Optional[_Document]:
        """Creates a _Document from lines of text."""
        if not lines:
            return None

        lines_for_embedding = [line.lower() for line in lines] if ignore_case else lines
        embeddings = self.model.encode(lines_for_embedding)

        return _Document(
            file_path=file_path, lines=lines, embeddings=np.array(embeddings)
        )

    def _search_documents(
        self,
        documents: List[_Document],
        query_embedding: np.ndarray,
        n_lines: int,
        top_k: int,
        max_distance: Optional[float],
    ) -> List[SearchResult]:
        """Performs the core search logic on a list of in-memory documents."""
        raw_results = []
        for doc in documents:
            for i, line_embedding in enumerate(doc.embeddings):
                distance = cosine(query_embedding, line_embedding)
                if max_distance is None or distance < max_distance:
                    raw_results.append((distance, doc, i))

        raw_results.sort(key=lambda x: x[0])

        final_results = raw_results if max_distance is not None else raw_results[:top_k]

        return [
            SearchResult(
                file_path=doc.file_path,
                context_lines=doc.lines[max(0, i - n_lines) : min(len(doc.lines), i + n_lines + 1)],
                context_start_line=max(0, i - n_lines),
                match_line_index=i,
                distance=dist,
            )
            for dist, doc, i in final_results
        ]