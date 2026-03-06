#!/usr/bin/env python3
"""
send-changelog-to-slack.py

Generates a changelog from the latest push to main and posts it
to Slack via an incoming webhook using Block Kit rich_text blocks.

Usage:
  SLACK_WEBHOOK_URL="https://hooks.slack.com/..." python3 scripts/send-changelog-to-slack.py

In GitHub Actions the webhook comes from a repo secret.
"""

import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

REPO_URL = "https://github.com/diegouis/provectus-marketplace"
REPO_NAME = "provectus-marketplace"

CATEGORIES = [
    ("feat",  "Features", "rocket"),
    ("fix",   "Fixes",    "wrench"),
    ("chore", "Chores",   "broom"),
    ("docs",  "Docs",     "books"),
    ("other", "Other",    "package"),
]

SCOPE_RE = re.compile(r"^[a-z]+\(([^)]+)\):\s*")
PR_REF_RE = re.compile(r"\s*\(#\d+\)$")


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True, text=True, check=True,
    )
    return result.stdout.strip()


def get_commit_range() -> str:
    # Priority 1: Tag-based range (set by release-notify workflow)
    prev_tag = os.environ.get("RELEASE_PREVIOUS_TAG", "")
    curr_tag = os.environ.get("RELEASE_CURRENT_TAG", "")
    if prev_tag and curr_tag:
        return f"{prev_tag}..{curr_tag}"

    # Priority 2: Push-event range (set by GitHub Actions push trigger)
    before = os.environ.get("GITHUB_EVENT_BEFORE", "")
    sha = os.environ.get("GITHUB_SHA", "")
    if before and sha:
        return f"{before}..{sha}"

    # Fallback
    return "HEAD~1..HEAD"


def parse_commits(range_spec: str) -> list[dict]:
    log = git("log", "--no-merges", "--format=%h|%s|%an", range_spec)
    if not log:
        return []

    commits = []
    for line in log.splitlines():
        hash_, subject, author = line.split("|", 2)

        if subject.startswith("Merge pull request"):
            continue

        # Detect type
        commit_type = "other"
        for prefix in ("feat", "fix", "chore", "docs"):
            if subject.startswith(prefix):
                commit_type = prefix
                break

        # Extract scope
        scope = ""
        m = SCOPE_RE.match(subject)
        if m:
            scope = m.group(1)

        # Clean subject: strip type prefix and trailing PR ref
        clean = subject.split(": ", 1)[-1] if ": " in subject else subject
        clean = PR_REF_RE.sub("", clean)

        commits.append({
            "hash": hash_,
            "subject": clean,
            "author": author,
            "type": commit_type,
            "scope": scope,
        })

    return commits


def build_category_blocks(cat_type: str, label: str, emoji: str, commits: list[dict]) -> list[dict]:
    """Build blocks for one category: section header + rich_text bullet list."""
    bullet_items = []
    for c in commits:
        elements = []
        if c["scope"]:
            elements.append({"type": "text", "text": f"{c['scope']}  ", "style": {"bold": True, "italic": True}})
        elements.append({"type": "text", "text": c["subject"]})
        elements.append({"type": "text", "text": "  "})
        elements.append({
            "type": "link",
            "url": f"{REPO_URL}/commit/{c['hash']}",
            "text": c["hash"],
            "style": {"code": True},
        })
        bullet_items.append({"type": "rich_text_section", "elements": elements})

    return [
        # Category header as its own section block (gives natural top padding)
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":{emoji}:  *{label}*  ({len(commits)})",
            },
        },
        # Bullet list as rich_text block
        {
            "type": "rich_text",
            "elements": [
                {
                    "type": "rich_text_list",
                    "style": "bullet",
                    "indent": 0,
                    "elements": bullet_items,
                },
            ],
        },
    ]


def build_payload(commits: list[dict]) -> dict:
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    head_sha = git("rev-parse", "--short", "HEAD")

    # Detect release context
    release_tag = os.environ.get("RELEASE_CURRENT_TAG", "")

    # Group by type
    grouped = defaultdict(list)
    for c in commits:
        grouped[c["type"]].append(c)

    # Category blocks (only non-empty) — each returns a list of blocks
    category_blocks = []
    for cat_type, label, emoji in CATEGORIES:
        if grouped[cat_type]:
            category_blocks.extend(build_category_blocks(cat_type, label, emoji, grouped[cat_type]))

    # Collect unique authors
    authors = sorted({c["author"] for c in commits})
    authors_str = ", ".join(authors)

    commit_s = "commit" if len(commits) == 1 else "commits"

    # Header: include version when this is a tag-based release
    if release_tag:
        version = release_tag.lstrip("v")
        header_text = f"Provectus Marketplace v{version} — Changelog"
    else:
        header_text = "Provectus Marketplace — Changelog"

    # Footer: link to release tag or commit history
    if release_tag:
        footer_text = (
            f"*{len(commits)}* {commit_s} in *{release_tag}*"
            f"  •  <{REPO_URL}/releases/tag/{release_tag}|View release>"
            f"  •  <{REPO_URL}|{REPO_NAME}>"
        )
    else:
        footer_text = (
            f"*{len(commits)}* {commit_s} pushed to *main*"
            f"  •  <{REPO_URL}/commits/main|View full history>"
            f"  •  <{REPO_URL}|{REPO_NAME}>"
        )

    return {
        "blocks": [
            # Title
            {
                "type": "header",
                "text": {"type": "plain_text", "text": header_text, "emoji": True},
            },
            # Metadata line
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": f":calendar:  *{date}*"},
                    {"type": "mrkdwn", "text": f":git:  `{head_sha}`"},
                    {"type": "mrkdwn", "text": f":busts_in_silhouette:  {authors_str}"},
                ],
            },
            {"type": "divider"},
            # Categories
            *category_blocks,
            # Footer
            {"type": "divider"},
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": footer_text,
                    },
                ],
            },
        ]
    }


def send_to_slack(webhook_url: str, payload: dict) -> None:
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        if resp.status != 200:
            body = resp.read().decode()
            print(f"Failed to send changelog. HTTP {resp.status}: {body}", file=sys.stderr)
            sys.exit(1)

    print(f"Changelog sent to Slack successfully. ({len(payload['blocks'])} blocks)")


def main():
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "")
    if not webhook_url:
        print("Error: SLACK_WEBHOOK_URL is not set.", file=sys.stderr)
        sys.exit(1)

    range_spec = get_commit_range()
    commits = parse_commits(range_spec)

    if not commits:
        print(f"No non-merge commits in range {range_spec}. Nothing to send.")
        return

    payload = build_payload(commits)
    send_to_slack(webhook_url, payload)


if __name__ == "__main__":
    main()
