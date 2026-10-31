
from src.embeddings.embedder import create_embeddings
from src.vectorstore.vector_db import search_vector_store
from src.utils.logger import get_logger

logger = get_logger(__name__)

MIN_RELEVANCE_SCORE = 0.30


def retrieve_relevant_chunks(
    query: str,
    chunks: list[str],
    index,
    top_k: int = 3,
    min_score: float = MIN_RELEVANCE_SCORE,
) -> list[dict]:
    """Find relevant document chunks for a question."""

    if not query.strip():
        raise ValueError("Query cannot be empty")

    if not chunks:
        raise ValueError("No document chunks available for retrieval")

    logger.info("Retrieving relevant chunks for query")

    query_embedding = create_embeddings([query])

    scores, indices = search_vector_store(
        index,
        query_embedding,
        top_k=top_k,
    )

    results = []

    for score, idx in zip(scores, indices):
        if idx < 0 or score < min_score:
            continue

        results.append({
            "text": chunks[int(idx)],
            "score": float(score),
        })

    logger.info(
        "Retrieved %d relevant chunks | Threshold: %.2f",
        len(results),
        min_score,
    )

    return results
