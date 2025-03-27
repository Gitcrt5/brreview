# Bridge Results Automation

Version: 1.1  
Date: 2025-03-27

## 📌 Project Overview

This project automates the collection, analysis, and tracking of bridge game results from the Newcastle Bridge Club public website.

### Key Features
- Scrapes historical and new results (2020–present)
- Tracks all player, partnership, and board-level data
- Generates structured summary documents for analysis
- Supports future export to LIN files and interactive dashboards
- Includes structured bidding entry and commentary fields

## 🏗️ Project Structure

```
bridge-results-automation/
│
├── data/                  # Local database or result files
├── src/                   # Source code for scraper, parser, and generator
│   ├── scraper/           # HTML scraping modules
│   ├── parser/            # PBN parser, HTML extractors
│   ├── db/                # DB models and initialization
│   └── reports/           # Summary generation logic
│
├── tests/                 # Unit tests and validation scripts
├── .env                   # Environment variables (e.g. DB paths, user name)
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## ⚙️ Technologies Used

- Python 3.10+
- SQLite (or PostgreSQL)
- BeautifulSoup4, Requests
- SQLAlchemy (optional ORM)
- Docker (for deployment on Synology)
- cron (for scheduling automation)

## 🚀 Getting Started

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the `.env` file with your configuration
4. Run the initial setup script to create the database
5. Begin by importing historical data

## 🔜 Planned Features

- LIN export (deferred)
- Interactive analytics and dashboards
- Google Docs or email summaries
- Web interface for review and filtering

## 📝 License

MIT License
