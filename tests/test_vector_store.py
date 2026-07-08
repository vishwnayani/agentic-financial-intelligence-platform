from app.rag.vector_store import get_vector_store


def test_vector_store():

    vector_store = get_vector_store()

    print()

    print("=" * 60)
    print("Vector Store Created Successfully")
    print("=" * 60)

    print()

    print(vector_store)

    print()

    print("Test Passed")


if __name__ == "__main__":
    test_vector_store()