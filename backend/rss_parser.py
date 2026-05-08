import feedparser
from datetime import datetime
from sqlalchemy.orm import Session
from models import Article
from config import RSS_FEEDS
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def parse_feed(source_name: str, feed_url: str, db: Session):
    try:
        feed = feedparser.parse(feed_url)

        if feed.bozo:
            logger.warning(f"Feed {source_name} had parsing issues: {feed.bozo_exception}")

        for entry in feed.entries[:10]:  # Limit to 10 articles per feed
            try:
                # Extract article data
                title = entry.get("title", "No Title")
                description = entry.get("summary", entry.get("description", ""))
                url = entry.get("link", "")

                if not url:
                    continue

                # Parse publication date
                pub_date = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    pub_date = datetime(*entry.published_parsed[:6])

                # Check if article already exists
                existing = db.query(Article).filter(Article.url == url).first()
                if existing:
                    continue

                # Create and save article
                article = Article(
                    title=title,
                    description=description[:500],  # Limit description length
                    url=url,
                    source=source_name,
                    pub_date=pub_date,
                )
                db.add(article)

            except Exception as e:
                logger.error(f"Error parsing entry from {source_name}: {e}")
                continue

        db.commit()
        logger.info(f"Successfully fetched articles from {source_name}")

    except Exception as e:
        logger.error(f"Error fetching feed {source_name} ({feed_url}): {e}")
        db.rollback()

def fetch_all_feeds(db: Session):
    logger.info("Starting RSS feed fetch...")
    for source_name, feed_url in RSS_FEEDS.items():
        parse_feed(source_name, feed_url, db)
    logger.info("Finished RSS feed fetch")
