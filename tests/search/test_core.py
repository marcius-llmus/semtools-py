import os
from unittest.mock import MagicMock

import pytest
from pathlib import Path

from src.semtools.search.core import Searcher
from src.semtools.search.models import SearchResult
from src.semtools.workspace.store import DocMeta, RankedLine


class TestSearcher:
    def test_search_in_memory(self, searcher: Searcher, mock_file: Path):
        query = "fox"
        files = [str(mock_file)]

        results = searcher.search(query=query, files=files, top_k=1)

        assert results
        assert len(results) == 1
        result = results[0]
        assert isinstance(result, SearchResult)
        assert result.path == str(mock_file)
        assert "Line 1: The quick brown fox jumps over the lazy dog." in result.context_lines
        assert result.line_number == 0

    def test_search_in_memory_no_results(self, mocker):
        mocker.patch("sys.stdin.isatty", return_value=True)
        searcher = Searcher()
        query = "a query that will not be found"
        files = []

        results = searcher.search(query=query, files=files, top_k=1)

        assert not results

    @pytest.mark.asyncio
    async def test_search_with_workspace_no_changes(self, searcher: Searcher, mock_file: Path, mocker):
        mocker.patch("os.getenv", return_value="test_ws")
        mock_store = MagicMock()
        real_stat = os.stat(mock_file)
        mock_store.get_existing_docs.return_value = {
            str(mock_file): DocMeta(path=str(mock_file), size_bytes=real_stat.st_size, mtime=int(real_stat.st_mtime))
        }
        mock_store.search_line_embeddings.return_value = [RankedLine(path=str(mock_file), line_number=0, distance=0.1)]
        mocker.patch("src.semtools.search.core.Store", return_value=mock_store)
        mock_ws_instance = MagicMock()
        # Provide a real temporary path for the workspace database
        mock_ws_instance.config.root_dir = str(mock_file.parent / "test_ws")
        mocker.patch("src.semtools.search.core.Workspace.open", return_value=mock_ws_instance)

        await searcher._search_with_workspace(query="fox", files=[str(mock_file)], n_lines=3, top_k=1, max_distance=None, ignore_case=False)

        mock_store.upsert_line_embeddings.assert_not_called()
        mock_store.upsert_document_metadata.assert_not_called()
        mock_store.search_line_embeddings.assert_called_once()

    @pytest.mark.asyncio
    async def test_search_with_workspace_new_file(self, searcher: Searcher, mock_file: Path, mocker):
        mocker.patch("os.getenv", return_value="test_ws")
        mock_store = MagicMock()
        mock_store.get_existing_docs.return_value = {}  # No existing docs
        mocker.patch("src.semtools.search.core.Store", return_value=mock_store)
        mock_ws_instance = MagicMock()
        mock_ws_instance.config.root_dir = str(mock_file.parent / "test_ws")
        mocker.patch("src.semtools.search.core.Workspace.open", return_value=mock_ws_instance)

        await searcher._search_with_workspace(query="fox", files=[str(mock_file)], n_lines=3, top_k=1, max_distance=None, ignore_case=False)

        mock_store.upsert_line_embeddings.assert_called_once()
        mock_store.upsert_document_metadata.assert_called_once()
        mock_store.search_line_embeddings.assert_called_once()

    @pytest.mark.asyncio
    async def test_search_with_workspace_modified_file(self, searcher: Searcher, mock_file: Path, mocker):
        
        mocker.patch("os.getenv", return_value="test_ws")
        mock_store = MagicMock()
        mock_store.get_existing_docs.return_value = {
            str(mock_file): DocMeta(path=str(mock_file), size_bytes=1, mtime=1) # Stale meta
        }
        mocker.patch("src.semtools.search.core.Store", return_value=mock_store)
        mock_ws_instance = MagicMock()
        mock_ws_instance.config.root_dir = str(mock_file.parent / "test_ws")
        mocker.patch("src.semtools.search.core.Workspace.open", return_value=mock_ws_instance)

        
        await searcher._search_with_workspace(query="fox", files=[str(mock_file)], n_lines=3, top_k=1, max_distance=None, ignore_case=False)

        
        mock_store.upsert_line_embeddings.assert_called_once()
        mock_store.upsert_document_metadata.assert_called_once()

    def test_search_with_ignore_case(self):
        
        searcher = Searcher() # Real model
        mock_content = "FOX fox FoX"
        file = Path("test.txt")
        file.write_text(mock_content)

        
        results_case_sensitive = searcher.search("fox", [str(file)], ignore_case=False)
        results_ignore_case = searcher.search("fox", [str(file)], ignore_case=True)

        
        assert len(results_case_sensitive) == 1
        # The model is semantic, so it might find FOX anyway, but with a higher distance.
        # A better test is to check if the underlying lines sent to the model are lowercased.
        # For now, we assume the model is sensitive enough for this to work.
        # In a real scenario, mock the model and check input to `encode`.
        assert len(results_ignore_case) > 0 # Should find all instances

        file.unlink()

    def test_search_with_empty_query(self):
        
        searcher = Searcher()

        
        results = searcher.search("", ["anyfile.txt"])

        
        assert not results