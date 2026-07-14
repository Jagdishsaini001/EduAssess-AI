from pydantic import BaseModel
from typing import List

from models.question import Question


class AssessmentOutput(BaseModel):

    assessment_name: str

    subject: str

    chapter: str

    topic: str

    prompt_version: str

    questions: List[Question]