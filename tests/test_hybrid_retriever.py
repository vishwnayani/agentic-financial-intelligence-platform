from app.rag.hybrid_retriever import HybridRetriever


def test_hybrid_retriever():

    retriever = HybridRetriever()

    documents = retriever.retrieve(
        query="What are the major AI investments?",
        company="NVIDIA",
        document_type="10-K",
        k=5
    )

    print()

    print("=" * 80)

    print(f"Retrieved {len(documents)} Documents")

    print("=" * 80)

    for document in documents:

        print(document.metadata)

        print()

        print(document.page_content[:400])

        print()

        print("-" * 80)


if __name__ == "__main__":
    test_hybrid_retriever()