from pydantic import BaseModel

# from models.models import Message


class QuestionRequest(BaseModel):
    text: str


class QuestionResponse(BaseModel):
    text: str
