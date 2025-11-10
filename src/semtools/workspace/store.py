from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import lancedb
import pyarrow as pa


@dataclass
class DocMeta:
    """Metadata for a document in the workspace."""

    path: str
    size_bytes: int
    mtime: int


@dataclass
class LineEmbedding:
    """Represents a single line's embedding and metadata."""

    path: str
    line_number: int
    embedding: List[float]


@dataclass
class RankedLine:
    """Represents a search result from the workspace store."""

    path: str
    line_number: int
    distance: float


@dataclass
class WorkspaceStats:
    """Statistics about the workspace."""

    total_documents: int
    has_index: bool
    index_type: Optional[str]


class Store:
    """Manages all database interactions for a semtools workspace."""

    def __init__(self, workspace_dir: str | Path):
        db_path = Path(workspace_dir)
        db_path.mkdir(parents=True, exist_ok=True)
        self.db = lancedb.connect(str(db_path))

    def get_existing_docs(self, paths: List[str]) -> Dict[str, DocMeta]:
        """Gets existing document metadata for the given paths."""
        if "documents" not in self.db.table_names():
            return {}

        tbl = self.db.open_table("documents")
        path_filter = " OR ".join([f"path = '{p}'" for p in paths])
        results = tbl.search().where(path_filter).to_list()

        return {
            r["path"]: DocMeta(
                path=r["path"], size_bytes=r["size_bytes"], mtime=r["mtime"]
            )
            for r in results
        }

    def _delete_document_metadata(self, paths: List[str]) -> None:
        if not paths or "documents" not in self.db.table_names():
            return
        tbl = self.db.open_table("documents")
        path_filter = " OR ".join([f"path = '{p}'" for p in paths])
        tbl.delete(path_filter)

    def _delete_line_embeddings(self, paths: List[str]) -> None:
        if not paths or "line_embeddings" not in self.db.table_names():
            return
        tbl = self.db.open_table("line_embeddings")
        path_filter = " OR ".join([f"path = '{p}'" for p in paths])
        tbl.delete(path_filter)

    def delete_documents(self, paths: List[str]) -> None:
        """Deletes documents and all associated line embeddings by path."""
        self._delete_document_metadata(paths)
        self._delete_line_embeddings(paths)

    def upsert_document_metadata(self, metas: List[DocMeta]) -> None:
        """Upserts document metadata for tracking file changes."""
        if not metas:
            return

        paths = [m.path for m in metas]
        self._delete_document_metadata(paths)

        data = [
            {"path": m.path, "size_bytes": m.size_bytes, "mtime": m.mtime} for m in metas
        ]

        if "documents" not in self.db.table_names():
            schema = pa.schema(
                [
                    pa.field("path", pa.string()),
                    pa.field("size_bytes", pa.int64()),
                    pa.field("mtime", pa.int64()),
                ]
            )
            self.db.create_table("documents", data=data, schema=schema)
        else:
            tbl = self.db.open_table("documents")
            tbl.add(data)

    def upsert_line_embeddings(self, line_embeddings: List[LineEmbedding]) -> None:
        """Upserts line-level embeddings for documents."""
        if not line_embeddings:
            return

        paths = sorted(list({le.path for le in line_embeddings}))
        self._delete_line_embeddings(paths)

        dim = len(line_embeddings[0].embedding)
        data = [
            {
                "path": le.path,
                "line_number": le.line_number,
                "vector": le.embedding,
            }
            for le in line_embeddings
        ]

        if "line_embeddings" not in self.db.table_names():
            from lancedb.pydantic import LanceModel, Vector

            class LineSchema(LanceModel):
                path: str
                line_number: int
                vector: Vector(dim)

            self.db.create_table("line_embeddings", schema=LineSchema, data=data)
        else:
            tbl = self.db.open_table("line_embeddings")
            tbl.add(data)

        self._ensure_line_vector_index()

    def _ensure_line_vector_index(self) -> None:
        """Ensures a vector index exists for the line embeddings table."""
        tbl = self.db.open_table("line_embeddings")
        indexes = tbl.list_indexes()
        if not any(idx["name"] == "vector_idx" for idx in indexes):
            try:
                # num_partitions must be a power of 2
                num_rows = len(tbl)
                num_partitions = 2 ** math.floor(math.log2(max(1, num_rows / 256)))
                if num_partitions == 0:
                    num_partitions = 1

                tbl.create_index(
                    metric="cosine",
                    num_partitions=num_partitions,
                    num_sub_vectors=min(32, 2 ** math.floor(math.log2(max(1, num_rows / 1000)))),
                    vector_column_name="vector",
                    replace=True,
                )
            except Exception as e:
                if "Not enough data to train" in str(e):
                    print(
                        "Warning: Skipping vector index creation due to insufficient data."
                    )
                else:
                    raise e

    def get_all_document_paths(self) -> List[str]:
        """Gets all document paths in the workspace."""
        if "documents" not in self.db.table_names():
            return []
        tbl = self.db.open_table("documents")
        return [row["path"] for row in tbl.search().select(["path"]).to_list()]

    def get_stats(self) -> WorkspaceStats:
        """Get statistics about the workspace store."""
        table_names = self.db.table_names()
        doc_count = 0
        has_index = False

        if "documents" in table_names:
            doc_table = self.db.open_table("documents")
            doc_count = len(doc_table)

        if "line_embeddings" in table_names:
            line_table = self.db.open_table("line_embeddings")
            if len(line_table.list_indexes()) > 0:
                has_index = True

        return WorkspaceStats(
            total_documents=doc_count, has_index=has_index, index_type="IVF_PQ" if has_index else None
        )

    def search_line_embeddings(
        self,
        query_vec: List[float],
        subset_paths: List[str],
        top_k: int,
        max_distance: Optional[float] = None,
    ) -> List[RankedLine]:
        """Searches line embeddings directly for precise results."""
        if not subset_paths or "line_embeddings" not in self.db.table_names():
            return []

        tbl = self.db.open_table("line_embeddings")
        path_filter = " OR ".join([f"path = '{p}'" for p in subset_paths])

        query = tbl.search(query_vec).where(path_filter).limit(top_k).metric("cosine")

        results = query.to_list()

        ranked_lines = [
            RankedLine(
                path=r["path"], line_number=r["line_number"], distance=r["_distance"]
            )
            for r in results
        ]

        if max_distance is not None:
            return [r for r in ranked_lines if r.distance <= max_distance]

        return ranked_lines