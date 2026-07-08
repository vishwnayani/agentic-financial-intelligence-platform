from app.agents.planner import PlannerAgent
from app.agents.supervisor import SupervisorAgent


def test_supervisor():

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

    planner = PlannerAgent()

    supervisor = SupervisorAgent()

    state = planner.run(state)

    print(state["execution_plan"])

    state = supervisor.run(state)

    print()

    print("=" * 80)

    print("Execution Trace")

    print()

    for step in state["execution_trace"]:

        print(step)

    print()

    print("=" * 80)

    print("Final Answer")

    print()

    print(state["answer"])


if __name__ == "__main__":
    test_supervisor()