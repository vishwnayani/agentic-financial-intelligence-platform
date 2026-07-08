"""
analyst.py

Financial Analyst Agent

Responsibilities
----------------
1. Read the research summary.
2. Generate financial insights.
3. Do NOT retrieve documents.
"""

from app.graph.state import AgentState
from app.llm.openrouter import get_llm
from app.llm.prompts import ANALYST_PROMPT


class FinancialAnalystAgent:

    def __init__(self):

        self.llm = get_llm()

    def run(self, state: AgentState) -> AgentState:

        research = state["research"]

        prompt = f"""
{ANALYST_PROMPT}

Research Summary:

{research}

Instructions:

- Identify the important financial findings.
- Highlight revenue trends if present.
- Highlight risks if present.
- Highlight growth opportunities if present.
- Do NOT invent numbers.
- Use only the supplied research summary.

Produce a structured financial analysis.
"""

        response = self.llm.invoke(prompt)

        state["analysis"] = response.content

        state["execution_trace"].append("Financial Analyst")

        return state