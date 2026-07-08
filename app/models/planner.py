from typing import List, Literal
from pydantic import BaseModel, Field


class PlannerOutput(BaseModel):

    company: Literal[
        "APPLE",
        "AMAZON",
        "GOOGLE",
        "NVIDIA",
        "TESLA"
    ]

    document_type: Literal[
        "10-K",
        "10-Q"
    ]

    execution_plan: List[
        Literal[
            "research",
            "analyst",
            "reflection",
            "writer"
        ]
    ] = Field(
        description="Ordered list of agent identifiers."
    )