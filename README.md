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
| Jeffrey W. Gregory | [@jwm-dev](https://github.com/jwm-dev) | Repo & Release Manager |
| Vance Reed | [@virtualvance](https://github.com/virtualvance) | QA & Test Lead |
| Ryan Kendrick | [@rmkoupi](https://github.com/rmkoupi) | Infrastructure & CI/CD Lead |

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
