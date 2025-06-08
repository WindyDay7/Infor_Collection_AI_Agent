# core/search.py

import requests
from typing import List, Dict
import os
from config import settings
from core.logger import logger

SERPAPI_KEY = settings.SERPAPI_KEY

HEADERS = {
    "User-Agent": settings.USER_AGENT
}

def search_news(querys: List[str], num_results: int = 5) -> List[List[Dict]]:
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

    query_results = []

    for query in querys:
        if not query.strip():
            raise ValueError("Query cannot be empty.")
        # query = query.strip()
        url = "https://serpapi.com/search"
        params = {
            "engine": "google",
            "q": query,
            "tbm": "nws",  # news search
            "tbs": "qdr:m",       # only past week results
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
            # Append the extracted results for this query
            query_results.append(extracted)

        except Exception as e:
            logger.error(f"❌ Error fetching news for query '{query}': {e}")
            return []

    # If multiple queries were provided, return a list of results for each query
    return query_results