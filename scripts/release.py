#!/usr/bin/env -S uv run --python 3.13
"""
release.py — Interactive release script for Provectus Marketplace.

Usage:
  uv run scripts/release.py                # interactive mode (prompts for bump type)
  uv run scripts/release.py patch          # non-interactive with bump type
  uv run scripts/release.py --dry-run      # preview changes without committing

Performs the full release flow:
  1. Validates preconditions (branch, clean tree, tools)
  2. Shows commits since last tag
  3. Bumps VERSION and marketplace.json
  4. Commits, tags, and pushes
"""

import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

# ── ANSI helpers ──────────────────────────────────────────────────────────────

BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"

# Disable colors when not a TTY or NO_COLOR is set
if not sys.stdout.isatty() or os.environ.get("NO_COLOR"):
    BOLD = DIM = RESET = RED = GREEN = YELLOW = BLUE = MAGENTA = CYAN = ""

PASS = f"{GREEN}✓{RESET}"
FAIL = f"{RED}✗{RESET}"
ARROW = f"{CYAN}→{RESET}"
DOT = f"{DIM}·{RESET}"

SCOPE_RE = re.compile(r"^[a-z]+\(([^)]+)\):\s*")


def info(msg: str) -> None:
    print(f"  {ARROW} {msg}")


def success(msg: str) -> None:
    print(f"  {PASS} {msg}")


def fail(msg: str) -> None:
    print(f"  {FAIL} {RED}{msg}{RESET}", file=sys.stderr)


def header(msg: str) -> None:
    print(f"\n{BOLD}{msg}{RESET}")


def banner() -> None:
    print(f"""
{BOLD}{MAGENTA}╔══════════════════════════════════════════╗
║   Provectus Marketplace — Release Tool   ║
╚══════════════════════════════════════════╝{RESET}""")


# ── Git / shell helpers ───────────────────────────────────────────────────────

def git(*args: str, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True, text=True, check=check,
    )
    return result.stdout.strip()


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


# ── Version math ──────────────────────────────────────────────────────────────

def bump_version(version: str, bump_type: str) -> str:
    major, minor, patch = (int(x) for x in version.split("."))
    if bump_type == "major":
        major += 1; minor = 0; patch = 0
    elif bump_type == "minor":
        minor += 1; patch = 0
    else:
        patch += 1
    return f"{major}.{minor}.{patch}"


# ── Precondition checks ──────────────────────────────────────────────────────

def check_preconditions() -> bool:
    header("Preflight checks")
    ok = True

    # On main branch
    branch = git("branch", "--show-current")
    if branch == "main":
        success(f"On branch {BOLD}main{RESET}")
    else:
        fail(f"Must be on main (currently on {branch})")
        ok = False

    # Clean working tree (CHANGELOG.md is allowed — /release writes it before task release)
    RELEASE_MANAGED = {"CHANGELOG.md", "VERSION", "marketplace.json"}
    status = git("status", "--porcelain")
    dirty_files = {line[3:] for line in status.splitlines()} if status else set()
    unmanaged = dirty_files - RELEASE_MANAGED
    if not unmanaged:
        if dirty_files:
            success(f"Working tree clean (only release files modified: {', '.join(sorted(dirty_files))})")
        else:
            success("Working tree is clean")
    else:
        fail(f"Working tree has uncommitted changes: {', '.join(sorted(unmanaged))}")
        ok = False

    # jq available
    if shutil.which("jq"):
        success("jq is available")
    else:
        fail("jq is required but not installed")
        ok = False

    # VERSION file exists
    root = Path(git("rev-parse", "--show-toplevel"))
    if (root / "VERSION").is_file():
        success("VERSION file found")
    else:
        fail("VERSION file not found")
        ok = False

    return ok


# ── Commit analysis ──────────────────────────────────────────────────────────

CATEGORIES = {
    "feat": ("Features", "🚀"),
    "fix": ("Fixes", "🔧"),
    "chore": ("Chores", "🧹"),
    "docs": ("Docs", "📚"),
    "other": ("Other", "📦"),
}


def get_commits_since_tag(tag: str) -> list[dict]:
    log = git("log", "--no-merges", "--format=%h|%s|%an", f"{tag}..HEAD")
    if not log:
        return []
    commits = []
    for line in log.splitlines():
        hash_, subject, author = line.split("|", 2)
        if subject.startswith("Merge pull request"):
            continue
        commit_type = "other"
        for prefix in ("feat", "fix", "chore", "docs"):
            if subject.startswith(prefix):
                commit_type = prefix
                break
        scope = ""
        m = SCOPE_RE.match(subject)
        if m:
            scope = m.group(1)
        commits.append({
            "hash": hash_,
            "subject": subject,
            "author": author,
            "type": commit_type,
            "scope": scope,
        })
    return commits


def suggest_bump(commits: list[dict]) -> str:
    subjects = " ".join(c["subject"] for c in commits)
    if "BREAKING CHANGE" in subjects or any(c["subject"].startswith(("feat!", "fix!")) for c in commits):
        return "major"
    if any(c["type"] == "feat" for c in commits):
        return "minor"
    return "patch"


def show_commit_summary(commits: list[dict]) -> None:
    from collections import Counter
    type_counts = Counter(c["type"] for c in commits)
    scopes = sorted({c["scope"] for c in commits if c["scope"]})

    header(f"Commits since last tag ({len(commits)} total)")

    for cat_type, (label, emoji) in CATEGORIES.items():
        count = type_counts.get(cat_type, 0)
        if count:
            print(f"  {emoji}  {label}: {BOLD}{count}{RESET}")

    if scopes:
        print(f"\n  {DIM}Affected plugins:{RESET} {', '.join(scopes)}")

    # Show recent commits (max 15)
    print()
    shown = commits[:15]
    for c in shown:
        scope_str = f"{YELLOW}{c['scope']}{RESET} " if c["scope"] else ""
        type_color = GREEN if c["type"] == "feat" else (RED if c["type"] == "fix" else DIM)
        print(f"  {DIM}{c['hash']}{RESET}  {type_color}{c['type']:5}{RESET}  {scope_str}{c['subject'].split(': ', 1)[-1] if ': ' in c['subject'] else c['subject']}")
    if len(commits) > 15:
        print(f"  {DIM}... and {len(commits) - 15} more{RESET}")


# ── Interactive prompts ───────────────────────────────────────────────────────

def prompt_bump_type(suggested: str) -> str:
    options = ["patch", "minor", "major"]
    header("Select version bump")
    for i, opt in enumerate(options, 1):
        marker = f" {CYAN}← suggested{RESET}" if opt == suggested else ""
        print(f"  {BOLD}{i}{RESET}) {opt}{marker}")

    while True:
        try:
            choice = input(f"\n  Choice [{options.index(suggested) + 1}]: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            sys.exit(1)

        if not choice:
            return suggested
        if choice in ("1", "2", "3"):
            return options[int(choice) - 1]
        if choice in options:
            return choice
        print(f"  {DIM}Enter 1-3 or patch/minor/major{RESET}")


def confirm(prompt: str) -> bool:
    try:
        answer = input(f"\n  {prompt} [Y/n] ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    return answer in ("", "y", "yes")


# ── Release steps ─────────────────────────────────────────────────────────────

def step(label: str) -> None:
    """Print a step label with a spinner-like dot."""
    print(f"\n  {DOT} {DIM}{label}...{RESET}", end="", flush=True)


def step_done(label: str | None = None) -> None:
    extra = f" {label}" if label else ""
    print(f"\r  {PASS}{extra}")


def do_release(bump_type: str, current: str, new: str, dry_run: bool) -> None:
    root = Path(git("rev-parse", "--show-toplevel"))

    header("Release steps")

    if dry_run:
        print(f"  {YELLOW}(dry run — no changes will be made){RESET}\n")

    # 1. Validate plugins
    step("Running plugin validation")
    if not dry_run:
        result = run(["bash", str(root / "scripts" / "validate-plugins.sh")], check=False)
        if result.returncode != 0:
            step_done()
            fail("Plugin validation failed:")
            print(result.stderr or result.stdout)
            sys.exit(1)
    step_done("Plugin validation passed")

    # 2. Update VERSION
    step(f"Updating VERSION ({current} → {new})")
    if not dry_run:
        (root / "VERSION").write_text(new + "\n")
    step_done(f"VERSION → {BOLD}{new}{RESET}")

    # 3. Update marketplace.json
    step("Updating marketplace.json")
    if not dry_run:
        mj = root / "marketplace.json"
        result = run(["jq", "--arg", "v", new, ".version = $v", str(mj)])
        mj.write_text(result.stdout)
    step_done(f"marketplace.json version → {BOLD}{new}{RESET}")

    # 4. Commit
    step("Creating release commit")
    msg = f"chore(release): bump marketplace version to {new}"
    if not dry_run:
        git("add", "VERSION", "marketplace.json", "CHANGELOG.md")
        git("commit", "-m", msg)
    step_done(f"Committed: {DIM}{msg}{RESET}")

    # 5. Tag
    step(f"Creating tag v{new}")
    if not dry_run:
        git("tag", f"v{new}")
    step_done(f"Tagged {BOLD}v{new}{RESET}")

    # 6. Push
    step("Pushing to origin")
    if not dry_run:
        git("push", "origin", "main")
        git("push", "origin", f"v{new}")
    step_done("Pushed commit and tag to origin")


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    banner()

    # Parse args
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]
    bump_arg = args[0] if args else None

    if bump_arg and bump_arg not in ("patch", "minor", "major"):
        fail(f"Invalid bump type: {bump_arg}. Use patch, minor, or major.")
        sys.exit(1)

    # Preflight
    if not check_preconditions():
        print(f"\n  {FAIL} {RED}Preflight failed. Fix the issues above and retry.{RESET}")
        sys.exit(1)

    # Read current state
    root = Path(git("rev-parse", "--show-toplevel"))
    current_version = (root / "VERSION").read_text().strip()
    latest_tag = git("tag", "--sort=-v:refname").splitlines()[0] if git("tag") else None

    header("Current state")
    info(f"Version: {BOLD}{current_version}{RESET}")
    info(f"Latest tag: {BOLD}{latest_tag or '(none)'}{RESET}")

    # Commits since last tag
    if latest_tag:
        commits = get_commits_since_tag(latest_tag)
    else:
        commits = get_commits_since_tag(git("rev-list", "--max-parents=0", "HEAD"))

    if not commits:
        info(f"{YELLOW}No new commits since {latest_tag}. Nothing to release.{RESET}")
        return

    show_commit_summary(commits)

    # Determine bump type
    suggested = suggest_bump(commits)
    if bump_arg:
        bump_type = bump_arg
        info(f"Bump type: {BOLD}{bump_type}{RESET} (from argument)")
    elif sys.stdin.isatty():
        bump_type = prompt_bump_type(suggested)
    else:
        bump_type = suggested
        info(f"Bump type: {BOLD}{bump_type}{RESET} (auto-detected)")

    new_version = bump_version(current_version, bump_type)

    # Confirmation
    header("Release summary")
    print(f"""
  {DIM}Version:{RESET}  {current_version} {ARROW} {BOLD}{GREEN}{new_version}{RESET}
  {DIM}Tag:{RESET}      v{new_version}
  {DIM}Commits:{RESET}  {len(commits)}
  {DIM}Mode:{RESET}     {'DRY RUN' if dry_run else 'LIVE'}
""")

    if sys.stdin.isatty() and not confirm(f"Release {BOLD}v{new_version}{RESET}?"):
        print(f"\n  {DIM}Aborted.{RESET}")
        return

    # Execute
    do_release(bump_type, current_version, new_version, dry_run)

    # Done
    print(f"""
{BOLD}{GREEN}╔══════════════════════════════════════════╗
║  Released v{new_version:<29}║
╚══════════════════════════════════════════╝{RESET}
""")
    if not dry_run:
        info("The release-notify workflow will post to Slack automatically.")
    else:
        info(f"{YELLOW}Dry run complete — no changes were made.{RESET}")

    print()


if __name__ == "__main__":
    main()
