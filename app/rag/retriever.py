"""
retriever.py

Creates the semantic retriever used by all agents.
"""

from app.rag.vector_store import get_vector_store


class FinancialRetriever:

    def __init__(self):

        self.vector_store = get_vector_store()

        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k": 5
            }
        )

    def retrieve(self, query: str):

        """
        Returns the top-k relevant chunks.
        """

        return self.retriever.invoke(query)