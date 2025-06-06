### core/summarize.py

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_article(article_meta: dict, article_text: str) -> str:
    """
    Summarizes the article content using GPT and returns a Markdown block.
    """
    title = article_meta.get("title", "Untitled")
    link = article_meta.get("link", "")
    source = article_meta.get("source", "Unknown Source")
    date = article_meta.get("date", "")

    prompt = f"""
    You are a helpful news summarizer. Given the following article, produce a short and informative Markdown summary:

    Title: {title}
    Source: {source}
    Date: {date}
    Link: {link}

    Article:
    """
    {article_text[:3000]}
    """

    Summary:
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        summary = response.choices[0].message["content"]
        return f"## [{title}]({link})\n\n{summary}\n"
    except Exception as e:
        print(f"❌ OpenAI summarization failed: {e}")
        return f"## [{title}]({link})\n\n_Summary failed._\n"
