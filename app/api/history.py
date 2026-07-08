from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.auth.dependencies import get_current_user
from app.database.database import SessionLocal
from app.database.conversation import Conversation
from app.database.models import User

router = APIRouter()


@router.get("/history")
def get_history(
    current_user: User = Depends(get_current_user)
):

    db: Session = SessionLocal()

    conversations = (

        db.query(Conversation)

        .filter(
            Conversation.user_id == current_user.id
        )

        .order_by(
            Conversation.created_at.desc()
        )

        .all()

    )

    db.close()

    return [

        {

            "id": conversation.id,

            "question": conversation.question,

            "company": conversation.company,

            "document_type": conversation.document_type,

            "created_at": conversation.created_at

        }

        for conversation in conversations

    ]


@router.get("/history/{conversation_id}")
def get_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_user)
):

    db: Session = SessionLocal()

    conversation = (

        db.query(Conversation)

        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id == current_user.id
        )

        .first()

    )

    db.close()

    if conversation is None:

        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    return {

        "id": conversation.id,

        "question": conversation.question,

        "answer": conversation.answer,

        "execution_trace": conversation.execution_trace,

        "company": conversation.company,

        "document_type": conversation.document_type,

        "created_at": conversation.created_at

    }


@router.delete("/history/{conversation_id}")
def delete_conversation(
    conversation_id: int,
    current_user: User = Depends(get_current_user)
):

    db: Session = SessionLocal()

    conversation = (

        db.query(Conversation)

        .filter(
            Conversation.id == conversation_id,
            Conversation.user_id == current_user.id
        )

        .first()

    )

    if conversation is None:

        db.close()

        raise HTTPException(
            status_code=404,
            detail="Conversation not found."
        )

    db.delete(conversation)

    db.commit()

    db.close()

    return {

        "message": "Conversation deleted."

    }