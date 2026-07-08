from app.rag.chunking import get_text_splitter


def test_chunking():

    splitter = get_text_splitter()

    text = (
        "Artificial Intelligence is transforming financial analysis. "
        * 200
    )

    chunks = splitter.split_text(text)

    print(f"Number of chunks: {len(chunks)}")

    print()

    for i, chunk in enumerate(chunks):

        print(f"Chunk {i+1}")

        print(chunk[:100])

        print("-" * 60)


if __name__ == "__main__":

    test_chunking()