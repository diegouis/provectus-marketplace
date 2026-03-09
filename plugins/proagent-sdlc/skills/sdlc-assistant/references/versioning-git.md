# Versioning and Git Workflows

## Conventional Commit Format

Follows conventional commit standards and branch management best practices.

- `feat(scope):` - New feature (minor version bump)
- `fix(scope):` - Bug fix (patch version bump)
- `docs(scope):` - Documentation only
- `refactor(scope):` - Code restructure, no behavior change
- `test(scope):` - Test additions or corrections
- `chore(scope):` - Build, CI, dependency updates
- `feat!:` or `BREAKING CHANGE:` - Breaking change (major version bump)

## Branch Workflow

- `main` - Production-ready code
- `feature/<name>` - New features
- `fix/<name>` - Bug fixes
- `release/<version>` - Release preparation
- PRs required for all merges to main
- CI must pass before merge

## Enhanced Commit Workflow

From awesome-claude-code `resources/slash-commands/commit/commit.md`:
- Analyze staged changes to auto-generate semantic commit messages
- Validate conventional commit format before committing
- Include scope detection from changed file paths

## AI-Powered PR Creation

From awesome-claude-code `resources/slash-commands/create-pr/create-pr.md`:
- Auto-generate PR title and description from branch commits
- Link related issues automatically
- Populate review checklist based on change types

## Branch Finalization

From superpowers `skills/finishing-a-development-branch/SKILL.md`:
- Pre-merge quality checklist: all tests pass, no TODO/FIXME in diff, documentation updated
- Squash or rebase strategy recommendation based on commit history
- Final review dispatch before merge
