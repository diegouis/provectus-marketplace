#!/usr/bin/env python3
"""
Automatic version bumping for provectus-marketplace using Conventional Commits.

Finds the last v*.*.* git tag, scans commits since then, maps them to affected
plugins via changed files or commit scope, determines bump level per plugin,
and updates plugin.json + marketplace.json accordingly.

Usage:
    python3 scripts/bump-versions.py [--dry-run] [--tag] [--from-ref REF]
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PLUGINS_DIR = REPO_ROOT / "plugins"
MARKETPLACE_JSON = REPO_ROOT / "marketplace.json"

BUMP_TYPES = {"patch": 0, "minor": 1, "major": 2}
BUMP_PREFIXES = {
    "fix": "patch",
    "feat": "minor",
}
NO_BUMP_PREFIXES = {"docs", "chore", "style", "test", "ci", "refactor", "build", "perf"}


def run_git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout.strip()


def find_latest_tag() -> str | None:
    try:
        tag = run_git("describe", "--tags", "--match", "v*.*.*", "--abbrev=0")
        return tag
    except RuntimeError:
        return None


def get_commits_since(ref: str) -> list[dict]:
    """Return list of {hash, subject, body, parents} since ref (exclusive)."""
    sep = "---COMMIT-SEP---"
    field_sep = "---FIELD-SEP---"
    fmt = f"%H{field_sep}%P{field_sep}%s{field_sep}%b{sep}"
    try:
        log = run_git("log", f"{ref}..HEAD", f"--pretty=format:{fmt}")
    except RuntimeError:
        return []
    if not log:
        return []
    commits = []
    for entry in log.split(sep):
        entry = entry.strip()
        if not entry:
            continue
        parts = entry.split(field_sep, 3)
        if len(parts) < 4:
            continue
        hash_, parents, subject, body = parts
        commits.append({
            "hash": hash_.strip(),
            "parents": parents.strip().split(),
            "subject": subject.strip(),
            "body": body.strip(),
        })
    return commits


def parse_conventional_commit(subject: str, body: str) -> dict | None:
    """Parse a conventional commit message. Returns {type, scope, breaking, bump} or None."""
    # Pattern: type(scope)!: description  OR  type!: description  OR  type: description
    m = re.match(r"^(\w+)(?:\(([^)]*)\))?(!)?\s*:\s*(.+)$", subject)
    if not m:
        return None
    cc_type = m.group(1).lower()
    scope = m.group(2)
    bang = m.group(3) is not None
    breaking = bang or "BREAKING CHANGE" in body or "BREAKING-CHANGE" in body

    if breaking:
        bump = "major"
    elif cc_type in BUMP_PREFIXES:
        bump = BUMP_PREFIXES[cc_type]
    elif cc_type in NO_BUMP_PREFIXES:
        bump = None
    else:
        bump = None

    return {"type": cc_type, "scope": scope, "breaking": breaking, "bump": bump}


def get_changed_files(commit_hash: str) -> list[str]:
    """Return list of files changed in a commit."""
    try:
        output = run_git("diff-tree", "--no-commit-id", "-r", "--name-only", commit_hash)
        return [f for f in output.split("\n") if f]
    except RuntimeError:
        return []


def detect_plugins_from_files(files: list[str]) -> set[str]:
    """Extract plugin names from file paths like plugins/<name>/..."""
    plugins = set()
    for f in files:
        m = re.match(r"^plugins/([^/]+)/", f)
        if m:
            plugins.add(m.group(1))
    return plugins


def get_all_plugin_names() -> list[str]:
    """Return sorted list of plugin directory names."""
    if not PLUGINS_DIR.is_dir():
        return []
    return sorted(
        d.name for d in PLUGINS_DIR.iterdir()
        if d.is_dir() and (d / ".claude-plugin" / "plugin.json").exists()
    )


def read_plugin_version(plugin_name: str) -> str:
    path = PLUGINS_DIR / plugin_name / ".claude-plugin" / "plugin.json"
    with open(path) as f:
        data = json.load(f)
    return data.get("version", "0.0.0")


def bump_version(version: str, bump: str) -> str:
    parts = version.split(".")
    if len(parts) != 3:
        parts = ["0", "0", "0"]
    major, minor, patch = int(parts[0]), int(parts[1]), int(parts[2])
    if bump == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump == "minor":
        minor += 1
        patch = 0
    elif bump == "patch":
        patch += 1
    return f"{major}.{minor}.{patch}"


def update_plugin_json(plugin_name: str, new_version: str, dry_run: bool) -> str:
    path = PLUGINS_DIR / plugin_name / ".claude-plugin" / "plugin.json"
    with open(path) as f:
        data = json.load(f)
    old_version = data.get("version", "0.0.0")
    data["version"] = new_version
    if not dry_run:
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
    return old_version


def update_marketplace_json(version_map: dict[str, str], dry_run: bool) -> str:
    """Update marketplace.json with new plugin versions and bump global version.

    Returns the new global version.
    """
    with open(MARKETPLACE_JSON) as f:
        data = json.load(f)

    marketplace_plugin_names = {p["name"] for p in data.get("plugins", [])}
    warnings = []

    for plugin in data.get("plugins", []):
        name = plugin["name"]
        if name in version_map:
            plugin["version"] = version_map[name]

    # Warn about plugins not in marketplace
    for name in version_map:
        if name not in marketplace_plugin_names:
            warnings.append(f"  WARNING: '{name}' updated on disk but not found in marketplace.json")

    # Bump global marketplace version: take the max of all bumped plugin versions
    all_versions = [version_map[n] for n in version_map]
    if all_versions:
        max_version = max(all_versions, key=lambda v: list(map(int, v.split("."))))
        data["version"] = max_version
    else:
        max_version = data.get("version", "0.0.0")

    if not dry_run:
        with open(MARKETPLACE_JSON, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")

    for w in warnings:
        print(w)

    return max_version


def check_working_tree_clean() -> bool:
    try:
        status = run_git("status", "--porcelain")
        return status == ""
    except RuntimeError:
        return False


def main():
    parser = argparse.ArgumentParser(description="Auto-bump plugin versions using Conventional Commits")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without modifying files")
    parser.add_argument("--tag", action="store_true", help="Commit changes and create annotated tag")
    parser.add_argument("--from-ref", type=str, default=None, help="Override baseline ref (e.g. HEAD~5)")
    args = parser.parse_args()

    # Determine baseline ref
    baseline = args.from_ref
    if not baseline:
        baseline = find_latest_tag()
        if not baseline:
            print("ERROR: No v*.*.* tags found and --from-ref not specified.")
            print("  To bootstrap, create a baseline tag first:")
            print("    git tag -a v0.4.0 -m \"Baseline version tag for auto-versioning\"")
            print("  Or run with --from-ref HEAD~N to scan recent commits.")
            sys.exit(1)

    print(f"Baseline: {baseline}")

    # Get commits
    commits = get_commits_since(baseline)
    if not commits:
        print("Nothing to bump — no commits since baseline.")
        sys.exit(0)

    # Analyze commits → per-plugin bump level
    all_plugins = set(get_all_plugin_names())
    plugin_bumps: dict[str, str] = {}  # plugin_name → highest bump type

    for commit in commits:
        # Skip merge commits
        if len(commit["parents"]) > 1:
            continue

        parsed = parse_conventional_commit(commit["subject"], commit["body"])
        if not parsed or parsed["bump"] is None:
            continue

        bump = parsed["bump"]

        # Determine affected plugins
        affected: set[str] = set()

        # 1. From scope if it matches a plugin name
        if parsed["scope"] and parsed["scope"] in all_plugins:
            affected.add(parsed["scope"])

        # 2. From changed files
        changed = get_changed_files(commit["hash"])
        affected |= detect_plugins_from_files(changed)

        if not affected:
            continue

        for plugin in affected:
            if plugin not in plugin_bumps:
                plugin_bumps[plugin] = bump
            elif BUMP_TYPES[bump] > BUMP_TYPES[plugin_bumps[plugin]]:
                plugin_bumps[plugin] = bump

    if not plugin_bumps:
        print("Nothing to bump — no version-affecting conventional commits found.")
        sys.exit(0)

    # Compute new versions and apply
    version_map: dict[str, str] = {}
    print()
    for plugin_name in sorted(plugin_bumps):
        current = read_plugin_version(plugin_name)
        bump_type = plugin_bumps[plugin_name]
        new_ver = bump_version(current, bump_type)
        version_map[plugin_name] = new_ver
        prefix = "[DRY RUN] " if args.dry_run else ""
        print(f"{prefix}{plugin_name}: {current} → {new_ver} ({bump_type})")
        update_plugin_json(plugin_name, new_ver, args.dry_run)

    print()
    global_ver = update_marketplace_json(version_map, args.dry_run)
    prefix = "[DRY RUN] " if args.dry_run else ""
    print(f"{prefix}marketplace.json global version → {global_ver}")

    if args.dry_run:
        print("\nDry run complete — no files were modified.")
        return

    # Optionally commit and tag
    if args.tag:
        if not check_working_tree_clean() and not plugin_bumps:
            print("\nERROR: Working tree is dirty. Commit or stash changes before using --tag.")
            sys.exit(1)

        # Stage updated files
        files_to_stage = [str(MARKETPLACE_JSON.relative_to(REPO_ROOT))]
        for plugin_name in version_map:
            rel = str((PLUGINS_DIR / plugin_name / ".claude-plugin" / "plugin.json").relative_to(REPO_ROOT))
            files_to_stage.append(rel)

        for f in files_to_stage:
            run_git("add", f)

        tag_name = f"v{global_ver}"
        commit_msg = f"chore(release): bump versions to {tag_name}"
        run_git("commit", "-m", commit_msg)
        run_git("tag", "-a", tag_name, "-m", f"Release {tag_name}")

        print(f"\nCommitted and tagged as {tag_name}")


if __name__ == "__main__":
    main()
