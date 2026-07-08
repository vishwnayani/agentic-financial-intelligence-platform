import requests

import os

BASE_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
)


def login(email: str, password: str):

    return requests.post(

        f"{BASE_URL}/auth/login",

        json={

            "email": email,

            "password": password

        },

        timeout=60

    )


def register(

    username: str,

    email: str,

    password: str

):

    return requests.post(

        f"{BASE_URL}/auth/register",

        json={

            "username": username,

            "email": email,

            "password": password

        },

        timeout=60

    )


def ask_question(

    token: str,

    question: str

):

    return requests.post(

        f"{BASE_URL}/api/chat",

        headers={

            "Authorization": f"Bearer {token}"

        },

        json={

            "question": question

        },

        timeout=300

    )

def get_history(token: str):

    return requests.get(

        f"{BASE_URL}/api/history",

        headers={

            "Authorization": f"Bearer {token}"

        },

        timeout=60

    )


def get_conversation(

    token: str,

    conversation_id: int

):

    return requests.get(

        f"{BASE_URL}/api/history/{conversation_id}",

        headers={

            "Authorization": f"Bearer {token}"

        },

        timeout=60

    )

def delete_conversation(

    token: str,

    conversation_id: int

):

    return requests.delete(

        f"{BASE_URL}/api/history/{conversation_id}",

        headers={

            "Authorization": f"Bearer {token}"

        },

        timeout=60

    )