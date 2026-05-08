import React, { useEffect, useState } from 'react';
import { fetchArticles, fetchSources, refreshFeeds } from '../services/api';
import ArticleCard from './ArticleCard';
import '../styles/ArticleList.css';

const ArticleList = () => {
  const [articles, setArticles] = useState([]);
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedSource, setSelectedSource] = useState(null);
  const [refreshing, setRefreshing] = useState(false);

  useEffect(() => {
    loadData();
  }, [selectedSource]);

  const loadData = async () => {
    setLoading(true);
    setError(null);
    try {
      const articlesData = await fetchArticles(50, 0, selectedSource);
      setArticles(articlesData);

      if (!selectedSource) {
        const sourcesData = await fetchSources();
        setSources(sourcesData);
      }
    } catch (err) {
      setError('Failed to load articles. Please try again later.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleRefresh = async () => {
    setRefreshing(true);
    try {
      await refreshFeeds();
      await loadData();
    } catch (err) {
      setError('Failed to refresh feeds.');
    } finally {
      setRefreshing(false);
    }
  };

  return (
    <div className="article-list-container">
      <div className="list-header">
        <h2>Latest News</h2>
        <button
          className="refresh-btn"
          onClick={handleRefresh}
          disabled={refreshing}
        >
          {refreshing ? 'Refreshing...' : 'Refresh'}
        </button>
      </div>

      <div className="filters">
        <button
          className={`filter-btn ${selectedSource === null ? 'active' : ''}`}
          onClick={() => setSelectedSource(null)}
        >
          All Sources
        </button>
        {sources.map((source) => (
          <button
            key={source.source}
            className={`filter-btn ${selectedSource === source.source ? 'active' : ''}`}
            onClick={() => setSelectedSource(source.source)}
          >
            {source.source} ({source.count})
          </button>
        ))}
      </div>

      {error && <div className="error-message">{error}</div>}

      {loading ? (
        <div className="loading">Loading articles...</div>
      ) : articles.length === 0 ? (
        <div className="no-articles">No articles found. Try refreshing the feed.</div>
      ) : (
        <div className="articles-grid">
          {articles.map((article) => (
            <ArticleCard key={article.id} article={article} />
          ))}
        </div>
      )}
    </div>
  );
};

export default ArticleList;
