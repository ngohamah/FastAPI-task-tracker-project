# Product Backlog — Task Tracker API

## Product Vision

A lightweight Task Tracker API that lets a user create, update, and monitor
the status of their tasks through a simple, well-tested REST interface —
built to demonstrate disciplined Agile planning and DevOps practice, not
feature volume.

## Definition of Done (DoD)

A backlog item is "Done" only when **all** of the following are true:

- [ ] Code implements the story's acceptance criteria
- [ ] Unit/integration tests exist for the new behavior and pass locally
- [ ] Code is committed with a clear, scoped commit message (no bundling
      unrelated changes)
- [ ] CI pipeline runs and passes on the commit (from Sprint 1 onward)
- [ ] Endpoint is manually smoke-tested (via `/docs` Swagger UI or curl)
- [ ] No known critical bugs or unhandled errors for the happy path
- [ ] Relevant docs (README/backlog status) updated

## Backlog

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

Estimation method: relative sizing using Fibonacci-like story points
(1, 2, 3, 5, 8), based on implementation + test effort.

## Acceptance Criteria (Given/When/Then)

**US1 — Create task**
- Given valid `title` and `description`, when POST `/tasks` is called, then a
  task is created with `id`, `status="pending"`, and a 201 response returns
  the new task.
- Given a missing/empty `title`, when POST `/tasks` is called, then the API
  returns a 422 validation error.

**US2 — List tasks**
- Given tasks exist, when GET `/tasks` is called, then a 200 response
  returns a JSON array of all tasks.
- Given no tasks exist, when GET `/tasks` is called, then a 200 response
  returns an empty array (not an error).

**US3 — Get task by ID**
- Given a task with a known ID exists, when GET `/tasks/{id}` is called,
  then a 200 response returns that task.
- Given no task with that ID exists, when GET `/tasks/{id}` is called, then
  a 404 response is returned.

**US4 — Update task**
- Given a task exists, when PATCH `/tasks/{id}` is called with any subset of
  `title`/`description`/`status`, then only those fields are updated and the
  updated task is returned with 200.
- Given no task with that ID exists, when PATCH `/tasks/{id}` is called,
  then a 404 response is returned.

**US5 — Delete task**
- Given a task exists, when DELETE `/tasks/{id}` is called, then the task is
  removed and a 204 response is returned.
- Given no task with that ID exists, when DELETE `/tasks/{id}` is called,
  then a 404 response is returned.

**US6 — Filter by status**
- Given tasks with mixed statuses exist, when GET `/tasks?status=done` is
  called, then only tasks with `status="done"` are returned.

**US7 — Health endpoint**
- Given the service is running, when GET `/health` is called, then a 200
  response returns `{"status": "ok"}`.

**US8 — Logging**
- Given any request is handled, when the request completes, then a log line
  is written to the console with method, path, and status code.
- Given an unhandled exception occurs, when it is raised, then it is logged
  with a stack trace before a 500 response is returned.
