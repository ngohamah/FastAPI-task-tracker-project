# Sprint 1 — Review

## Sprint Goal (recap)

Stand up the core read/write task API with tests and CI, so there is a
demoable, testable slice of the product by the end of the sprint.

## Delivered

| Story | Status | Evidence |
|-------|--------|----------|
| US1 — Create task | Done | `POST /tasks` — `app/main.py`, tested in `tests/test_create_task.py` |
| US2 — List tasks | Done | `GET /tasks` — `app/main.py`, tested in `tests/test_list_tasks.py` |
| US3 — Get task by ID | Done | `GET /tasks/{id}` — `app/main.py`, tested in `tests/test_get_task.py` |

All acceptance criteria from [backlog.md](backlog.md) for US1–US3 are met:
validation on empty title (422), empty-list handling (200 + `[]`), and
404 on unknown ID.

## Demo

Run locally:

```bash
uvicorn app.main:app --reload
```

Then visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI, or:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk", "description": "2%"}'

curl http://127.0.0.1:8000/tasks
```

## Test & CI evidence

- 6/6 tests passing locally (`pytest tests/ -v`)
- GitHub Actions workflow (`.github/workflows/ci.yml`) runs the same suite
  on every push/PR — see the Actions tab on the repo for the run log.

## Definition of Done check

All three delivered stories meet every DoD item in
[backlog.md](backlog.md): implemented against acceptance criteria, tested,
committed as scoped commits, CI green, manually smoke-tested, no known
critical bugs.
