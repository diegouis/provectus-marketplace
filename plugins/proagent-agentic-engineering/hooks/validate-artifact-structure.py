#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Validate Artifact Structure: Ensure SKILL.md files have YAML frontmatter before writing.

Event:    PreToolUse
Matcher:  Write|Edit
Pattern:  exit-code
Timeout:  10s
"""

import sys
import json
import os
from pathlib import Path

# -- Configuration ----------------------------------------------------------
PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))

# -- Input ------------------------------------------------------------------
try:
    data = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    sys.exit(0)  # Graceful degradation: never block on bad input

# -- Extract Fields ---------------------------------------------------------
tool_name = data.get("tool_name", "")
tool_input = data.get("tool_input", {})
file_path = tool_input.get("file_path", "")
content = tool_input.get("content", "")

# -- Decision Logic ---------------------------------------------------------
# Only validate SKILL.md files
if file_path.endswith("/SKILL.md") or file_path.endswith("\\SKILL.md"):
    # For Write tool, check content directly
    if tool_name == "Write" and content:
        if not content.strip().startswith("---"):
            print(
                "SKILL.md files must start with YAML frontmatter (---). "
                "Add frontmatter with at least: name, description.",
                file=sys.stderr,
            )
            sys.exit(2)  # Block

    # For Edit tool, we can't easily validate partial edits -- allow
    # The full file validation happens on Write

# -- Auxiliary Operations ---------------------------------------------------
try:
    log_dir = PROJECT_DIR / ".claude" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / "proagent-ae-validation.log"
    if file_path:
        import datetime
        entry = json.dumps({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "event": "PreToolUse",
            "tool": tool_name,
            "file": file_path,
            "decision": "allow"
        })
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
except Exception:
    pass  # Never let logging break primary function

sys.exit(0)
