"""
hybrid_retriever.py

Hybrid retriever for the Agentic Financial Intelligence Platform.

Version 1.0

Uses semantic retrieval with optional metadata filtering.
"""

from typing import Optional

from app.rag.vector_store import get_vector_store


class HybridRetriever:

    def __init__(self):

        self.vector_store = get_vector_store()

    def retrieve(
        self,
        query: str,
        company: Optional[str] = None,
        document_type: Optional[str] = None,
        k: int = 5
    ):
        """
        Retrieve relevant documents.

        Parameters
        ----------
        query : str
            User query.

        company : Optional[str]
            Filter by company.

        document_type : Optional[str]
            Filter by document type (10-K / 10-Q).

        k : int
            Number of documents to return.
        """

        search_kwargs = {
            "k": k
        }

        filters = []

        if company:
            filters.append({"company": company})

        if document_type:
            filters.append({"document_type": document_type})

        if len(filters) == 1:
            search_kwargs["filter"] = filters[0]

        elif len(filters) > 1:
            search_kwargs["filter"] = {
                "$and": filters
            }

        documents = self.vector_store.similarity_search(
            query=query,
            **search_kwargs
        )

        return documents