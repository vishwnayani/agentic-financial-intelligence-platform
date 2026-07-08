"""
writer.py

Writer Agent

Responsibilities
----------------
1. Read the research summary.
2. Read the financial analysis.
3. Read the reflection.
4. Produce the final response.
"""

from app.graph.state import AgentState
from app.llm.openrouter import get_llm
from app.llm.prompts import WRITER_PROMPT


class WriterAgent:

    def __init__(self):

        self.llm = get_llm()

    def _build_citations(self, documents):

        citations = []

        seen = set()

        for doc in documents:

            company = doc.metadata.get("company", "Unknown")
            document_type = doc.metadata.get("document_type", "Unknown")
            page = doc.metadata.get("page", "Unknown")

            citation = (
                f"{company} | {document_type} | Page {page}"
            )

            if citation not in seen:
                citations.append(citation)
                seen.add(citation)

        return "\n".join(citations)

    def run(self, state: AgentState) -> AgentState:

        citations = self._build_citations(
            state["retrieved_documents"]
        )

        prompt = f"""
{WRITER_PROMPT}

Question:

{state["question"]}

Research Summary:

{state["research"]}

Financial Analysis:

{state["analysis"]}

Reflection:

{state["reflection"]}

Write the final answer.

Requirements:

- Professional tone.
- Well structured.
- Do not repeat information.
- Use ONLY supplied information.
- End with a Sources section.
"""

        response = self.llm.invoke(prompt)

        final_answer = response.content

        final_answer += "\n\nSources\n-------\n"

        final_answer += citations

        state["answer"] = final_answer

        state["execution_trace"].append("Writer Agent")

        return state