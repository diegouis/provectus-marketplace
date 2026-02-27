#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Audit Artifact Modification: Log all modifications to agent artifacts in JSONL format.

Event:    PostToolUse
Matcher:  Write|Edit
Pattern:  exit-code
Timeout:  5s
"""

import sys
import json
import os
import datetime
from pathlib import Path

# -- Configuration ----------------------------------------------------------
PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
ARTIFACT_PATTERNS = ("agents/", "skills/", "commands/", "hooks/")

# -- Input ------------------------------------------------------------------
try:
    data = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    sys.exit(0)  # Graceful degradation: never block on bad input

# -- Extract Fields ---------------------------------------------------------
tool_name = data.get("tool_name", "")
tool_input = data.get("tool_input", {})
file_path = tool_input.get("file_path", "")
session_id = data.get("session_id", "unknown")

# -- Decision Logic ---------------------------------------------------------
# Only log modifications to agent artifact files
is_artifact = any(pattern in file_path for pattern in ARTIFACT_PATTERNS)

# -- Auxiliary Operations (logging) -----------------------------------------
if is_artifact and file_path:
    try:
        log_dir = PROJECT_DIR / ".claude" / "logs"
        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / "proagent-ae-audit.log"

        entry = json.dumps({
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "event": "PostToolUse",
            "tool": tool_name,
            "file": file_path,
            "session_id": session_id,
        })
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(entry + "\n")
    except Exception:
        pass  # Never let logging break primary function

sys.exit(0)
