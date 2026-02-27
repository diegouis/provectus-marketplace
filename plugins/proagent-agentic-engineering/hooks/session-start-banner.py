#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Session Start Banner: Display plugin loaded message with version and available commands.

Event:    SessionStart
Matcher:  *
Pattern:  exit-code
Timeout:  5s
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
    sys.exit(0)  # Graceful degradation

# -- Decision Logic ---------------------------------------------------------
# Check if plugin is present
plugin_json = PROJECT_DIR / ".claude-plugin" / "plugin.json"
agents_dir = PROJECT_DIR / ".claude" / "agents"
skills_dir = PROJECT_DIR / ".claude" / "skills"

plugin_detected = plugin_json.exists() or agents_dir.exists() or skills_dir.exists()

if plugin_detected:
    version = "unknown"
    try:
        if plugin_json.exists():
            with open(plugin_json, "r", encoding="utf-8") as f:
                meta = json.load(f)
                version = meta.get("version", "unknown")
    except Exception:
        pass

    banner = (
        f"[proagent-agentic-engineering v{version}] "
        "Agentic engineering plugin loaded. "
        "Commands: /proagent-agentic-engineering (hub), "
        "/proagent-agentic-engineering-run (workflows), "
        "/proagent-agentic-engineering-review (quality), "
        "/proagent-agentic-engineering-create (factory)"
    )
    print(banner, file=sys.stderr)

sys.exit(0)
