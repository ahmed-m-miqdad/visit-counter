# Visit Counter 🐳

A containerized web application that tracks page visits in real time.  
Built to practice Docker fundamentals and multi-container orchestration with Docker Compose.

## Tech Stack

- **Python** + **Flask** — web server
- **Redis** — in-memory visit counter
- **Docker** + **Docker Compose** — containerization and orchestration

## Project Structure

\```
.
├── app.py               # Flask application
├── requirements.txt     # Python dependencies
├── Dockerfile           # Image build instructions
├── docker-compose.yml   # Multi-container setup
└── .dockerignore        # Excludes unnecessary files from image
\```

## Getting Started

Make sure you have [Docker](https://www.docker.com/) installed, then:

\```bash
git clone https://github.com/YOUR_USERNAME/visit-counter.git
cd visit-counter
docker compose up
\```

Open [http://localhost:5000](http://localhost:5000) and refresh — the counter increments on every visit.

To stop:

\```bash
docker compose down
\```

## What This Covers

- Writing a Dockerfile from scratch
- Layer caching optimization
- Multi-container apps with Docker Compose
- Container networking via service name resolution
- Keeping images minimal with `.dockerignore`

## Author

**Your Name** — [GitHub](https://github.com/YOUR_USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR_USERNAME)