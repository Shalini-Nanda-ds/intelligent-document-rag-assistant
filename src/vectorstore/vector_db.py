
import faiss
import numpy as np

from src.utils.logger import get_logger

logger = get_logger(__name__)


def create_vector_store(embeddings: np.ndarray):
    """Build a FAISS index for similarity search."""
    vectors = np.asarray(embeddings, dtype="float32")

    if vectors.ndim != 2 or vectors.shape[0] == 0:
        raise ValueError("Embeddings must be a non-empty 2D array")

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    logger.info(
        "FAISS index created | Vectors: %d | Dimensions: %d",
        index.ntotal,
        index.d,
    )

    return index


def search_vector_store(
    index,
    query_embedding: np.ndarray,
    top_k: int = 3,
):
    """Return the closest vector matches for a query."""
    query = np.asarray(query_embedding, dtype="float32").reshape(1, -1)

    if query.shape[1] != index.d:
        raise ValueError("Query embedding dimension does not match index")

    if index.ntotal == 0:
        raise ValueError("Cannot search an empty FAISS index")

    top_k = max(1, min(top_k, index.ntotal))
    scores, indices = index.search(query, top_k)

    logger.info("FAISS search completed | Results: %d", len(indices[0]))

    return scores[0], indices[0]
