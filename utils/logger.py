import logging
from pathlib import Path


def configure_logger(log_dir: Path):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "test_run.log", encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

logger = logging.getLogger()
