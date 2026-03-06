---
description: Generate a CHANGELOG entry from recent commits and prepare a marketplace release
argument-hint: patch | minor | major (optional — auto-detected if omitted)
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# /release — Generate Changelog & Prepare Release

You are preparing a release for the Provectus Marketplace.

## Step 1: Gather context

1. Read `VERSION` to get the current version.
2. Run `git tag --sort=-v:refname | head -1` to find the latest tag.
3. Run `git log --no-merges --format="%h|%s|%an" <latest-tag>..HEAD` to get commits since that tag.
4. If there are no new commits, tell the user there is nothing to release and stop.

## Step 2: Categorize commits

Group every commit by conventional-commit type:

| Prefix | Category |
|--------|----------|
| `feat` | Features |
| `fix` | Fixes |
| `chore` | Chores |
| `docs` | Documentation |
| anything else | Other |

For each commit, extract the scope (e.g., `proagent-ae` from `feat(proagent-ae): ...`) to identify affected plugins.

## Step 3: Determine version bump

If the user provided an argument ($ARGUMENTS), use it as the bump type (`patch`, `minor`, or `major`).

Otherwise, recommend a bump based on the commits:
- Any `feat` → **minor**
- Only `fix`/`chore`/`docs` → **patch**
- Any commit message contains `BREAKING CHANGE` or starts with `feat!`/`fix!` → **major**

## Step 4: Write the CHANGELOG entry

Read the current `CHANGELOG.md`. Insert a new entry **directly below the `<!-- New entries are added below this line by /release -->` marker**.

Use this format:

```markdown
## [X.Y.Z] - YYYY-MM-DD

Brief 2-3 sentence narrative summary describing the most important changes in this release,
written for both technical and non-technical readers. Focus on *what changed and why it matters*,
not implementation details.

### Features
- **scope** — description (`hash`)

### Fixes
- **scope** — description (`hash`)

### Chores
- description (`hash`)

### Documentation
- description (`hash`)
```

Rules:
- Only include category sections that have commits.
- The narrative summary should highlight the most impactful changes.
- Use the cleaned commit subject (strip type prefix and trailing PR references).
- Link commit hashes: e.g., [`abc1234`](https://github.com/diegouis/provectus-marketplace/commit/abc1234).
- List affected plugins in the summary if the release touches specific plugins.

## Step 5: Present summary

After writing the CHANGELOG entry, display:

1. The version bump: `current version` → `new version`
2. A count of commits by category
3. The list of affected plugins (if any)
4. Instructions to finalize the release:

```
To finalize this release, run:

  task release BUMP=<type>

Preview without making changes:

  task release:dry BUMP=<type>

This will validate plugins, update VERSION and marketplace.json, commit, tag, and push.
The release-notify workflow will then post to Slack automatically.
```

## Important

- Do **NOT** modify `VERSION` or `marketplace.json` — the release script handles that.
- Do **NOT** create git tags or commits — the release script handles that.
- Only write to `CHANGELOG.md`.
