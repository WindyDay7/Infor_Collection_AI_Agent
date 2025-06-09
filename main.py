from config import settings
from core.logger import logger
from agents import news_agent

def main():
  news_agent.run_news_agent(querys=settings.QUERY_LIST)
  logger.info("News agent execution completed.")

if __name__ == "__main__":
  main()