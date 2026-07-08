"""
openrouter.py

Centralized OpenRouter client.
"""

from langchain_openai import ChatOpenAI

from app.config.settings import settings


def get_llm(
    temperature: float = 0.0,
    max_tokens: int = 2048,
):
    return ChatOpenAI(
        model=settings.OPENROUTER_MODEL,
        api_key=settings.OPENROUTER_API_KEY,
        base_url=settings.OPENROUTER_BASE_URL,
        temperature=temperature,
        max_tokens=max_tokens,
    )