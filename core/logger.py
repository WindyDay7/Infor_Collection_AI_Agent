# core/logger.py
import logging
import os
from config import settings


log_file = settings.LOG_FILE
log_level = settings.LOG_LEVEL.upper()

logging.basicConfig(
    level=log_level,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("news_agent")
