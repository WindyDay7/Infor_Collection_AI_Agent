### agents/news_agent.py

from core.search import search_news
from core.fetch import fetch_url, fetch_page_uc
from core.extract import extract_main_text, extract_main_text_with_newspaper
from core.summarize import summarize_article
from core.logger import logger
import os
from datetime import datetime
from config import settings

from typing import List, Dict

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_news_agent(querys: List[str]):
    logger.info("Starting news agent...")
    results = search_news(querys=querys, num_results=settings.NEWS_QUERY)
    query_num = 0

    for result in results:
        markdown_block = []
        for i, article in enumerate(result):
            logger.info(f"Processing article {i+1}: {article['title']}")
            html = fetch_url(article['link'])
            if not html:
                html = fetch_page_uc(article['link'])
            if not html:
                logger.warning(f"Could not fetch HTML for {article['link']}")
                continue

            content = extract_main_text(html)
            if not content:
                content = extract_main_text_with_newspaper(html)
            if not content:
                logger.warning(f"Could not extract main content for {article['title']}")
                continue

            md = summarize_article(article, content)
            markdown_block.append(md)
            logger.info(f"Article {i+1} processed successfully.")

        # Collect all markdown blocks for the day
        date_str = datetime.now().strftime("%Y%m%d")
        out_path = os.path.join(OUTPUT_DIR, f"news_digest_{date_str}.md")

        with open(out_path, "a", encoding="utf-8") as f:
            f.write(f"# 🧠 Weekly AI Information about {querys[query_num]} \n\n")
            f.write("\n---\n\n".join(markdown_block))

        logger.info(f"News agent completed for query: {querys[query_num]}")
        query_num += 1
    
    logger.info("All queries processed successfully.")