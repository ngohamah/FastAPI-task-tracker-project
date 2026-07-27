# Final Assessment — Agile & DevOps in Practice

**Project:** Task Tracker API
**Repository:** https://github.com/ngohamah/agile-practices-lab-project
**Author:** Rodney (ngoh.amah@amalitechtraining.org)
**Date:** 27 July 2026

---

## 1. Executive Summary

This report documents the individual delivery of a small working
prototype — a Task Tracker REST API — across two simulated Agile sprints,
following the practices and deliverables specified in the assessment
brief. All 8 backlog items were delivered, tested, and shipped through a
working CI pipeline, with basic monitoring/logging added in Sprint 2 as
required.

| Metric | Result |
|--------|--------|
| Backlog items delivered | 8 / 8 (brief required ≥ 2 per sprint) |
| Total commits | 18 (one story/concern per commit — no big-bang commits) |
| Automated tests | 17, all passing |
| CI pipeline | GitHub Actions — green on every pushed commit |
| Lint | `ruff check .` — zero issues |

---

## 2. Product Vision

> A lightweight Task Tracker API that lets a user create, update, and
> monitor the status of their tasks through a simple, well-tested REST
> interface — built to demonstrate disciplined Agile planning and DevOps
> practice, not feature volume.

---

## 3. Sprint 0 — Planning

### 3.1 Product Backlog

| # | User Story | Points | Priority | Sprint |
|---|------------|--------|----------|--------|
| US1 | As a user, I want to create a task with a title and description so that I can track work I need to do. | 3 | High | 1 |
| US2 | As a user, I want to view a list of all my tasks so that I can see everything outstanding. | 2 | High | 1 |
| US3 | As a user, I want to view a single task by its ID so that I can check its details. | 2 | High | 1 |
| US4 | As a user, I want to update a task's title, description, or status so that I can keep it current. | 3 | High | 2 |
| US5 | As a user, I want to delete a task so that I can remove things I no longer need. | 2 | Medium | 2 |
| US6 | As a user, I want to filter tasks by status (pending/done) so that I can focus on what's left. | 3 | Medium | 2 |
| US7 | As an operator, I want a health-check endpoint so that I can monitor whether the service is running. | 1 | Medium | 2 |
| US8 | As an operator, I want request and error logging so that I can diagnose issues without a debugger. | 2 | Low | 2 |

**Estimation method:** relative sizing using Fibonacci-like story points
(1, 2, 3, 5, 8), based on implementation + test effort.

### 3.2 Definition of Done (DoD)

A backlog item is "Done" only when **all** of the following are true:

1. Code implements the story's acceptance criteria
2. Unit/integration tests exist for the new behavior and pass locally
3. Code is committed with a clear, scoped commit message (no bundling
   unrelated changes)
4. CI pipeline runs and passes on the commit (from Sprint 1 onward)
5. Endpoint is manually smoke-tested (via `/docs` Swagger UI or curl)
6. No known critical bugs or unhandled errors for the happy path
7. Relevant docs (README/backlog status) updated

### 3.3 Acceptance Criteria (Given/When/Then)

**US1 — Create task**
- Given valid `title` and `description`, when `POST /tasks` is called,
  then a task is created with `id`, `status="pending"`, and a 201
  response returns the new task.
- Given a missing/empty `title`, when `POST /tasks` is called, then the
  API returns a 422 validation error.

**US2 — List tasks**
- Given tasks exist, when `GET /tasks` is called, then a 200 response
  returns a JSON array of all tasks.
- Given no tasks exist, when `GET /tasks` is called, then a 200 response
  returns an empty array (not an error).

**US3 — Get task by ID**
- Given a task with a known ID exists, when `GET /tasks/{id}` is called,
  then a 200 response returns that task.
- Given no task with that ID exists, when `GET /tasks/{id}` is called,
  then a 404 response is returned.

**US4 — Update task**
- Given a task exists, when `PATCH /tasks/{id}` is called with any subset
  of `title`/`description`/`status`, then only those fields are updated
  and the updated task is returned with 200.
- Given no task with that ID exists, when `PATCH /tasks/{id}` is called,
  then a 404 response is returned.

**US5 — Delete task**
- Given a task exists, when `DELETE /tasks/{id}` is called, then the task
  is removed and a 204 response is returned.
- Given no task with that ID exists, when `DELETE /tasks/{id}` is called,
  then a 404 response is returned.

**US6 — Filter by status**
- Given tasks with mixed statuses exist, when `GET /tasks?status=done` is
  called, then only tasks with `status="done"` are returned.

**US7 — Health endpoint**
- Given the service is running, when `GET /health` is called, then a 200
  response returns `{"status": "ok"}`.

**US8 — Logging**
- Given any request is handled, when the request completes, then a log
  line is written with method, path, and status code.
- Given an unhandled exception occurs, when it is raised, then it is
  logged with a stack trace before a 500 response is returned.

### 3.4 Sprint 1 Plan

**Sprint Goal:** Stand up the core read/write task API with tests and CI,
so there is a demoable, testable slice of the product by the end of the
sprint.

**Selected stories:** US1, US2, US3 (7 points capacity).

**Deferred to Sprint 2:** update, delete, filtering, health endpoint,
logging — these depend on the create/read path existing first and are
lower priority per the backlog.

---

## 4. Sprint 1 — Execution

### 4.1 Delivered

| Story | Status | Evidence |
|-------|--------|----------|
| US1 — Create task | Done | `POST /tasks` — tested in `tests/test_create_task.py` |
| US2 — List tasks | Done | `GET /tasks` — tested in `tests/test_list_tasks.py` |
| US3 — Get task by ID | Done | `GET /tasks/{id}` — tested in `tests/test_get_task.py` |

All acceptance criteria for US1–US3 were met: validation on empty title
(422), empty-list handling (200 + `[]`), and 404 on unknown ID.

### 4.2 CI/CD Pipeline

A GitHub Actions workflow (`.github/workflows/ci.yml`) was added, running
on every push/PR: installs dependencies, then runs the test suite. It has
passed on every commit since its introduction.

### 4.3 Testing Evidence

6/6 tests passing locally and in CI at the end of Sprint 1.

### 4.4 Sprint Review

Demoed via `uvicorn app.main:app --reload` and the `/docs` Swagger UI, and
via curl:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy milk", "description": "2%"}'

curl http://127.0.0.1:8000/tasks
```

### 4.5 Sprint 1 Retrospective

**What went well**
- One story per commit (scaffold → US1 → US2 → US3 → CI) kept history
  readable and each commit independently testable — no "big bang" commit.
- Writing acceptance criteria in Sprint 0 before coding removed ambiguity
  about "done"; tests were a direct translation of those criteria.
- The in-memory storage decision kept Sprint 1 scoped to the API surface
  instead of getting pulled into database setup.

**What didn't go well**
- Local environment setup cost real time: the default `python3` resolved
  to Python 3.14, which didn't yet have prebuilt wheels for
  `pydantic-core`, so the first dependency install failed and had to be
  redone against Python 3.12.
- CI was added *after* all three stories were already implemented and
  manually tested, rather than at the start of the sprint — so most of
  Sprint 1 had no automated regression coverage between commits.
- No linting/formatting check existed yet.

**Improvements identified for Sprint 2**
1. Pin the Python version explicitly (README + `.python-version`).
2. Set up CI *before* writing the first Sprint 2 feature, not after.
3. Add a lint step (`ruff`) to CI.

---

## 5. Sprint 2 — Execution & Improvement

### 5.1 Retro Improvements Applied First

Before any new feature code was written, the Sprint 1 retro actions were
carried out: `.python-version` pinned to 3.12, a README documenting setup,
and `ruff` wired into CI — all committed in
`chore: apply Sprint 1 retro - pin Python version, add ruff lint to CI, add README`,
ahead of any Sprint 2 story work.

### 5.2 Delivered

| Story | Status | Evidence |
|-------|--------|----------|
| US4 — Update task | Done | `PATCH /tasks/{id}` — tested in `tests/test_update_task.py` |
| US5 — Delete task | Done | `DELETE /tasks/{id}` — tested in `tests/test_delete_task.py` |
| US6 — Filter by status | Done | `GET /tasks?status=` — tested in `tests/test_filter_tasks.py` |
| US7 — Health endpoint | Done | `GET /health` — tested in `tests/test_health.py` |
| US8 — Logging | Done | request logging middleware + global exception handler — tested in `tests/test_logging.py` |

5 additional backlog items delivered (brief required ≥ 2), for 8/8
backlog items complete across both sprints.

### 5.3 Monitoring & Logging (DevOps requirement)

- `GET /health` returns `{"status": "ok"}` for uptime monitoring.
- A request-logging middleware logs method, path, and status code for
  every request.
- A global exception handler logs unhandled errors with a stack trace
  before returning a 500 response.
- Logs are written to both the console and a persisted `app.log` file
  (added as a follow-up improvement after Sprint 2 — see Section 7).

### 5.4 Testing & CI Evidence

- 15/15 tests passing at Sprint 2 close (17/17 after the post-Sprint-2
  additions in Section 7).
- `ruff check .` passes with zero issues.
- GitHub Actions green on every Sprint 2 commit.

### 5.5 Sprint Review

```bash
curl http://127.0.0.1:8000/health
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

### 5.6 Sprint 2 Retrospective

**What went well**
- Pinning the Python version and adding lint to CI *before* new feature
  code worked exactly as intended: zero environment issues in Sprint 2,
  and every commit was covered by lint and tests from the start.
- The storage layer built in Sprint 1 already supported update/delete/
  filter, so Sprint 2 stories were pure API-layer additions.
- Test-driving each endpoint against Sprint 0's acceptance criteria
  continued to remove scope ambiguity.

**What didn't go well**
- Testing the global exception handler (US8) surfaced a non-obvious
  FastAPI `TestClient` behavior (it re-raises unhandled exceptions by
  default even with a registered handler), costing some debugging time.
- Monitoring remained "basic" as scoped — console/file logs only, no
  aggregation, retention, or alerting. Appropriate for this prototype's
  scope, but worth naming explicitly.

**Lessons learned (across both sprints)**
1. Writing acceptance criteria before code consistently paid off — tests
   were a near-direct translation of Given/When/Then criteria.
2. Fixing process gaps immediately (same sprint) beats deferring them —
   the Sprint 1 retro actions paid off within Sprint 2 itself.
3. One story per commit made the two-sprint history genuinely easy to
   review story-by-story.

**If this project continued (beyond assessment scope)**
- Swap in-memory storage for a persistent store — the `TaskStore`
  interface was written narrow enough to swap without touching the API
  layer.
- Add structured (JSON) logging and an external error tracker once
  there's a real deployment target to send telemetry to.

---

## 6. Deliverables Mapping

| Brief requirement | Where it lives |
|---|---|
| Backlog & Sprint Plans | `docs/backlog.md`, `docs/sprint0-planning.md`, `docs/sprint2-planning.md` |
| Codebase, incremental commits | `app/`, `tests/` — 18 scoped commits |
| CI/CD Evidence | `.github/workflows/ci.yml`; GitHub Actions run history |
| Testing Evidence | `tests/` (17 tests); CI logs |
| Sprint Review Documents | `docs/sprint1-review.md`, `docs/sprint2-review.md` |
| Retrospectives | `docs/sprint1-retro.md`, `docs/sprint2-retro.md` |

---

## 7. Additional Improvements (Post-Sprint 2)

Two small enhancements were made after Sprint 2 closed, continuing the
same one-concern-per-commit discipline:

1. **Root path redirect** (`chore: redirect root path to /docs...`) — `GET /`
   now redirects to the Swagger UI instead of returning a 404, improving
   the demo experience.
2. **Persisted file logging** (`feat: add FileHandler so logs persist to
   app.log...`) — logs now write to both console and a gitignored
   `app.log` file, extending the US8 logging behavior.

Both changes shipped with their own tests and passed CI before merging,
bringing the total to 17 passing tests and 18 commits.

---

## 8. Evaluation Criteria Self-Check

| Dimension | Weight | Self-assessment |
|-----------|--------|------------------|
| Agile Practice | 25% | Backlog with 8 stories, story-point estimates, Given/When/Then acceptance criteria, explicit DoD, and two sprint plans with clear goals and capacity. |
| DevOps Practice | 25% | GitHub Actions CI (test + lint) green on every commit; console + file logging; `/health` endpoint for monitoring. |
| Delivery Discipline | 20% | 18 commits, one story/concern each — no big-bang commits; full history in Section 6. |
| Prototype Quality | 20% | All 8 backlog items implemented and meeting their acceptance criteria; 17/17 tests passing. |
| Reflection | 10% | Two retrospectives; Sprint 1's 3 improvements were concretely applied and validated at the start of Sprint 2 (Section 5.1, 5.6). |

---

## Appendix — Full Commit History

```
docs: Sprint 0 planning - product vision, backlog, DoD, Sprint 1 plan
chore: scaffold FastAPI project structure and in-memory storage layer
feat: implement US1 create task endpoint with tests
feat: implement US2 list tasks endpoint with tests
feat: implement US3 get task by id endpoint with tests
ci: add GitHub Actions pipeline to run tests on push and PR
docs: Sprint 1 review and retrospective
chore: apply Sprint 1 retro - pin Python version, add ruff lint to CI, add README
docs: Sprint 2 planning
feat: implement US4 update task endpoint with tests
feat: implement US5 delete task endpoint with tests
feat: implement US6 filter tasks by status with tests
feat: implement US7 health check endpoint with tests
feat: implement US8 request/error logging with tests
docs: Sprint 2 review and retrospective
chore: redirect root path to /docs for a friendlier demo experience
feat: add FileHandler so logs persist to app.log alongside console output
```
