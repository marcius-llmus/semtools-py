import sys
from typing import List, Optional

import numpy as np
from model2vec import StaticModel

from .models import Document


class DocumentLoader:
    """Handles loading and processing of documents from various sources."""

    def __init__(self, model: StaticModel, ignore_case: bool = False):
        self.model = model
        self.ignore_case = ignore_case

    @staticmethod
    def normalize_lines(raw_lines: List[str]) -> List[str]:
        """Removes trailing newlines from a list of strings."""
        return [line.rstrip("\n") for line in raw_lines]

    @staticmethod
    def apply_case_sensitivity(lines: List[str], ignore_case: bool) -> List[str]:
        """Applies case folding to a list of strings if required."""
        if ignore_case:
            return [line.lower() for line in lines]
        return lines

    def load(self, files: List[str]) -> List[Document]:
        """Loads documents from files or stdin."""
        if not files and not sys.stdin.isatty():
            return self._load_from_stdin()
        return self._load_from_files(files)

    def _load_from_stdin(self) -> List[Document]:
        """Loads a single document from stdin."""
        documents: List[Document] = []
        if stdin_lines := self.normalize_lines(sys.stdin.readlines()):
            if doc := self._create_document_from_lines("<stdin>", stdin_lines):
                documents.append(doc)
        return documents

    def _load_from_files(self, files: List[str]) -> List[Document]:
        """Loads documents from a list of file paths."""
        documents: List[Document] = []
        for file_path in files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    if lines := self.normalize_lines(f.readlines()):
                        if doc := self._create_document_from_lines(file_path, lines):
                            documents.append(doc)
            except (IOError, UnicodeDecodeError):
                continue
        return documents

    def _create_document_from_lines(
        self, file_path: str, lines: List[str]
    ) -> Optional[Document]:
        """Creates a Document from lines of text."""
        lines_for_embedding = self.apply_case_sensitivity(lines, self.ignore_case)
        embeddings = self.model.encode(lines_for_embedding)

        return Document(
            path=file_path, lines=lines, embeddings=np.array(embeddings)
        )