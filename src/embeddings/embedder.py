
from sentence_transformers import SentenceTransformer

from src.utils.logger import get_logger

logger = get_logger(__name__)

_model = None


def get_model():
    """Load the embedding model only when needed."""
    global _model

    if _model is None:
        logger.info("Loading embedding model")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        logger.info("Embedding model loaded successfully")

    return _model


def create_embeddings(texts: list[str]):
    """Convert text chunks into numerical vectors."""
    if not texts:
        raise ValueError("Cannot create embeddings from empty text list")

    model = get_model()

    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    logger.info(
        "Created embeddings for %d text items",
        len(texts),
    )

    return embeddings
