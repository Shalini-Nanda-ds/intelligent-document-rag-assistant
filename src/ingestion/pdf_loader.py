
from pathlib import Path
from pypdf import PdfReader

from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""

    pdf_path = Path(file_path)

    logger.info("Starting PDF loading: %s", pdf_path.name)

    try:
        reader = PdfReader(str(pdf_path))
        pages_text = []

        for page in reader.pages:
            text = page.extract_text() or ""
            pages_text.append(text)

        full_text = "\n".join(pages_text)

        logger.info(
            "PDF loaded successfully: %s | Pages: %d | Characters: %d",
            pdf_path.name,
            len(reader.pages),
            len(full_text),
        )

        return full_text

    except Exception:
        logger.exception("Failed to load PDF: %s", pdf_path)
        raise
