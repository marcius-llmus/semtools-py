import json
from unittest.mock import patch

import pytest

from semtools.workspace.store import WorkspaceStats
from src.semtools.workspace.core import Workspace
from src.semtools.workspace.errors import WorkspaceError


class TestWorkspace:
    def test_open_workspace(self, workspace: Workspace):
        workspace.save()  # Ensure config file exists
        with patch("os.getenv", return_value="test_ws"):
            opened_ws = Workspace.open()

            assert opened_ws.config.name == "test_ws"
            assert opened_ws.config.root_dir == workspace.config.root_dir

    def test_open_non_existent_workspace_raises_error(self, temp_workspace_dir):
        with patch("os.getenv", return_value="non_existent_ws"):
            with pytest.raises(WorkspaceError, match="not found"):
                Workspace.open()

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

    def test_delete_workspace(self, workspace: Workspace):
        workspace.save()
        ws_path = workspace._get_root_path(workspace.config.name)
        assert ws_path.exists()

        Workspace.delete(workspace.config.name)
        assert not ws_path.exists()

    def test_delete_non_existent_workspace(self):
        with pytest.raises(WorkspaceError):
            Workspace.delete("non_existent_ws")

    @pytest.mark.asyncio
    async def test_get_status(self, workspace: Workspace, mocker):
        mock_store_instance = mocker.AsyncMock()
        mock_store_instance.get_stats.return_value = WorkspaceStats(
            total_documents=0, has_index=False, index_type=None
        )
        mocker.patch("src.semtools.workspace.core.Store.create", return_value=mock_store_instance)

        await workspace.get_status()
        mock_store_instance.get_stats.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_prune(self, workspace: Workspace, tmp_path, mocker):
        file_to_keep = tmp_path / "keep.txt"
        file_to_keep.touch()
        file_to_delete = tmp_path / "delete.txt"
        file_to_delete.touch()

        mock_store_instance = mocker.AsyncMock()
        mock_store_instance.get_all_document_paths.return_value = [
            str(file_to_keep),
            str(file_to_delete),
        ]
        mocker.patch("src.semtools.workspace.core.Store.create", return_value=mock_store_instance)

        file_to_delete.unlink()

        missing = await workspace.prune()

        assert missing == [str(file_to_delete)]
        mock_store_instance.delete_documents.assert_awaited_once_with(missing)