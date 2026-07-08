"""
builder.py

Builds the LangGraph workflow.
"""

from langgraph.graph import StateGraph, END

from app.graph.state import AgentState

from app.agents.planner import PlannerAgent
from app.agents.supervisor import SupervisorAgent


planner = PlannerAgent()
supervisor = SupervisorAgent()


def planner_node(state: AgentState):

    return planner.run(state)


def supervisor_node(state: AgentState):

    return supervisor.run(state)


def build_graph():

    workflow = StateGraph(AgentState)

    workflow.add_node(
        "planner",
        planner_node
    )

    workflow.add_node(
        "supervisor",
        supervisor_node
    )

    workflow.set_entry_point("planner")

    workflow.add_edge(
        "planner",
        "supervisor"
    )

    workflow.add_edge(
        "supervisor",
        END
    )

    return workflow.compile()