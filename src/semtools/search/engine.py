from typing import List, Optional

import numpy as np
from scipy.spatial.distance import cosine

from .models import Document, SearchResult


class SearchEngine:
    """A stateless engine for ranking and formatting search results."""

    @staticmethod
    def _get_context_window(
        line_index: int, total_lines: int, n_lines: int
    ) -> tuple[int, int]:
        """Calculates the start and end indices for a context slice."""
        start = max(0, line_index - n_lines)
        end = min(total_lines, line_index + n_lines + 1)
        return start, end

    @staticmethod
    def format_results(
        raw_results: list[tuple[float, Document, int]], n_lines: int
    ) -> List[SearchResult]:
        """Formats raw search hits into SearchResult objects."""
        results = []
        for dist, doc, i in raw_results:
            start_line, end_line = SearchEngine._get_context_window(
                i, len(doc.lines), n_lines
            )
            context = doc.lines[start_line:end_line]
            results.append(
                SearchResult(
                    file_path=doc.file_path,
                    context_lines=context,
                    context_start_line=start_line,
                    match_line_index=i,
                    distance=dist,
                )
            )
        return results

    @staticmethod
    def rank_results(
        documents: List[Document],
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
                if max_distance is None or distance <= max_distance:
                    raw_results.append((distance, doc, i))

        raw_results.sort(key=lambda x: x[0])

        final_results = (
            raw_results if max_distance is not None else raw_results[:top_k]
        )

        return SearchEngine.format_results(final_results, n_lines)
