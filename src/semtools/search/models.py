from dataclasses import dataclass
import numpy as np
from typing import List


@dataclass
class SearchResult:
    """
    Represents a single search result, mirroring the Rust implementation's structure.
    """

    path: str
    context_lines: List[str]
    context_start_line: int
    line_number: int
    distance: float


@dataclass
class Document:
    """Internal representation of a file's content and embeddings."""

    path: str
    lines: List[str]
    embeddings: np.ndarray