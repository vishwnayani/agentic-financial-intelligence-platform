from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.models import User

from app.schemas.auth import (
    UserRegister,
    UserLogin,
    Token
)

from app.auth.hashing import (
    hash_password,
    verify_password
)

from app.auth.jwt_handler import create_access_token


router = APIRouter()


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/register")
def register(user: UserRegister):

    db: Session = SessionLocal()

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    new_user = User(

        username=user.username,

        email=user.email,

        hashed_password=hash_password(
            user.password
        )

    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    db.close()

    return {

        "message": "Registration successful."

    }


@router.post(
    "/login",
    response_model=Token
)
def login(user: UserLogin):

    db: Session = SessionLocal()

    existing = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials."
        )

    if not verify_password(

        user.password,

        existing.hashed_password

    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid credentials."
        )

    token = create_access_token(

        {

            "sub": existing.email

        }

    )

    db.close()

    return {

        "access_token": token,

        "token_type": "bearer"

    }