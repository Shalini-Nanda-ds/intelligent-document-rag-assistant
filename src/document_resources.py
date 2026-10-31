from functools import lru_cache

from src.ingestion.pdf_loader import load_pdf
from src.processing.chunker import chunk_text
from src.embeddings.embedder import create_embeddings
from src.vectorstore.vector_db import create_vector_store
from src.utils.logger import get_logger

logger = get_logger(__name__)

PDF_PATH = "data/documents/leave_policy.pdf"


@lru_cache(maxsize=1)
def load_document_resources():
    """Load and process the PDF once, then reuse its resources."""
    logger.info("Preparing document resources")

    document_text = load_pdf(PDF_PATH)

    if not document_text.strip():
        raise ValueError("The PDF contains no extractable text.")

    chunks = chunk_text(document_text)
    embeddings = create_embeddings(chunks)
    index = create_vector_store(embeddings)

    logger.info("Document resources prepared successfully")

    return chunks, index