from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import desc
from database import init_db, get_db
from models import Article
from scheduler import start_scheduler, stop_scheduler
from rss_parser import fetch_all_feeds
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Initialize database
init_db()

app = FastAPI(title="AI & Crypto News Aggregator")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for response
class ArticleResponse(BaseModel):
    id: int
    title: str
    description: str
    url: str
    source: str
    pub_date: Optional[datetime]
    fetched_date: datetime

    class Config:
        from_attributes = True

@app.on_event("startup")
async def startup_event():
    # Fetch feeds immediately on startup
    db = next(get_db())
    try:
        fetch_all_feeds(db)
    finally:
        db.close()
    # Start background scheduler
    start_scheduler()

@app.on_event("shutdown")
async def shutdown_event():
    stop_scheduler()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/api/articles", response_model=List[ArticleResponse])
async def get_articles(
    limit: int = 50,
    offset: int = 0,
    source: Optional[str] = None,
    db: Session = Depends(get_db),
):
    """Get latest articles, optionally filtered by source"""
    query = db.query(Article)

    if source:
        query = query.filter(Article.source == source)

    articles = query.order_by(desc(Article.pub_date), desc(Article.fetched_date)).offset(offset).limit(limit).all()

    return articles

@app.get("/api/sources")
async def get_sources(db: Session = Depends(get_db)):
    """Get list of all sources with article counts"""
    sources = db.query(Article.source).distinct().all()
    result = []

    for (source,) in sources:
        count = db.query(Article).filter(Article.source == source).count()
        result.append({"source": source, "count": count})

    return sorted(result, key=lambda x: x["count"], reverse=True)

@app.post("/api/refresh")
async def refresh_feeds(db: Session = Depends(get_db)):
    """Manually trigger RSS feed fetch"""
    fetch_all_feeds(db)
    return {"status": "refresh completed"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
