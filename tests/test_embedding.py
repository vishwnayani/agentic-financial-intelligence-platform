from app.rag.embeddings import get_embedding_model


def test_embeddings():

    embedding_model = get_embedding_model()

    embedding = embedding_model.embed_query(
        "What are the major risks discussed in the annual report?"
    )

    print(f"Embedding Dimension : {len(embedding)}")

    print()

    print(embedding[:10])


if __name__ == "__main__":
    test_embeddings()