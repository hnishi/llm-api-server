from typing import Optional

from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv(verbose=True)

SYSTEM_PROMPT = """
質問に回答してください。
もし答えがわからない場合は、わからないと回答してください。
"""


def generate_answer(question: str, temperature: Optional[float] = None) -> str:
    if temperature is None:
        temperature = 0

    chat_model = ChatOpenAI()

    return chat_model.predict(question)
