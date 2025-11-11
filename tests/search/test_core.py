import pytest
from pathlib import Path

from src.semtools.search.core import Searcher
from src.semtools.search.models import SearchResult


class TestSearcher:
    def test_search_in_memory(self, searcher: Searcher, mock_file: Path):
        # Arrange
        query = "fox"
        files = [str(mock_file)]

        # Act
        results = searcher.search(query=query, files=files, top_k=1)

        # Assert
        assert results
        assert len(results) == 1
        result = results[0]
        assert isinstance(result, SearchResult)
        assert result.path == str(mock_file)
        assert "Line 1: The quick brown fox jumps over the lazy dog." in result.context_lines
        assert result.line_number == 0

    def test_search_in_memory_no_results(self):
        pass

    @pytest.mark.asyncio
    async def test_search_with_workspace_no_changes(self):
        pass

    @pytest.mark.asyncio
    async def test_search_with_workspace_new_file(self):
        pass

    @pytest.mark.asyncio
    async def test_search_with_workspace_modified_file(self):
        pass

    def test_search_with_ignore_case(self):
        pass

    def test_search_with_empty_query(self):
        pass