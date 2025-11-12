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

    def test_create_and_use_new_workspace(self, temp_workspace_dir):
        
        ws_name = "test_ws_1"