# AI & Crypto News Aggregator

A modern web application that aggregates the latest news about AI and cryptocurrency from reliable RSS feed sources. Built with **FastAPI** (backend) and **React** (frontend).

## Features

✨ **Real-time News Aggregation** - Automatically fetches articles from 12+ trusted sources  
📰 **Clean, Responsive UI** - Beautiful card-based layout that works on all devices  
🔄 **Auto-refresh** - Backend fetches feeds every 2 hours (configurable)  
🎯 **Source Filtering** - Filter articles by news source  
🚀 **Fast & Efficient** - Built with FastAPI and React for optimal performance

## Tech Stack

**Backend:**
- FastAPI - Modern Python web framework
- SQLAlchemy - ORM for database management
- APScheduler - Background task scheduling
- feedparser - RSS feed parsing

**Frontend:**
- React 18 - UI framework
- Axios - HTTP client
- CSS3 - Responsive styling

**Database:**
- SQLite (development)
- PostgreSQL (production ready)

## News Sources

### AI News
- OpenAI Blog
- Google AI Blog
- MIT News (AI)
- Hugging Face Blog
- The Batch (by Andrew Ng)

### Crypto News
- CoinDesk
- Cointelegraph
- The Block Crypto
- Bitcoin Magazine
- Ethereum Foundation Blog

### General Tech
- TechCrunch
- Hacker News

## Getting Started

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn

### Backend Setup

1. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the FastAPI server:**
   ```bash
   python -m uvicorn main:app --reload
   ```
   
   The API will be available at `http://localhost:8000`
   - API docs: `http://localhost:8000/docs`
   - Health check: `http://localhost:8000/health`

3. **API Endpoints:**
   - `GET /api/articles?limit=50&offset=0` - Get latest articles
   - `GET /api/articles?source=OpenAI` - Filter by source
   - `GET /api/sources` - Get all sources with article counts
   - `POST /api/refresh` - Manually trigger RSS feed fetch

### Frontend Setup

1. **Install dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm start
   ```
   
   The app will open at `http://localhost:3000`

3. **Build for production:**
   ```bash
   npm run build
   ```

## Project Structure

```
.
├── backend/
│   ├── main.py                 # FastAPI app entry point
│   ├── models.py               # SQLAlchemy Article model
│   ├── database.py             # Database setup & connection
│   ├── rss_parser.py           # RSS feed fetching & parsing
│   ├── scheduler.py            # Background task scheduler
│   ├── config.py               # Configuration & RSS feed list
│   └── requirements.txt        # Python dependencies
├── frontend/
│   ├── public/
│   │   └── index.html         # HTML template
│   ├── src/
│   │   ├── components/
│   │   │   ├── ArticleCard.jsx     # Individual article display
│   │   │   └── ArticleList.jsx     # Article feed container
│   │   ├── services/
│   │   │   └── api.js              # API client
│   │   ├── styles/
│   │   │   ├── App.css
│   │   │   ├── ArticleCard.css
│   │   │   ├── ArticleList.css
│   │   │   └── index.css
│   │   ├── App.jsx            # Main app component
│   │   └── index.js           # React entry point
│   ├── package.json           # Node dependencies
│   └── .env                   # Environment variables
└── README.md
```

## Development Workflow

1. **Terminal 1 - Backend:**
   ```bash
   cd backend
   python -m uvicorn main:app --reload
   ```

2. **Terminal 2 - Frontend:**
   ```bash
   cd frontend
   npm start
   ```

3. **View the app:** Open `http://localhost:3000` in your browser

## Configuration

### Backend Configuration
Edit `backend/config.py` to:
- Change RSS feed sources
- Adjust feed update interval (default: 120 minutes)
- Set database URL

### Frontend Configuration
Edit `frontend/.env` to:
- Change API URL for different environments
- Customize API base path

## API Response Example

```json
[
  {
    "id": 1,
    "title": "GPT-4 Achieves New Milestone",
    "description": "OpenAI announces breakthrough results...",
    "url": "https://openai.com/blog/gpt-4",
    "source": "OpenAI",
    "pub_date": "2024-05-08T10:30:00",
    "fetched_date": "2024-05-08T15:45:30"
  }
]
```

## Database Schema

### Article Table
| Column | Type | Notes |
|--------|------|-------|
| id | Integer | Primary key |
| title | String | Article title |
| description | Text | Article summary |
| url | String | Unique article URL |
| source | String | News source name |
| pub_date | DateTime | Publication date |
| fetched_date | DateTime | When article was fetched |

## Deployment

### Backend (FastAPI)
Options:
- **Heroku** - `git push heroku main`
- **Railway** - Connect GitHub repo, auto-deploy
- **PythonAnywhere** - Upload & configure
- **Docker** - Containerize and deploy anywhere

### Frontend (React)
Options:
- **Vercel** - Auto-deploy on git push
- **Netlify** - Connect GitHub repo
- **GitHub Pages** - `npm run build` + push to gh-pages branch
- **Same server as backend** - Serve static files with FastAPI

### Production Setup
1. Update `frontend/.env` with production API URL
2. Build frontend: `npm run build`
3. Set `DATABASE_URL` to PostgreSQL connection string
4. Deploy both backend and frontend

## Troubleshooting

**Articles not loading?**
- Check backend is running: `curl http://localhost:8000/health`
- Check browser console for errors (F12)
- Verify CORS is enabled in FastAPI

**RSS feeds not updating?**
- Check backend logs for feed errors
- Verify RSS feed URLs are still valid
- Manually trigger refresh: `POST /api/refresh`

**CORS errors?**
- Ensure `proxy` in `frontend/package.json` points to correct backend URL
- Or update `frontend/.env` REACT_APP_API_URL

## Future Enhancements

- User accounts & saved preferences
- Email notifications for breaking news
- Full-text search across articles
- Article tagging & categorization
- Social media sharing
- Dark mode toggle
- Advanced filtering (date range, keyword search)
- Caching with Redis
- Real-time updates with WebSockets

## License

MIT License - feel free to use and modify for your own projects

## Support

If you encounter issues:
1. Check the troubleshooting section
2. Review backend logs: `uvicorn main:app --reload`
3. Check browser console (F12)
4. Verify all services are running
