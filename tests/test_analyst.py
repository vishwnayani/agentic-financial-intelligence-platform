from app.agents.researcher import ResearchAgent
from app.agents.analyst import FinancialAnalystAgent


def test_analyst():

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

    state = researcher.run(state)

    state = analyst.run(state)

    print()

    print("=" * 80)

    print("Execution Trace")

    print(state["execution_trace"])

    print()

    print("=" * 80)

    print("Analysis")

    print()

    print(state["analysis"])
    

if __name__ == "__main__":
    test_analyst()