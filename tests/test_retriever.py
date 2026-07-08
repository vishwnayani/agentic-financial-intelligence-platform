from app.rag.retriever import FinancialRetriever


def test_retriever():

    retriever = FinancialRetriever()

    query = "What are the major risks discussed by Apple?"

    documents = retriever.retrieve(query)

    print()

    print("=" * 80)

    print(f"Retrieved {len(documents)} Documents")

    print("=" * 80)

    print()

    for i, document in enumerate(documents, start=1):

        print(f"Document {i}")

        print("-" * 60)

        print(document.page_content[:500])

        print()

        print(document.metadata)

        print()

        print("=" * 80)


if __name__ == "__main__":

    test_retriever()