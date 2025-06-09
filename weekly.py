from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from agents import news_agent
from config import settings
from core.logger import logger

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', day_of_week='mon', hour=8, minute=0)
def scheduled_job():
    try:
        logger.info(f"Scheduled job started at {datetime.now()}")
        news_agent.run_news_agent(querys=settings.QUERY_LIST)
        logger.info("News agent execution completed.")
    except Exception as e:
        logger.error(f"Scheduled job failed: {e}", exc_info=True)

if __name__ == '__main__':
    logger.info("Starting scheduler...")
    scheduler.start()
    logger.info("Scheduler started successfully.")