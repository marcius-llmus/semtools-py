import json
from unittest.mock import patch

import pytest

from src.semtools.workspace.core import Workspace


class TestWorkspace:
    def test_open_workspace(self, workspace: Workspace):
        
        workspace.save()  # Ensure config file exists
        with patch("os.getenv", return_value="test_ws"):
            
            opened_ws = Workspace.open()
            
            assert opened_ws.config.name == "test_ws"
            assert opened_ws.config.root_dir == workspace.config.root_dir

    def test_open_workspace_not_found_creates_default(self, temp_workspace_dir):
        with patch("os.getenv", return_value="new_ws"):
            
            opened_ws = Workspace.open()
            
            assert opened_ws.config.name == "new_ws"
            assert "new_ws" in opened_ws.config.root_dir

    def test_save_workspace_config(self, workspace: Workspace):
        
        workspace.save()

        
        config_path = workspace._get_config_path_for("test_ws")
        assert config_path.exists()
        with open(config_path, "r") as f:
            data = json.load(f)
        assert data["name"] == "test_ws"

    def test_create_or_use_workspace(self, temp_workspace_dir):
        
        ws_path = temp_workspace_dir.parent / "created_ws"
        
        
        with patch("src.semtools.workspace.core.APP_HOME_DIR", ws_path.parent.parent):
             Workspace.create_or_use("created_ws")

        
        config_path = ws_path / "config.json"
        assert config_path.exists()

    @pytest.mark.asyncio
    async def test_get_status(self, workspace: Workspace, mocker):
        mock_store = mocker.patch("src.semtools.workspace.core.Store")
        await workspace.get_status()
        mock_store.return_value.get_stats.assert_called_once()

    @pytest.mark.asyncio
    async def test_prune(self, workspace: Workspace, workspace_store, tmp_path):
        
        file_to_keep = tmp_path / "keep.txt"
        file_to_keep.touch()
        file_to_delete = tmp_path / "delete.txt"
        file_to_delete.touch()

        workspace_store.get_all_document_paths = lambda: [str(file_to_keep), str(file_to_delete)]
        workspace_store.delete_documents = (lambda paths: None)
        
        file_to_delete.unlink()

        with patch("src.semtools.workspace.core.Store", return_value=workspace_store):
            
            missing = await workspace.prune()

            
            assert missing == [str(file_to_delete)]