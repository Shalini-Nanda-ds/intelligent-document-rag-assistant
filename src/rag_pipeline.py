
from src.document_resources import load_document_resources
from src.retrieval.retriever import retrieve_relevant_chunks
from src.llm.generator import generate_answer
from src.utils.logger import get_logger

logger = get_logger(__name__)


def answer_question(question: str) -> str:
    """Answer a question using information from the policy PDF."""

    if not question.strip():
        raise ValueError("Question cannot be empty.")

    logger.info("Starting RAG pipeline")

    chunks, index = load_document_resources()

    retrieved_chunks = retrieve_relevant_chunks(
        query=question,
        chunks=chunks,
        index=index,
        top_k=3,
    )

    if not retrieved_chunks:
        logger.warning("No relevant document context found")
        return "I could not find this information in the provided document."

    context = "\n\n".join(item["text"] for item in retrieved_chunks)

    try:
        answer = generate_answer(question, context)

        logger.info("RAG pipeline completed successfully")
        return answer

    except Exception:
        logger.exception(
            "Gemini unavailable. Returning retrieved document context."
        )

        return (
            "Gemini is temporarily unavailable. "
            "Here is the relevant information extracted from the policy document:\n\n"
            f"{context}"
        )
