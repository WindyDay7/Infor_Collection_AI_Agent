### agents/news_agent.py

from core.search import search_news
from core.fetch import fetch_url
from core.extract import extract_main_text
from core.summarize import summarize_article
import os
from datetime import datetime

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_news_agent():
    print("🔍 Searching for news...")
    results = search_news("AI in payment systems", num_results=5)

    markdown_blocks = []
    for i, article in enumerate(results):
        print(f"\n📄 ({i+1}) {article['title']}")
        html = fetch_url(article['link'])
        if not html:
            continue

        content = extract_main_text(html)
        if not content:
            print("⚠️  Could not extract main content.")
            continue

        md = summarize_article(article, content)
        markdown_blocks.append(md)

    date_str = datetime.now().strftime("%Y%m%d")
    out_path = os.path.join(OUTPUT_DIR, f"news_digest_{date_str}.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("# 🧠 Daily AI & Payment News Digest\n\n")
        f.write("\n---\n\n".join(markdown_blocks))

    print(f"\n✅ Summary saved to {out_path}")