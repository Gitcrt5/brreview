**BRReview Specifications**

**Version:** 1.1  
**Date:** 2025-03-28  
**Project:** BRReview (Bridge Results Review)

---

### ✨ Overview
BRReview is a project designed to automate the scraping, analysis, and structured review of session results from the publicly available Newcastle Bridge Club results website. It supports both historical data ingestion and ongoing monitoring of new sessions. The system is designed for deployment via Docker on a Synology NAS and is structured for future cloud or cross-platform expansion.

---

### 🔢 Current Requirements

#### ✅ Functional Requirements
- Scrape all bridge session data from the Newcastle Bridge Club results site from 2020 to the present.
- Store each session's metadata (date, name, ID) in a structured database.
- Track individual players and partnerships across multiple sessions.
- Detect new results by comparing scraped session IDs against stored values.
- Allow reprocessing by providing a reset mechanism that clears and recreates the database.
- Track full player details, board numbers, results, and scores.
- Include structured support for:
  - Bidding sequences per partnership per board
  - Free-text comments on bidding and hand play
- Use SQLAlchemy ORM with SQLite (default) and PostgreSQL (optional future backend).
- Operate inside a Docker container running on Synology NAS.
- Source code and config maintained in GitHub.

#### 🛠️ Technical Setup
- Written in Python 3.10+
- Dockerized environment with Dockerfile and docker-compose
- `requests` + `BeautifulSoup` for web scraping
- SQLAlchemy for ORM
- `python-dotenv` for config management
- SQLite for default database

#### 📃 Deployment
- Primary deployment: Docker container on Synology DS918+
- Database path: `/app/data/brreview.db` mounted to Synology volume

---

### 🔄 Current Enhancements in Development

#### 🔢 Database
- `reset_db.py`: Drops and recreates all tables using SQLAlchemy
- `scrape_historical.py`: Scrapes all session headers from 2020 to current year

#### 🗐 Session Detection
- System will scrape the current results page and compare session IDs to those in the DB
- New sessions will be flagged and processed

#### 🌐 Docker Behavior
- Updated `.env` config places SQLite DB in bind-mounted `data/` directory
- Container CMD is being refactored to avoid continuous restarting

---

### ⚡ Proposed Enhancements (Adopted)
- Add structured bidding capture for each partnership per board
- Add free-text fields for bidding commentary and general hand commentary
- Support export of LIN files (deferred until explicitly requested)
- Track and compare performance across different partners

---

### 🔍 Proposed Enhancements (Pending)
- Interactive charts and dashboards (e.g., via Plotly, Dash, or similar)
- Cloud deployment variant (e.g., GitHub Actions or lightweight cloud container)
- Scraping and storing full session board data and scores
- Summary report generation for new sessions (email or document)
- Web interface for browsing and filtering results
- Configurable alerting/notifications for new results
- **User roles and access control for future feedback/commenting capabilities (e.g., teachers or reviewers giving input on hands and bidding)**

---

### 🔄 Project Workflow (Current Stage)
1. Define and confirm technology stack
2. Create database schema and initial setup (complete)
3. Deploy container on Synology and validate DB creation (complete)
4. Scrape session headers for historical data (in progress)
5. Implement session monitoring and detection (next)
6. Expand scraping to full session details (future)

---

### 📓 Maintainer Notes
- All environment variables and sensitive settings should reside in `.env`, never committed
- `.env.example` to be created and committed to GitHub for reference
- Use `reset_db.py` for test resets and `scrape_historical.py` for initial load
- All code changes should be committed with appropriate structure and comments

---

**End of Specification v1.1**

