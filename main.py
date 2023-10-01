import uvicorn
from fastapi import Body, FastAPI, HTTPException

import logic
from models.api import QuestionRequest, QuestionResponse

app = FastAPI()


@app.post(
    "/question",
    response_model=QuestionResponse,
    description="Question API",
)
async def question(
    req_body: QuestionRequest = Body(...),
):
    try:
        temperature = None
        question = req_body.text
        collection = req_body.collection

        answer = logic.answer(question, collection, temperature)
        return QuestionResponse(text=answer)

    except HTTPException as e:
        raise e
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Internal Service Error")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
