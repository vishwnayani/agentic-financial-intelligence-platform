"""
planner.py

Planner Agent

Responsibilities
----------------
1. Understand the user's request.
2. Identify the company.
3. Identify the document type.
4. Produce the execution plan.
"""

from app.graph.state import AgentState
from app.llm.openrouter import get_llm
from app.llm.prompts import PLANNER_PROMPT

from app.models.planner import PlannerOutput


class PlannerAgent:

    def __init__(self):

        llm = get_llm(temperature=0)

        self.llm = llm.with_structured_output(
            PlannerOutput
        )

    def run(self, state: AgentState) -> AgentState:

        question = state["question"]

        prompt = f"""
{PLANNER_PROMPT}

User Question:

{question}

Available Companies

- APPLE
- AMAZON
- GOOGLE
- NVIDIA
- TESLA

Available Documents

- 10-K
- 10-Q

Available execution_plan values

- research
- analyst
- reflection
- writer

Rules

- Use ONLY the exact execution_plan values above.
- Do NOT write sentences.
- Do NOT explain your reasoning.
- Do NOT invent new values.
- Return only the structured output.

Determine:

1. company
2. document_type
3. execution_plan
"""

        plan: PlannerOutput = self.llm.invoke(prompt)

        state["company"] = plan.company

        state["document_type"] = plan.document_type

        state["execution_plan"] = plan.execution_plan

        state["plan"] = plan.model_dump_json(indent=2)

        state["execution_trace"].append("Planner Agent")

        return state