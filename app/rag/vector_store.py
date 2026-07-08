"""
vector_store.py

Creates and loads the Chroma vector database used
throughout the project.
"""

from pathlib import Path

from langchain_chroma import Chroma

from app.rag.embeddings import get_embedding_model


# Persistent storage location
CHROMA_DB_PATH = Path("data/chroma_db")


def get_vector_store() -> Chroma:
    """
    Creates (if needed) and returns the Chroma vector store.
    """

    vector_store = Chroma(
        collection_name="financial_documents",
        embedding_function=get_embedding_model(),
        persist_directory=str(CHROMA_DB_PATH)
    )

    return vector_store