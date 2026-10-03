# Project Charter — Fuel Inventory Management System

**Team:** name
**Members:** Jeffrey W. Gregory (@jwm-dev) · Vance Reed (@virtualvance) · Ryan Kendrick (@rmkoupi)
**Course:** SDI 4213/5213 — DevOps
**Date:** 2026-09-03
**Repository:** https://github.com/jwm-dev/sdi4213-team-name-project-name

## Purpose

Distributed companies that store fuel at multiple sites need a single view of
what fuel is where. This project builds a fuel inventory management system: a
REST API that tracks fuel stock records across company sites, built and
operated with DevOps practices (version control workflow, automated testing,
CI/CD, containerized deployment).

## Objectives

1. Deliver a working fuel inventory API with full CRUD on the main data
   object by midterm.
2. Maintain an automated pytest suite that runs on every pull request.
3. Establish a GitHub Actions pipeline that tests and builds on every push to
   `main`.
4. Containerize the application and deploy it to a live public environment by
   end of semester.
5. Practice a consistent branch-and-pull-request workflow across all team
   members.

## Intended Users

- **Site operators**, who record fuel received and dispensed at their site.
- **Inventory managers**, who need current stock levels and capacity headroom
  across all sites to plan reorders and transfers.
- **Company management / auditors**, who need a trustworthy record of what
  fuel is held where.

## Key Features

1. Create, read, update, and delete fuel stock records (fuel type, quantity,
   capacity, last updated) per site.
2. Manage sites (create/read/update/delete) and list all stock at a site.
3. Interactive, always-current API documentation at `/docs`.
4. Validation guardrails (e.g., quantity cannot exceed capacity; known fuel
   types only).
5. Deployed, publicly reachable instance backed by an automated test-and-build
   pipeline.

## Scope

**In scope**

- CRUD API for fuel stock records and sites, with interactive API
  documentation (FastAPI `/docs`).
- Automated test suite, CI/CD pipeline, Dockerfile, live deployment.
- GitHub Issues + project board for all work tracking.

**Out of scope (initially)**

- Custom frontend beyond the generated API docs.
- Authentication/authorization, delivery scheduling, multi-user accounts.
  These may be revisited after the midterm milestone if time allows.

## Initial Data Model

- **FuelStock** (main object): `id`, `site_id`, `fuel_type`
  (diesel / gasoline / jet-a), `quantity_gallons`, `capacity_gallons`,
  `last_updated`.
- **Site**: `id`, `name`, `location` — gives one relationship to demonstrate
  without expanding scope.

## Technology Stack

Python 3.12 · FastAPI · SQLite (→ PostgreSQL at containerization) · pytest ·
GitHub Actions · Docker on Render or Fly.io free tier.

FastAPI was selected because its type-driven validation, automatic `/docs` interface, async support, and small footprint fit a lightweight REST API well.
SQLite provides a zero-configuration database for early development, while PostgreSQL gives us a production-ready database when the application is containerized and deployed.
pytest integrates cleanly with FastAPI through fixtures and `TestClient`, making API behavior straightforward to test automatically.
GitHub Actions keeps CI alongside the repository, while Docker and a Render or Fly.io free tier give the team a simple path from tested code to a publicly deployed service.

## Team and Roles

| Member | Role | Accountable for |
|---|---|---|
| Jeffrey W. Gregory (@jwm-dev) | Code & Architecture Lead | Application design, code quality, repo administration, merges to `main` |
| Vance Reed (@virtualvance) | Project Management & Domain SME | Planning, project board, fuel/energy domain requirements |
| Ryan Kendrick (@rmkoupi) | Team Morale & Support | Keeping the team unblocked, documentation upkeep, reviews |

Everyone writes application code; roles assign accountability, not exclusive
ownership.

## Ways of Working

- All work is tracked as GitHub Issues with a description, assignee, and
  label, and lives on the project board.
- No direct commits to `main`: feature branches + pull requests, reviewed by
  at least one other member.
- CI must pass before merge once the pipeline exists.

## Milestones

| When | Milestone |
|---|---|
| Week 1 | Repo, README, charter, issues, board, roles |
| Week 2 | Branch/PR workflow established; framework scaffolded |
| Midterm | Full CRUD on FuelStock, tested, CI running |
| End of semester | Containerized, deployed live, final demo |

## Risks and Challenges

| Risk | Impact | How we handle it |
|---|---|---|
| Three-person team with uneven availability week to week | A missed Friday milestone costs 10% per day and is dead after 3 days | Split each week's milestone into issues on Monday; every member owns one branch and one PR per week; reviews answered within two days |
| Work landing directly on `main` or unreviewed merges | Breaks the workflow the course grades and risks shipping broken code | Branch protection on `main` (require one review); the loop in `docs/team-workflow.md` is the only path in |
| SQLite to PostgreSQL migration at containerization | Schema or query differences surface late, during the Docker/Compose weeks | Access the database only through SQLAlchemy from the start; run the test suite against PostgreSQL in Compose before the midterm |
| Free-tier hosting limits (sleep on idle, cold starts, quota) | Live demo or health checks fail at the wrong moment | Keep the app small and stateless; add a `/health` endpoint early; rehearse the demo against the deployed URL, with a local Compose fallback |
| CI/CD supply chain: mutable action tags, secrets in workflows | A poisoned `@v1` tag or leaked token compromises the pipeline | Pin GitHub Actions to a commit SHA, use least-privilege `permissions:` blocks, keep secrets in repository secrets and never in code |
| Scope creep beyond CRUD (auth, scheduling, UI) | Later DevOps milestones (IaC, Kubernetes) get starved of time | Charter scope is the contract; new ideas go to the Backlog column and are revisited only after the midterm checkpoint |

## Success Criteria

The project succeeds if the API is deployed and publicly reachable, CRUD
operations work against the deployed instance, the test suite runs green in
CI on every PR, and the git history shows the branch-and-PR workflow being
followed by all three members.
