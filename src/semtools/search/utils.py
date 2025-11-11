from typing import List


def normalize_lines(raw_lines: List[str]) -> List[str]:
    """Removes trailing newlines from a list of strings."""
    return [line.rstrip("\n") for line in raw_lines]


def apply_case_sensitivity(lines: List[str], ignore_case: bool) -> List[str]:
    """Applies case folding to a list of strings if required."""
    if ignore_case:
        return [line.lower() for line in lines]
    return lines
