### core/summarize.py

from openai import OpenAI
from config import settings
from core.logger import logger

def summarize_article(article_meta: dict, article_text: str) -> str:
    """
    Summarizes the article content using GPT and returns a Markdown block.
    """
    title = article_meta.get("title", "Untitled")
    link = article_meta.get("link", "")
    source = article_meta.get("source", "Unknown Source")
    date = article_meta.get("date", "")

    # You are a helpful news summarizer. Given the following article, produce a short and informative Markdown summary
    prompt = f"""
    下面是一篇 AI 相关的文章, 请抽取其中的关键信息, 然后生成总结性的摘要.:

    Title: {title}
    Source: {source}
    Date: {date}
    Link: {link}

    Article:
    """
    {article_text[:30000]}
    """

    Summary:
    """

    client_open_router = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.OPEN_ROUTER_API_KEY, # OpenRouter API Key
    )

    client_ali_mota = OpenAI(
        base_url='https://api-inference.modelscope.cn/v1/',
        api_key=settings.MOTA_API_KEY, # ModelScope Token
    )

    open_router_models = settings.MODELS.get("open_router_models", []).split(',')
    ali_mota_models = settings.MODELS.get("ali_mota_models", []).split(',')


    # first try ModelScope Open router
    for model in open_router_models:
        model = model.strip()
        try:
            response = client_open_router.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=30000
            )
            summary = response.choices[0].message.content
            logger.info(f"✅ OpenRouter summarization successful with model {model}")
            return f"## [{title}]({link})\n\n{summary}\n"
        except Exception as e:
            logger.warning(f"❌ OpenRouter summarization failed with model {model}: {e}")

    # if OpenRouter fails, try ModelScope MOTA
    for model in ali_mota_models:
        model = model.strip()
        try:
            response = client_ali_mota.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=8192,  # MOTA has a max token limit of 8192
            )
            summary = response.choices[0].message.content
            logger.info(f"✅ ModelScope MOTA summarization successful with model {model}")
            return f"## [{title}]({link})\n\n{summary}\n"

        except Exception as e:
            logger.warning(f"❌ ModelScope MOTA summarization failed with model {model}: {e}")
    
    logger.error("❌ All summarization attempts failed.")
    return f"## [{title}]({link})\n\nFailed to summarize the article.\n"