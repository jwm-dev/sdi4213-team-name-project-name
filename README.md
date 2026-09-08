# Fuel Inventory Management System

**Team:** name · **Course:** SDI 4213/5213 — DevOps

## Project Description

An inventory management system to coordinate the management of fuel stocks
across a distributed company. The system tracks fuel stock records (fuel type,
quantity, capacity) per site and exposes them through a documented REST API
with full CRUD operations.

## Team Members

| Member | GitHub | Initial Role |
|---|---|---|
| Jeffrey W. Gregory | [@jwm-dev](https://github.com/jwm-dev) | Code & Architecture Lead |
| Vance Reed | [@virtualvance](https://github.com/virtualvance) | Project Management & Domain SME |
| Ryan Kendrick | [@rmkoupi](https://github.com/rmkoupi) | Team Morale & Support |

Everyone writes application code; the role marks who is accountable for that
axis of the project.

## Planned Technology Stack

- **Programming language:** Python 3.12
- **Framework:** FastAPI
- **Database:** SQLite (migrating to PostgreSQL at containerization)
- **Testing framework:** pytest
- **CI/CD platform:** GitHub Actions
- **Deployment target:** Docker container on Render or Fly.io (free tier)

## Project Goals

- Deliver a working fuel inventory API with full CRUD on fuel stock records by midterm.
- Maintain an automated pytest suite that runs on every pull request.
- Establish a CI/CD pipeline in GitHub Actions that tests and builds on every push to main.
- Containerize the application and deploy it to a live public environment.
- Practice a consistent branch-and-pull-request workflow across all team members.

## Current Status

- **Week 1:** Project setup and charter — README, charter, folder structure,
  and initial issues in place.
- **Week 2:** Branch-and-PR workflow established; `docs/team-workflow.md`.
- **Week 3:** FastAPI skeleton with `/health` and `/fuelstocks` endpoints, pytest suite, local run instructions.

## Team Workflow

Our team workflow is documented in [docs/team-workflow.md](docs/team-workflow.md).

## Running Locally

Requires Python 3.12+.

```bash
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

Then open http://localhost:8000/docs for the interactive API documentation.
Binding to `0.0.0.0` makes the API reachable from other machines on your
network (and later from inside a container); use `--host 127.0.0.1` to keep it
local only.

Endpoints so far:

| Method | Path | Purpose |
|---|---|---|
| GET | `/health` | Liveness check, returns `{"status": "ok"}` |
| GET | `/fuelstocks` | List fuel stock records |
| POST | `/fuelstocks` | Create a record (`site_id`, `fuel_type`, `quantity_gallons`, `capacity_gallons`) |
| GET | `/fuelstocks/{id}` | Fetch one record |

Storage is in-memory for now; SQLite arrives in a later milestone.

## Running the Tests

Tests are tiered by what sits on the other end of the call:

| Level | What it exercises | Command |
|---|---|---|
| L0 | In-process: model rules and routes via FastAPI's `TestClient`, no socket, no I/O | `pytest` (default) |
| L1 | Needs a real dependency (database); arrives with SQLite | `pytest -m l1` |
| L2 | Real HTTP against a uvicorn process the fixture starts on a free port | `pytest -m l2` |
| L3 | The L2 suite pointed at an already-running or deployed instance | `BASE_URL=http://host:8000 pytest -m l2` |

Unmarked tests are L0. `scripts/smoke.sh` is a shell version of L2 for a
quick manual check: it starts the server on `0.0.0.0`, hits it with `curl`,
and stops it.
