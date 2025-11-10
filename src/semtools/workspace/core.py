import json
import os
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .errors import WorkspaceError


@dataclass
class WorkspaceConfig:
    """Configuration for a semtools workspace, mirroring the Rust struct."""

    name: str = "default"
    root_dir: str = ""
    in_batch_size: int = 5_000
    oversample_factor: int = 3


class Workspace:
    """Manages semtools workspaces, configurations, and paths."""

    def __init__(self, config: WorkspaceConfig):
        self.config = config

    @classmethod
    def open(cls) -> "Workspace":
        """Opens the active workspace configuration."""
        active_name = cls.get_active_workspace_name()
        config_path = cls._get_config_path_for(active_name)

        if config_path.exists():
            with open(config_path, "r") as f:
                config_data = json.load(f)
            config = WorkspaceConfig(**config_data)
        else:
            config = WorkspaceConfig(name=active_name)

        if not config.root_dir:
            config.root_dir = str(cls._get_root_path(active_name))

        return cls(config)

    def save(self) -> None:
        """Saves the current workspace configuration to disk."""
        config_path = self._get_config_path_for(self.config.name)
        config_path.parent.mkdir(parents=True, exist_ok=True)

        with open(config_path, "w") as f:
            json.dump(asdict(self.config), f, indent=2)

    @staticmethod
    def get_active_workspace_name() -> str:
        """Gets the name of the active workspace from the environment variable."""
        active = os.getenv("SEMTOOLS_WORKSPACE")
        if not active:
            raise WorkspaceError(
                "No active workspace. Set the SEMTOOLS_WORKSPACE environment variable."
            )
        return active

    @staticmethod
    def _get_root_path(name: str) -> Path:
        """Gets the root directory path for a named workspace."""
        return Path.home() / ".semtools" / "workspaces" / name

    @classmethod
    def _get_config_path_for(cls, name: str) -> Path:
        """Gets the path to the config.json file for a named workspace."""
        return cls._get_root_path(name) / "config.json"