# core/search.py

import requests
from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def search_news(query: str, num_results: int = 5) -> List[Dict]:
    """
    Search for news using SerpAPI's Google News engine.
    
    Returns a list of news articles with keys:
    - title
    - link
    - snippet
    - source
    - date
    """
    if not SERPAPI_KEY:
        raise ValueError("SERPAPI_KEY not found. Please set it in .env.")

    url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "tbm": "nws",  # news search
        "num": num_results,
        "api_key": SERPAPI_KEY
    }

    try:
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()

        results = data.get("news_results", [])
        extracted = []
        for item in results[:num_results]:
            extracted.append({
                "title": item.get("title"),
                "link": item.get("link"),
                "snippet": item.get("snippet"),
                "source": item.get("source"),
                "date": item.get("date")
            })

        return extracted

    except Exception as e:
        print(f"❌ Error fetching news from SerpAPI: {e}")
        return []
