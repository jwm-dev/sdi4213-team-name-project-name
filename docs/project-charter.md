# Project Charter — Fuel Inventory Management System

**Team:** name
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

## Team and Roles

| Member | Role | Accountable for |
|---|---|---|
| Jeffrey W. Gregory (@jwm-dev) | Repo & Release Manager | Repo administration, branch protection, releases, merges to `main` |
| Vance Reed (@virtualvance) | QA & Test Lead | Test suite health, coverage of new features, review sign-off |
| Ryan Kendrick (@rmkoupi) | Infrastructure & CI/CD Lead | Actions pipeline, Docker, deployment environment |

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

## Success Criteria

The project succeeds if the API is deployed and publicly reachable, CRUD
operations work against the deployed instance, the test suite runs green in
CI on every PR, and the git history shows the branch-and-PR workflow being
followed by all three members.
