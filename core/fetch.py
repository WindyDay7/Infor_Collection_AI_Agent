# core/fetch.py

import requests
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

# Optional cookie string for authenticated access
COOKIES_RAW = os.getenv("REQUEST_COOKIES")  # Example: "sessionid=xyz; token=abc"

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def parse_cookies(raw_cookie_string: str) -> dict:
    """Parses a raw cookie string into a dictionary."""
    cookies = {}
    for part in raw_cookie_string.split(";"):
        if "=" in part:
            key, val = part.strip().split("=", 1)
            cookies[key] = val
    return cookies

COOKIES = parse_cookies(COOKIES_RAW) if COOKIES_RAW else {}

def fetch_url(url: str, timeout: int = 10) -> Optional[str]:
    """
    Fetches the HTML content of a given URL using optional headers and cookies.
    Returns the raw HTML as a string.
    """
    try:
        response = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching URL: {url}\n{e}")
        return None
