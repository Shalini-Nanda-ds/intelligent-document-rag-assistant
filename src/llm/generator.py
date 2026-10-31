
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from src.utils.logger import get_logger

logger = get_logger(__name__)

load_dotenv()


def generate_answer(question: str, context: str) -> str:
    """Generate an answer grounded in retrieved document text."""

    logger.info("Preparing Gemini API request")

    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    if not api_key:
        logger.error("Gemini API key is missing")
        raise ValueError(
            "Gemini API key missing. Add GEMINI_API_KEY to your .env file."
        )

    client = genai.Client(
        api_key=api_key,
        http_options=types.HttpOptions(
        timeout=180000,
        retry_options=types.HttpRetryOptions(attempts=2),
    ),
    )

    prompt = f"""
You are a company policy assistant.

Answer the question using ONLY the context below.
If the context does not contain the answer, say:
"I could not find this information in the provided document."

Do not invent company rules.

Context:
{context}

Question:
{question}

Answer:
"""

    logger.info("Sending question to Gemini API")

    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt,
            config={"thinking_config": {"thinking_level": "low"}},
        )

        answer = response.text or "I could not generate an answer."

        logger.info("Gemini response received successfully")

        return answer

    except Exception:
        logger.exception("Gemini API request failed")
        raise
