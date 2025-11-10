from dataclasses import dataclass
from typing import List


@dataclass
class SearchResult:
    """
    Represents a single search result, mirroring the Rust implementation's structure.
    """

    file_path: str
    context_lines: List[str]
    context_start_line: int  # 0-based index of the first line in context_lines
    match_line_index: int  # 0-based index of the matching line within the original file
    distance: float