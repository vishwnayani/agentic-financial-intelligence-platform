"""
reflection.py

Reflection Agent

Responsibilities
----------------
1. Review the financial analysis.
2. Identify unsupported claims.
3. Suggest improvements.
4. Never invent new information.
"""

from app.graph.state import AgentState
from app.llm.openrouter import get_llm
from app.llm.prompts import REFLECTION_PROMPT


class ReflectionAgent:

    def __init__(self):

        self.llm = get_llm()

    def run(self, state: AgentState) -> AgentState:

        prompt = f"""
{REFLECTION_PROMPT}

Question:

{state["question"]}

Research Summary:

{state["research"]}

Financial Analysis:

{state["analysis"]}

Instructions

Review the financial analysis carefully.

Check for:

- Unsupported claims
- Hallucinations
- Missing evidence
- Logical inconsistencies

If the analysis is already correct,
say so.

Do NOT create new financial facts.
"""

        response = self.llm.invoke(prompt)

        state["reflection"] = response.content

        state["execution_trace"].append("Reflection Agent")

        return state