### core/extract.py

from bs4 import BeautifulSoup
from typing import Optional
import re

def extract_main_text(html: str) -> Optional[str]:
    """
    Attempts to extract the main article content from raw HTML.
    Falls back to full text body if no clear article tag found.
    """
    try:
        soup = BeautifulSoup(html, 'html.parser')

        # Try common article containers
        article = soup.find('article')
        if not article:
            # Fallback to main or div with typical content class
            article = soup.find('div', class_=re.compile("(article|content|main|post)"))

        if not article:
            return None

        paragraphs = article.find_all('p')
        text = '\n\n'.join(p.get_text().strip() for p in paragraphs if p.get_text().strip())
        return text.strip() if text else None

    except Exception as e:
        print(f"❌ Error extracting text from HTML: {e}")
        return None