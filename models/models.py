from pydantic import BaseModel, Field


class Message(BaseModel):
    text: str = Field(..., description="message text")
