"""
==============================================================================
EduAssess AI
------------------------------------------------------------------------------
Version : 0.5.0
Module  : Assessment Model
==============================================================================
"""

from typing import Dict

from pydantic import BaseModel, Field


class Assessment(BaseModel):
    """
    Assessment request model used to build
    the Gemini prompt.
    """

    assessment_name: str = Field(...)

    purpose: str = Field(...)

    programme: str = Field(...)

    semester: str = Field(...)

    course: str = Field(...)

    subject: str = Field(...)

    chapter: str = Field(...)

    topic: str = Field(...)

    knowledge_source: str = Field(...)

    bloom_level: str = Field(...)

    ai_behaviour: str = Field(...)

    additional_instructions: str = Field(default="")

    question_blueprint: Dict[str, int] = Field(default_factory=dict)