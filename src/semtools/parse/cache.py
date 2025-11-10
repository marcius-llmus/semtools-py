import hashlib
from pathlib import Path
from typing import Optional


class CacheManager:
    """Manages the local file cache for parsed documents."""

    def __init__(self, cache_dir: Path):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _get_cache_key(self, file_path: str) -> str:
        """Generates a SHA256 hash of the file path to use as a cache key."""
        return hashlib.sha256(file_path.encode()).hexdigest()

    def should_skip_file(self, file_path: str) -> bool:
        """
        Determines if a file should be skipped from parsing.

        Mirrors the Rust implementation's logic to skip already-readable files.
        """
        return Path(file_path).suffix.lower() in [".md", ".markdown", ".txt"]

    async def get_cached_result(self, file_path: str) -> Optional[Path]:
        """
        Returns the path to the cached result if it exists.

        Args:
            file_path: The original path of the file.

        Returns:
            A Path object to the cached file, or None if not in cache.
        """
        cache_key = self._get_cache_key(file_path)
        original_suffix = Path(file_path).suffix
        cached_file_path = self.cache_dir / f"{cache_key}{original_suffix}.md"

        if cached_file_path.exists():
            return cached_file_path
        return None

    async def write_results_to_disk(
        self, file_path: str, content: str
    ) -> Path:
        """Writes the parsed markdown content to the cache."""
        cache_key = self._get_cache_key(file_path)
        original_suffix = Path(file_path).suffix
        cached_file_path = self.cache_dir / f"{cache_key}{original_suffix}.md"

        with open(cached_file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return cached_file_path