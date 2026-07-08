from app.llm.openrouter import get_llm


def test_llm():

    llm = get_llm()

    response = llm.invoke(
        "Explain what Retrieval-Augmented Generation is in one paragraph."
    )

    print()

    print("=" * 80)

    print(response.content)

    print()

    print("=" * 80)

    print("LLM Working Successfully")


if __name__ == "__main__":
    test_llm()