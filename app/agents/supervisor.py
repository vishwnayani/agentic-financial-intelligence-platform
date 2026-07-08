"""
supervisor.py

Supervisor Agent

Responsibilities
----------------
1. Execute agents according to the planner.
2. Manage execution flow.
3. Return the final state.
"""

from app.graph.state import AgentState

from app.agents.researcher import ResearchAgent
from app.agents.analyst import FinancialAnalystAgent
from app.agents.reflection import ReflectionAgent
from app.agents.writer import WriterAgent


class SupervisorAgent:

    def __init__(self):

        self.agents = {

        "research": ResearchAgent(),

        "analyst": FinancialAnalystAgent(),

        "reflection": ReflectionAgent(),

        "writer": WriterAgent()

    }

    def run(self, state: AgentState) -> AgentState:

        execution_plan = state["execution_plan"]

        for agent_name in execution_plan:

            agent = self.agents.get(agent_name)

            if agent is None:
                continue

            state = agent.run(state)

        state["execution_trace"].append("Supervisor Agent")

        return state