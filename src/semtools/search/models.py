from dataclasses import dataclass
import numpy as np
from typing import List


@dataclass
class SearchResult:
    """
    Represents a single search result, mirroring the Rust implementation's structure.
    """

    file_path: str
    context_lines: List[str]
    context_start_line: int
    match_line_index: int
    distance: float


@dataclass
class Document:
    """Internal representation of a file's content and embeddings."""

    file_path: str
    lines: List[str]
    embeddings: np.ndarray
