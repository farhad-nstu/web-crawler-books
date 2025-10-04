# Books Scraper API

A FastAPI-based API for scraping, storing, and tracking books.  
Includes Celery worker and beat for scheduled crawling, MongoDB for storage, and Redis as Celery broker.

---

## Features

- FastAPI REST API for books and change logs
- MongoDB storage
- Celery worker for background tasks
- Celery beat for scheduled crawling
- API Key authentication
- Swagger docs with API Key support
- Dockerized setup

## Docker Setup

- This project uses Docker Compose to run all services:
- API: FastAPI server (http://localhost:8000)
- Worker: Celery worker
- Beat: Celery scheduler
- MongoDB: Database (localhost:27018)
- Redis: Broker/cache (localhost:6380)

## Stop any old containers and remove orphans
- docker compose down --remove-orphans

## Build and start all services in detached mode
- docker compose up --build -d

## Check running containers
- docker compose ps

## Testing with Postman

We provide both a **Postman collection** and a **Postman environment**:

- `postman_collection.json`
- `postman_environment.json`

### Steps
1. Open Postman → Import both files.
2. Select environment **Books Scraper Local**.
3. Run requests directly:
   - GET `{{BASE_URL}}/api/books`
   - GET `{{BASE_URL}}/api/books/{book_id}`
   - GET `{{BASE_URL}}/api/changes`

N.B: No need to type API keys — everything is pre-configured.
