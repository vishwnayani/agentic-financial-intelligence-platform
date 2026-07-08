from app.agents.planner import PlannerAgent


def test_planner():

    state = {

        "question":"Summarize NVIDIA's AI investments",

        "retrieved_documents":[],

        "plan":"",

        "research":"",

        "analysis":"",

        "reflection":"",

        "answer":"",

        "execution_trace":[],

        "company":None,

        "document_type":None,

        "execution_plan":[]
    }

    print("A")

    planner = PlannerAgent()

    print("B")

    state = planner.run(state)

    print("C")

    print()

    print("="*80)

    print(state["company"])

    print()

    print(state["document_type"])

    print()

    print(state["execution_plan"])

    print()

    print(state["execution_trace"])

if __name__ == "__main__":
    test_planner()