from app.graph.state import AgentState


def test_state():

    state: AgentState = {

        "question": "Summarize NVIDIA's AI investments.",

        "retrieved_documents": [],

        "plan": "",

        "research": "",

        "analysis": "",

        "reflection": "",

        "answer": "",

        "execution_trace": [],

        "company": None,

        "document_type": None

    }

    print()

    print(state)


if __name__ == "__main__":

    test_state()