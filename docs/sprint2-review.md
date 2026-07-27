# Sprint 2 — Review

## Sprint Goal (recap)

Complete the task lifecycle (update/delete/filter) and add basic
monitoring/logging, applying the Sprint 1 retrospective improvements.

## Delivered

| Story | Status | Evidence |
|-------|--------|----------|
| US4 — Update task | Done | `PATCH /tasks/{id}` — tested in `tests/test_update_task.py` |
| US5 — Delete task | Done | `DELETE /tasks/{id}` — tested in `tests/test_delete_task.py` |
| US6 — Filter by status | Done | `GET /tasks?status=` — tested in `tests/test_filter_tasks.py` |
| US7 — Health endpoint | Done | `GET /health` — tested in `tests/test_health.py` |
| US8 — Logging | Done | request logging middleware + global exception handler — tested in `tests/test_logging.py` |

That's 5 additional backlog items (brief required ≥2), for 8/8 backlog
items delivered across both sprints.

## Retro improvements applied (from Sprint 1)

- Python version pinned (`.python-version`, README) — no repeat of the
  Sprint 1 environment friction.
- Lint (`ruff`) wired into CI *before* any Sprint 2 feature commit.
- CI covered every Sprint 2 commit from the start (not retrofitted).

## Demo

```bash
uvicorn app.main:app --reload
```

```bash
# monitoring
curl http://127.0.0.1:8000/health

# lifecycle
curl -X POST http://127.0.0.1:8000/tasks -H "Content-Type: application/json" \
  -d '{"title": "Ship report", "description": "Q3 summary"}'
curl -X PATCH http://127.0.0.1:8000/tasks/1 -H "Content-Type: application/json" \
  -d '{"status": "done"}'
curl "http://127.0.0.1:8000/tasks?status=done"
curl -X DELETE http://127.0.0.1:8000/tasks/1 -w "%{http_code}\n"
```

Console output during these calls shows a log line per request
(`GET /health -> 200`, etc.), demonstrating the logging/monitoring in
action.

## Test & CI evidence

- 15/15 tests passing locally and in CI (`pytest tests/ -v`)
- `ruff check .` passes with zero issues
- GitHub Actions green on every Sprint 2 commit — see the Actions tab on
  the repo.

## Definition of Done check

All five delivered stories meet every DoD item in
[backlog.md](backlog.md): acceptance criteria implemented, tests written
and passing, scoped commits, CI green, manually smoke-tested, no known
critical bugs, docs updated.
