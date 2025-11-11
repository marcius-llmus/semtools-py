import numpy as np

from src.semtools.search.engine import SearchEngine
from src.semtools.search.models import Document


class TestSearchEngine:
    def test_rank_results_with_top_k(self, mock_documents):
        
        query_embedding = np.array([0.1, 0.2])  # Closest to doc1, line 1

        
        results = SearchEngine.rank_results(
            documents=mock_documents, query_embedding=query_embedding, n_lines=1, top_k=1, max_distance=None
        )

        
        assert len(results) == 1
        assert results[0].path == "/fake/doc1.txt"
        assert results[0].line_number == 0

    def test_rank_results_with_max_distance(self, mock_documents):
        
        query_embedding = np.array([0.4, 0.5])  # Equidistant to doc1 line 2 and doc2 line 1

        
        results = SearchEngine.rank_results(
            documents=mock_documents, query_embedding=query_embedding, n_lines=1, top_k=10, max_distance=0.0005
        )

        
        assert len(results) == 2
        paths = {r.path for r in results}
        assert "/fake/doc1.txt" in paths
        assert "/fake/doc2.txt" in paths

    def test_rank_results_empty(self):
        
        results = SearchEngine.rank_results(
            documents=[], query_embedding=np.array([0, 0]), n_lines=1, top_k=1, max_distance=None
        )
        
        assert not results

    def test_format_results(self, mock_documents):
        
        raw_results = [(0.1, mock_documents[0], 0)]

        
        formatted = SearchEngine.format_results(raw_results, n_lines=1)

        
        assert len(formatted) == 1
        assert formatted[0].path == mock_documents[0].path

    def test_get_context_window_middle(self):
        start, end = SearchEngine._get_context_window(line_index=10, total_lines=20, n_lines=3)
        assert start == 7
        assert end == 14

    def test_get_context_window_start(self):
        start, end = SearchEngine._get_context_window(line_index=1, total_lines=20, n_lines=3)
        assert start == 0
        assert end == 5

    def test_get_context_window_end(self):
        start, end = SearchEngine._get_context_window(line_index=18, total_lines=20, n_lines=3)
        assert start == 15
        assert end == 20