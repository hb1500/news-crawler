from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from rss_parser import fetch_all_feeds
from database import SessionLocal
from config import FEED_UPDATE_INTERVAL
import logging

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()

def scheduled_fetch():
    db = SessionLocal()
    try:
        fetch_all_feeds(db)
    finally:
        db.close()

def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            scheduled_fetch,
            trigger=IntervalTrigger(minutes=FEED_UPDATE_INTERVAL),
            id="fetch_feeds",
            name="Fetch RSS feeds",
            replace_existing=True,
        )
        scheduler.start()
        logger.info(f"Scheduler started - feeds will update every {FEED_UPDATE_INTERVAL} minutes")

def stop_scheduler():
    if scheduler.running:
        scheduler.shutdown()
