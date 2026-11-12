# Python Microservices Platform

A cleanly separated FastAPI backend example with customer create/read endpoints, Pydantic
validation, repository abstraction, health endpoint, tests, and CI.

## Run
```bash
pip install -e ".[dev]"
uvicorn backend_api.api:app --reload --app-dir src
pytest -q
```
API docs: `http://localhost:8000/docs`.

## Current implementation
The sample uses an in-memory repository. It demonstrates API and service boundaries, not a
complete distributed microservices deployment.

## Roadmap
PostgreSQL + SQLAlchemy, Alembic migrations, Redis caching, JWT/OAuth2 authentication,
service-to-service communication, OpenTelemetry, structured logs, contract tests, and
Docker Compose deployment.
