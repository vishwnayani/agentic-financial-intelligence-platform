from app.agents.researcher import ResearchAgent
from app.agents.analyst import FinancialAnalystAgent
from app.agents.reflection import ReflectionAgent


def test_reflection():

    state = {

        "question": "Summarize NVIDIA's AI investments.",

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

    researcher = ResearchAgent()
    analyst = FinancialAnalystAgent()
    reflection = ReflectionAgent()

    state = researcher.run(state)
    state = analyst.run(state)
    state = reflection.run(state)

    print()

    print("=" * 80)

    print("Execution Trace")

    print(state["execution_trace"])

    print()

    print("=" * 80)

    print("Reflection")

    print()

    print(state["reflection"])


if __name__ == "__main__":
    test_reflection()