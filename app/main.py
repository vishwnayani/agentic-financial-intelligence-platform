from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.chat import router as chat_router
from app.database.database import engine
from app.database.database import Base
from app.api.auth import router as auth_router
from app.api.history import router as history_router
from app.database import models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Agentic Financial Intelligence Platform",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "project": "Agentic Financial Intelligence Platform",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "database": "Connected",
        "api": "Healthy"
    }


app.include_router(

    chat_router,

    prefix="/api",

    tags=["Chat"]

)

app.include_router(

    auth_router,

    prefix="/auth",

    tags=["Authentication"]

)

app.include_router(

    history_router,

    prefix="/api",

    tags=["History"]

)