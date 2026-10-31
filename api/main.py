from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.rag_pipeline import answer_question
from src.utils.logger import get_logger

logger = get_logger(__name__)

app = FastAPI(
    title="Intelligent Document RAG Assistant API",
    description="API for document-based question answering using RAG.",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Intelligent Document RAG Assistant API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        answer = answer_question(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    except Exception:
        logger.exception("API failed to answer question")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing the question."
        )