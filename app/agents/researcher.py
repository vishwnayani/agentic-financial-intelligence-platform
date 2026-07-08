"""
researcher.py

Research Agent

Responsibilities
----------------
1. Retrieve relevant financial document chunks.
2. Build context.
3. Generate an objective research summary.
4. Update AgentState.
"""

from app.graph.state import AgentState
from app.rag.hybrid_retriever import HybridRetriever
from app.llm.openrouter import get_llm
from app.llm.prompts import RESEARCH_PROMPT


class ResearchAgent:

    def __init__(self):

        self.retriever = HybridRetriever()

        self.llm = get_llm()

    def _build_context(self, documents):

        context = []

        for doc in documents:

            metadata = doc.metadata

            company = metadata.get("company", "Unknown")

            document_type = metadata.get(
                "document_type",
                "Unknown"
            )

            page = metadata.get("page", "Unknown")

            context.append(

                f"""
Company: {company}

Document Type: {document_type}

Page: {page}

Content:
{doc.page_content}
"""
            )

        return "\n\n".join(context)

    def run(self, state: AgentState) -> AgentState:

        question = state["question"]

        documents = self.retriever.retrieve(

            query=question,

            company=state.get("company"),

            document_type=state.get("document_type")
        )

        context = self._build_context(documents)

        prompt = f"""
{RESEARCH_PROMPT}

You are the Research Agent.

Your job is ONLY to summarize the retrieved evidence.

Do NOT perform financial analysis.

Do NOT speculate.

Do NOT answer beyond the supplied context.

Question:

{question}

Context:

{context}

Produce an objective research summary.
"""

        response = self.llm.invoke(prompt)

        state["retrieved_documents"] = documents

        state["research"] = response.content

        state["execution_trace"].append("Research Agent")

        return state