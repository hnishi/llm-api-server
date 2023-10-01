from typing import Literal

from pydantic import BaseModel

# from models.models import Message

Collection = Literal["langchain"]


class QuestionRequest(BaseModel):
    text: str
    collection: Collection | None = None


class QuestionResponse(BaseModel):
    text: str
