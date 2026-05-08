import React from 'react';
import '../styles/ArticleCard.css';

const ArticleCard = ({ article }) => {
  const formatDate = (dateString) => {
    if (!dateString) return 'Date unavailable';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  };

  return (
    <article className="article-card">
      <div className="article-header">
        <h3 className="article-title">{article.title}</h3>
        <span className="article-source">{article.source}</span>
      </div>

      <p className="article-description">
        {article.description || 'No description available'}
      </p>

      <div className="article-footer">
        <span className="article-date">{formatDate(article.pub_date)}</span>
        <a
          href={article.url}
          target="_blank"
          rel="noopener noreferrer"
          className="read-more"
        >
          Read More →
        </a>
      </div>
    </article>
  );
};

export default ArticleCard;
