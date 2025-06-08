# utils/browser_tools.py

from playwright.sync_api import sync_playwright
from typing import Optional
import time

def fetch_page_with_browser(url: str, wait_time: int = 5, cookies: Optional[list] = None) -> Optional[str]:
    """
    Fetches the full page content using a headless browser (Playwright).
    Optionally injects cookies for logged-in sessions.
    """
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()

            if cookies:
                context.add_cookies(cookies)

            page = context.new_page()
            page.goto(url, timeout=15000)
            time.sleep(wait_time)  # wait for JS to load

            content = page.content()

            browser.close()
            return content

    except Exception as e:
        print(f"❌ Error fetching page with browser: {e}")
        return None

def convert_cookies_from_string(cookie_string: str, domain: str) -> list:
    """
    Converts raw cookie string (e.g., from browser dev tools) into a list of Playwright cookies.
    """
    cookies = []
    for part in cookie_string.split(";"):
        if "=" in part:
            name, value = part.strip().split("=", 1)
            cookies.append({
                "name": name,
                "value": value,
                "domain": domain,
                "path": "/"
            })
    return cookies
