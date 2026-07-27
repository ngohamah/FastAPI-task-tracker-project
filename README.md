# Task Tracker API

A lightweight Task Tracker API that lets a user create, update, and monitor
the status of their tasks through a simple, well-tested REST interface.

Built as an Agile/DevOps practice exercise: see [docs/](docs/) for the
backlog, sprint plans, sprint reviews, and retrospectives.

## Requirements

- Python **3.12** (see `.python-version` — newer Python versions may not
  have prebuilt wheels for this project's pinned dependencies yet)

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Interactive docs (Swagger UI): http://127.0.0.1:8000/docs

## Run tests

```bash
pytest tests/ -v
```

## Lint

```bash
ruff check .
```
