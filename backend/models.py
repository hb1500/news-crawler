from sqlalchemy import Column, Integer, String, Text, DateTime, func
from datetime import datetime
from database import Base

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text, nullable=True)
    url = Column(String, unique=True, index=True)
    source = Column(String, index=True)
    pub_date = Column(DateTime, nullable=True, index=True)
    fetched_date = Column(DateTime, default=datetime.utcnow, index=True)

    class Config:
        from_attributes = True
