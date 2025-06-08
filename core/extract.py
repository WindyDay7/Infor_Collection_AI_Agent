### core/extract.py

from bs4 import BeautifulSoup
from typing import Optional
import re
from newspaper import Article
from core.logger import logger


def extract_main_text(html: str) -> Optional[str]:
    from bs4 import BeautifulSoup
    import re

    try:
        soup = BeautifulSoup(html, 'html.parser')

        # Try common article containers first
        article = (
            soup.find('article') or
            soup.find('main') or
            soup.find('div', class_=re.compile("(article|content|main|post|entry)", re.I)) or
            soup.find('div', id=re.compile("(article|content|main|post|entry)", re.I))
        )

        if article:
            paragraphs = article.find_all('p')
        else:
            # Fallback: get all paragraphs
            paragraphs = soup.find_all('p')

        text = '\n\n'.join(p.get_text().strip() for p in paragraphs if p.get_text().strip())
        return text.strip() if text else None

    except Exception as e:
        logger.warning(f"❌ Error extracting main text: {e}")
        return None


def extract_main_text_with_newspaper(html: str) -> Optional[str]:
    article = Article('')
    article.set_html(html)
    article.parse()
    return article.text if article.text.strip() else None
