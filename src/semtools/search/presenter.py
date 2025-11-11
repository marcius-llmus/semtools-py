from dataclasses import dataclass
from typing import List, Union

from .models import SearchResult
from ..workspace.store import RankedLine


@dataclass
class FormattedResult:
    """A unified structure for presenting a search result to the user."""

    header: str
    lines: List[str]
    highlighted_line_index: int  # relative to `lines`, -1 if none


class SearchResultFormatter:
    """Handles the formatting of search results for display."""

    def __init__(self, n_lines: int, is_tty: bool):
        self.n_lines = n_lines
        self.is_tty = is_tty

    def format_results(
        self, results: Union[List[SearchResult], List[RankedLine]]
    ) -> List[FormattedResult]:
        """Formats a list of raw search results into a display-ready format."""
        if not results:
            return []

        first_result = results[0]
        if isinstance(first_result, SearchResult):
            return [self._format_search_result(res) for res in results]
        elif isinstance(first_result, RankedLine):
            return [self._format_ranked_line(res) for res in results]
        return []

    def _format_search_result(self, res: SearchResult) -> FormattedResult:
        """Formats a single in-memory SearchResult."""
        end = res.context_start_line + len(res.context_lines)
        header = f"{res.path}:{res.context_start_line}::{end} ({res.distance:.4f})"

        formatted_lines, highlighted_index = [], -1
        for i, line in enumerate(res.context_lines):
            line_num = res.context_start_line + i
            line_to_print = f"{line_num + 1:4}: {line}"
            if line_num == res.line_number and self.is_tty:
                highlighted_index = i
            formatted_lines.append(line_to_print)

        return FormattedResult(
            header=header, lines=formatted_lines, highlighted_line_index=highlighted_index
        )

    def _format_ranked_line(self, ranked_line: RankedLine) -> FormattedResult:
        """Formats a single workspace-backed RankedLine, reading the file for context."""
        start = max(0, ranked_line.line_number - self.n_lines)
        header = f"{ranked_line.path}:{start}::{ranked_line.line_number + self.n_lines + 1} ({ranked_line.distance:.4f})"

        try:
            with open(ranked_line.path, "r", encoding="utf-8") as f:
                lines = [line.rstrip("\n") for line in f.readlines()]
            end = min(len(lines), ranked_line.line_number + self.n_lines + 1)
            context_lines = lines[start:end]

            formatted_lines, highlighted_index = [], -1
            for i, line in enumerate(context_lines):
                line_num = start + i
                line_to_print = f"{line_num + 1:4}: {line}"
                if line_num == ranked_line.line_number and self.is_tty:
                    highlighted_index = i
                formatted_lines.append(line_to_print)

            return FormattedResult(
                header=header,
                lines=formatted_lines,
                highlighted_line_index=highlighted_index,
            )
        except (IOError, UnicodeDecodeError):
            return FormattedResult(
                header=header,
                lines=["    [Error: Could not read file content]"],
                highlighted_line_index=-1,
            )
