# Contributing

How team "name" works on this repository.

## Branching strategy

We use short-lived feature branches off `main` (GitHub Flow):

- `main` is always the current, working state of the project. No direct
  commits to `main`.
- Branch from `main` for each piece of work, named
  `<topic>-<short-description>`, e.g. `feature-fuelstock-model`,
  `fix-quantity-validation`, `docs-runbook`.
- Keep branches small and focused — one issue per branch where possible.
- Delete the branch after its PR merges.

## Issues first

- Every piece of work starts as a GitHub Issue with a 1–2 sentence
  description, an assignee, and a label, and goes on the project board.
- Reference the issue from your PR (`Closes #N`) so it closes on merge and
  the board stays current.

## Pull requests

- Open a PR from your feature branch into `main`; fill in the PR template.
- At least **one other team member** reviews and approves before merge.
- Once CI exists, checks must pass before merge.
- Prefer "Squash and merge" to keep `main` history readable.

## Commit messages

- Imperative mood, concise subject line ("Add FuelStock model", not
  "Added stuff").
- Explain *why* in the body when it isn't obvious.
- Per course policy, AI use is documented in our reports and submissions,
  not in individual commit messages.

## Code standards

- Python 3.12, FastAPI, tests in `tests/` with pytest.
- New features come with tests; bug fixes come with a regression test.
