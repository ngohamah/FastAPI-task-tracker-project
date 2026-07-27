# Sprint 1 — Retrospective

## What went well

- Breaking the sprint into one story per commit (scaffold → US1 → US2 →
  US3 → CI) kept the history readable and each commit independently
  testable — no "big bang" commit.
- Writing acceptance criteria in Sprint 0 before coding meant there was no
  ambiguity about what "done" meant for each endpoint; tests were written
  directly from those criteria.
- The in-memory storage decision kept Sprint 1 scoped to the API surface
  instead of getting pulled into database setup.

## What didn't go well

- Local dev environment setup cost real time: the default `python3`
  resolved to Python 3.14, which doesn't yet have prebuilt wheels for
  `pydantic-core`, so the first dependency install failed and had to be
  redone against Python 3.12. This wasn't planned for and wasn't caught
  until implementation had already started.
- CI was added *after* all three stories were already implemented and
  manually tested, rather than at the very start of the sprint — so for
  most of Sprint 1 there was no automated verification catching
  regressions between commits.
- No linting/formatting check exists yet, so style consistency is only as
  good as manual discipline.

## Improvements for Sprint 2

1. **Pin the Python version explicitly** (document it in the README and
   match it in CI) so environment setup is reproducible and doesn't repeat
   the Sprint 1 friction.
2. **Set up CI before writing the first Sprint 2 feature**, not after —
   every Sprint 2 commit should be covered by automated tests from the
   start, not retrofitted at the end.
3. **Add a lint step to CI** (`ruff`) so style/consistency issues are
   caught automatically instead of relying on manual review.
