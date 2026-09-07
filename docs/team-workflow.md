# Team Workflow

How team **name** uses Git and GitHub for the Fuel Inventory Management
System, for the rest of the semester. Every task follows the same loop:

    Issue -> Branch -> Change -> Commit -> Push -> Pull Request -> Review -> Merge -> Update Board

`main` is the clean, reviewed, working version of the project. Nobody makes
routine changes directly on `main`.

## Branching Strategy

Our team will not make routine project changes directly on the main branch.
Each task will be completed on a separate branch.

Before creating a branch, each team member switches to `main` and pulls the
latest changes:

    git switch main
    git pull
    git switch -c <type>/<short-description>

Branch names use a type prefix and describe the purpose of the work:

- `feature/add-fuelstock-endpoint`
- `docs/update-readme`
- `fix/quantity-validation`
- `test/add-basic-tests`
- `practice/merge-conflict-a`

Keep branches short-lived (a few days at most) and focused on one issue.
Delete the branch on GitHub after its pull request is merged.

## Pull Request Process

Each completed task is submitted using a pull request into `main`.

Before opening a pull request, the team member should:

- confirm they are working on a branch, not `main` (`git branch`)
- have pulled the latest version of `main` before starting the task
- complete the assigned work
- confirm the project still works (once tests exist, run `pytest` locally)
- commit changes with a clear message
- push the branch to GitHub (`git push -u origin <branch>`)
- open a pull request into `main` using the PR template

The pull request must have a clear title, a short description that explains
what changed and why, a `Closes #<issue>` line so the issue closes on merge,
and at least one teammate requested as reviewer. Keep pull requests small; a
40-line PR gets a better review than a 4,000-line one.

## Code Review Expectations

At least one teammate reviews each pull request before it is merged. Authors
do not merge their own pull request before it has been reviewed.

Reviewers should check:

- Does the change match the issue it closes?
- Was the work completed on a branch, not on `main`?
- Is the code or documentation clear?
- Is the pull request focused on one task?
- Are unnecessary files included (editor settings, caches, secrets)?
- Are there obvious errors?
- Are tests needed, and once CI exists, do the checks pass?

Leave specific, constructive comments tied to a line, not just "looks good".
If changes are requested, the author stays on the same branch, makes the
change, commits, and pushes; the pull request updates automatically. After
approval the pull request is merged (Squash and merge preferred), the branch
is deleted, and the issue is moved to Done.

## Commit Message Expectations

Commit messages should be short and specific: start with an imperative verb
(Add, Fix, Update, Remove), keep the summary line under about 50 characters,
and put extra detail in the body when the *why* is not obvious.

Good examples:

- Add project charter
- Update README with team roles
- Create initial app folder
- Fix typo in setup instructions

Weak examples:

- update
- stuff
- final
- fixed things

Per course policy, AI assistance is documented in our reports and
submissions, not in individual commit messages.

## Issue Tracking

The team uses GitHub Issues to track all work. Open an issue *before*
starting work, not after. Each issue should have a clear title, a one- to
two-sentence description, an assignee when possible, and a label
(`documentation`, `enhancement`, `bug`, ...). Every pull request references
its issue.

## Project Board

The team uses the GitHub Project board to track work status. Columns:

- **Backlog**: ideas and future milestone work
- **To Do**: agreed work for the current week
- **In Progress**: someone is actively working on it (move here when you
  create the branch)
- **Review**: a pull request is open and waiting for a reviewer
- **Done**: the pull request is merged and the issue is closed

The board is kept current as work happens, not just before a status meeting.

## Communication

- Decisions that matter are recorded in the repository (an issue, a pull
  request description, or a document), not only in chat.
- Communicate before making a major change or touching a file someone else is
  working on.
- Reviews are answered within two days so branches stay short-lived.
- Weekly milestones are due Friday; work is split into issues at the start of
  the week so everyone has a branch and a pull request each week.

## Roles

| Member | Role |
|---|---|
| Jeffrey W. Gregory (@jwm-dev) | Code & Architecture Lead, repo administration |
| Vance Reed (@virtualvance) | Project Management & Domain SME, keeps the board current |
| Ryan Kendrick (@rmkoupi) | Team Morale & Support, documentation and reviews |

Everyone writes application code and reviews pull requests.
