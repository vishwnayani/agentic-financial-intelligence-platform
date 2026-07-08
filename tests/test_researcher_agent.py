from app.agents.researcher import ResearchAgent


def test_research_agent():

    state = {

        "question": "Summarize NVIDIA's AI strategy.",

        "retrieved_documents": [],

        "plan": "",

        "research": "",

        "analysis": "",

        "reflection": "",

        "answer": "",

        "execution_trace": [],

        "company": "NVIDIA",

        "document_type": "10-K"

    }

    agent = ResearchAgent()

    state = agent.run(state)

    print()

    print("=" * 80)

    print("Execution Trace")

    print(state["execution_trace"])

    print()

    print("=" * 80)

    print("Research Summary")

    print()

    print(state["research"])

    print()

    print("=" * 80)

    print(f"Retrieved Documents : {len(state['retrieved_documents'])}")