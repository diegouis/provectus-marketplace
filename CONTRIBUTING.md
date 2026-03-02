# Contributing to Provectus Marketplace

Thank you for contributing! This document outlines the rules and workflow for this repository.

## Branch Protection Rules

The `main` branch is protected with the following enforced rules:

- **No direct pushes to `main`** — all changes must go through a Pull Request
- **1 approval required** — at least one reviewer must approve before merging
- **Stale reviews are dismissed** — pushing new commits invalidates previous approvals
- **Status checks must pass** — CI must be green before merging
- **Enforced for admins** — these rules apply to everyone, including repo admins
- **No force pushes** — force pushing to `main` is disabled
- **No branch deletion** — `main` cannot be deleted

## Merge Strategy

This repository uses **squash merges only**. When your PR is merged:

- All commits are squashed into a single commit
- The commit title comes from the **PR title**
- The commit message comes from the **PR body**
- The feature branch is **automatically deleted** after merge

This keeps `main` history clean and linear.

## Workflow

### 1. Create a Feature Branch

```bash
git fetch origin
git checkout main && git pull origin main
git checkout -b <type>/<short-description>
```

Branch prefixes:
| Prefix | Use for |
|---|---|
| `feature/` | New functionality |
| `fix/` | Bug fixes |
| `chore/` | Maintenance, deps, config |
| `docs/` | Documentation changes |
| `refactor/` | Code restructuring |
| `test/` | Adding or updating tests |

### 2. Make Changes

- Make small, atomic commits
- Write meaningful commit messages that explain **why**, not just what
- Never commit secrets, `.env` files, or API keys

### 3. Push and Open a PR

```bash
git push -u origin <branch-name>
gh pr create --title "Short description" --body "Details and test plan"
```

### 4. Review and Merge

- Request a review from at least one team member
- Address feedback and push fixes
- Once approved and CI passes, squash-merge via GitHub

## PR Guidelines

- **One PR per feature or fix** — keep reviews focused
- **Write a clear title** — it becomes the commit message in `main`
- **Include a description** — explain what changed and why
- **Add a test plan** — describe how the change was verified

## What NOT to Commit

- `.env` or `.env.*` files
- Private keys (`*.pem`, `*.key`)
- `credentials.*` or `secrets/` directories
- Large binary files
