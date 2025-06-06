# scheduler/weekly.py

from apscheduler.schedulers.blocking import BlockingScheduler
from agents.news_agent import run_news_agent

def job():
    print("🕒 Weekly news agent is running...")
    run_news_agent()

def start_weekly_scheduler():
    scheduler = BlockingScheduler()
    
    # Run every Monday at 09:00 AM
    scheduler.add_job(job, 'cron', day_of_week='mon', hour=9, minute=0)

    print("✅ Weekly scheduler started (runs every Monday 09:00 AM).")
    scheduler.start()

if __name__ == "__main__":
    start_weekly_scheduler()
