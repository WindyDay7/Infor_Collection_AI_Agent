# test_search.py (for testing only)
from core.search import search_news

if __name__ == "__main__":
    results = search_news(["intelligent Payment"], num_results=5)
    for article in results[0]:
        print(f"{article['title']}\n{article['link']}\n")
