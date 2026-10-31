
import logging
from pathlib import Path

# Project ke main folder ka path find karo
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Logs folder automatically create karo
LOG_DIR = PROJECT_ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log file ka path
LOG_FILE = LOG_DIR / "app.log"


def get_logger(name: str) -> logging.Logger:
    """Create a logger that writes messages to the console and log file."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Duplicate handlers ko prevent karo
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        # File handler
        file_handler = logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger