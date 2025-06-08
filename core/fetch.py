# core/fetch.py

import requests
from typing import Optional
import os
from config import settings
import undetected_chromedriver as uc
from core.logger import logger

COOKIES_RAW = settings.COOKIES

HEADERS = DEFAULT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/"
}


# COOKIES = settings.COOKIES

def fetch_url(url: str, timeout: int = 10) -> Optional[str]:
    """
    Fetches the HTML content of a given URL using optional headers and cookies.
    Returns the raw HTML as a string.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        logger.warning(f"❌ Error fetching URL: {url}\n{e}")
        return None

def fetch_page_uc(url)  -> Optional[str]:
    options = uc.ChromeOptions()
    options.headless = True  # 设置为 False 可在调试时看到浏览器
    driver = uc.Chrome(options=options)
    driver.get(url)
    html = driver.page_source
    driver.quit()
    return html