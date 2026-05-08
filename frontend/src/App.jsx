import React from 'react';
import ArticleList from './components/ArticleList';
import './styles/App.css';

function App() {
  return (
    <div className="app">
      <header className="app-header">
        <h1>🤖 AI & Crypto News</h1>
        <p className="subtitle">Stay updated with the latest in AI and cryptocurrency</p>
      </header>
      <main className="app-main">
        <ArticleList />
      </main>
      <footer className="app-footer">
        <p>&copy; 2024 AI & Crypto News Aggregator. Built with FastAPI & React.</p>
      </footer>
    </div>
  );
}

export default App;
