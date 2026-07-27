# Sprint 2 — Retrospective

## What went well

- Pinning the Python version and adding lint to CI *before* writing new
  feature code (the Sprint 1 retro action items) worked exactly as
  intended: zero environment setup issues in Sprint 2, and every commit
  from `chore: apply Sprint 1 retro...` onward was covered by both lint
  and tests in CI, not just tests added after the fact.
- Having the storage layer (`app/storage.py`) already support update/
  delete/filter from Sprint 1's scaffold meant Sprint 2 stories were pure
  API-layer additions — no rework of the data layer was needed.
- Test-driving each endpoint against the acceptance criteria written in
  Sprint 0 continued to remove ambiguity about scope for each story.

## What didn't go well

- Testing the global exception handler (US8) surfaced a non-obvious
  behavior: FastAPI's `TestClient` re-raises unhandled exceptions by
  default (`raise_server_exceptions=True`) even when an `Exception`
  handler is registered, so the "logged + returns 500" test needed a
  second `TestClient` instance with that flag disabled. This cost debugging
  time that a quick framework-behavior check up front would have avoided.
- Monitoring is still "basic" as scoped — logs go to console only, with no
  aggregation, retention, or alerting. That's appropriate for this
  prototype's scope, but worth naming explicitly rather than implying more
  maturity than exists.

## Lessons learned (across both sprints)

1. **Writing acceptance criteria before code consistently paid off** — in
   both sprints, tests were a near-direct translation of the Given/When/Then
   criteria, which kept "done" unambiguous and reduced back-and-forth on
   scope.
2. **Fixing process gaps immediately (same sprint) beats deferring them** —
   the Sprint 1 retro items were applied at the very start of Sprint 2
   rather than "eventually," which is why they measurably paid off within
   the same sprint instead of the next one.
3. **One story per commit** made the two-sprint history genuinely easy to
   review story-by-story — this is worth carrying into any future work
   past this assessment.

## If this project continued (not in scope for this assessment)

- Swap in-memory storage for a persistent store — the current `TaskStore`
  interface was written narrow enough to swap without touching the API
  layer.
- Add structured (JSON) logging and an external error tracker instead of
  console-only logging, once there's a real deployment target to send
  telemetry to.
