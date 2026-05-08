import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./articles.db")

RSS_FEEDS = {
    # AI News Sources
    "OpenAI": "https://openai.com/blog/rss.xml",
    "Google AI": "https://ai.googleblog.com/feeds/posts/default",
    "MIT News (AI)": "https://news.mit.edu/rss/topic/artificial-intelligence",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "The Batch": "https://www.deeplearning.ai/the-batch/feed/",

    # Crypto News Sources
    "CoinDesk": "https://feeds.coindesk.com/news/rss",
    "Cointelegraph": "https://cointelegraph.com/feed",
    "The Block": "https://www.theblockresearch.com/feed",
    "Bitcoin Magazine": "https://bitcoinmagazine.com/feed",
    "Ethereum Blog": "https://blog.ethereum.org/feed.xml",

    # General Tech News
    "TechCrunch": "https://techcrunch.com/feed",
    "Hacker News": "https://news.ycombinator.com/rss",
}

# Feed update interval in minutes
FEED_UPDATE_INTERVAL = 120

# Number of articles to keep (older ones are soft-deleted)
MAX_ARTICLES_PER_SOURCE = 100
