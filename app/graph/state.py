"""
state.py

Defines the shared state used by every LangGraph node.
"""

from typing import TypedDict, List, Optional

from langchain_core.documents import Document


class AgentState(TypedDict):

    question: str

    retrieved_documents: List[Document]

    plan: str

    research: str

    analysis: str

    reflection: str

    answer: str

    execution_trace: List[str]

    company: Optional[str]

    document_type: Optional[str]

    execution_plan: List[str]