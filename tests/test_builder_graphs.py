from app.graph.builder import build_graph


def test_graph():

    graph = build_graph()

    state = {

        "question": "Summarize NVIDIA's AI investments.",

        "retrieved_documents": [],

        "plan": "",

        "research": "",

        "analysis": "",

        "reflection": "",

        "answer": "",

        "execution_trace": [],

        "company": None,

        "document_type": None,

        "execution_plan": []

    }

    result = graph.invoke(state)

    print()

    print("=" * 80)

    print("Execution Trace")

    print()

    for step in result["execution_trace"]:

        print(step)

    print()

    print("=" * 80)

    print("Final Answer")

    print()

    print(result["answer"])


if __name__ == "__main__":

    test_graph()