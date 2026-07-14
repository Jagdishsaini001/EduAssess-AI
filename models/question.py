from typing import List, Optional

from pydantic import BaseModel, Field


class Question(BaseModel):
    """
    Standard question model for EduAssess AI.
    Every question is option-based.
    """

    question_number: int = Field(...)

    question_type: str = Field(...)

    # Optional supporting material
    # (case study, code, table, numerical data, etc.)
    context: Optional[str] = None

    # Actual question to answer
    question: str = Field(...)

    # Option text only
    # Example:
    # ["True", "False"]
    # ["Residual Dividend Policy", "Stable Dividend Policy", ...]
    options: List[str] = Field(default_factory=list)

    # Always one of:
    # A
    # B
    # C
    # D
    correct_answer: str = Field(...)

    explanation: str = Field(...)

    difficulty: str = Field(...)

    bloom_level: str = Field(...)