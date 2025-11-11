from typing import List, Optional

from model2vec import StaticModel

from .loader import DocumentLoader
from .engine import SearchEngine
from .enums import EmbeddingModel
from .models import SearchResult


class Searcher:
    """
    Encapsulates the logic for semantic search, mirroring the Rust implementation.
    """

    def __init__(self, model_name: EmbeddingModel = EmbeddingModel.POTION_MULTI_LINGUAL_128M):
        self.model = StaticModel.from_pretrained(model_name)

    def search(
        self,
        query: str,
        files: List[str],
        n_lines: int = 3,
        top_k: int = 3,
        max_distance: Optional[float] = None,
        ignore_case: bool = False,
    ) -> List[SearchResult]:
        """
        Orchestrates a search across files or stdin, mirroring the Rust binary's logic.
        """
        processed_query = query.lower() if ignore_case else query

        query_embedding = self.model.encode([processed_query])[0]

        doc_loader = DocumentLoader(self.model, ignore_case=ignore_case)
        documents = doc_loader.load(files)

        if not documents:
            raise ValueError(f"No documents loaded")

        return SearchEngine.rank_results(
            documents, query_embedding, n_lines, top_k, max_distance
        )
