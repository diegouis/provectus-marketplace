# Hook Body Template
#
# Canonical structure for `.claude/hooks/<name>.py` artifacts.
# Copy this scaffold and fill in the marked sections.

"""
#!/usr/bin/env uv run
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   <pin versions: "package==1.0.0">
# ]
# ///
\"\"\"
<Hook Name>: <one-line purpose>

Event:    <which hook event>
Matcher:  <matcher pattern or "universal">
Pattern:  <exit-code | json-output>
Timeout:  <seconds>
\"\"\"

import sys
import json
import os
from pathlib import Path

# -- Configuration ----------------------------------------------------------
PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd()))
# <additional config constants>

# -- Input ------------------------------------------------------------------
try:
    data = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    sys.exit(0)  # Graceful degradation: never block on bad input

# -- Extract Fields ---------------------------------------------------------
session_id = data.get("session_id", "unknown")
tool_name = data.get("tool_name", "")
tool_input = data.get("tool_input", {})

# -- Decision Logic ---------------------------------------------------------
# <core logic: validate, decide, transform>

# -- Output -----------------------------------------------------------------
# Exit code pattern:
#   sys.exit(0)  -- allow
#   sys.exit(2)  -- block (print reason to stderr)
# JSON pattern:
#   json.dump({"decision": "allow", "reason": "..."}, sys.stdout)

# -- Auxiliary Operations (logging, etc.) -----------------------------------
# Wrap in try/except with pass -- never let logging break primary function
try:
    # <logging, audit trail, etc.>
    pass
except Exception:
    pass

sys.exit(0)
"""
