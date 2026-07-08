from fastapi import APIRouter
from pydantic import BaseModel

from app.graph.builder import build_graph
from app.graph.state import AgentState

from fastapi import Depends
from app.auth.dependencies import get_current_user

from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.conversation import Conversation
from app.database.models import User

router = APIRouter()

graph = build_graph()


class ChatRequest(BaseModel):

    question: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    current_user: User = Depends(get_current_user)
):

    state: AgentState = {

        "question": request.question,

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

    result = graph.invoke(state)

    db: Session = SessionLocal()

    conversation = Conversation(

        user_id=current_user.id,

        question=request.question,

        answer=result["answer"],

        execution_trace="\n".join(
            result["execution_trace"]
        ),

        company=result["company"],

        document_type=result["document_type"]

    )

    db.add(conversation)

    db.commit()

    db.close()

    return {

        "answer": result["answer"],

        "execution_trace": result["execution_trace"],

        "company": result["company"],

        "document_type": result["document_type"]

    }