#!/usr/bin/env bash
# validate-plugins.sh — Verify all plugins are properly registered across the marketplace
#
# Checks:
#   1. Required files exist in each plugin directory
#   2. marketplace.json has an entry for each plugin
#   3. .claude-plugin/marketplace.json has an entry for each plugin
#   4. Root README.md mentions each plugin
#   5. Router SKILL.md mentions each non-router plugin
#
# Usage: bash scripts/validate-plugins.sh

set -euo pipefail

# Resolve the marketplace root (one level up from scripts/)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

PLUGINS_DIR="$ROOT/plugins"
MARKETPLACE_JSON="$ROOT/marketplace.json"
CLAUDE_PLUGIN_MARKETPLACE="$ROOT/.claude-plugin/marketplace.json"
ROOT_README="$ROOT/README.md"
ROUTER_SKILL="$ROOT/plugins/proagent-router/skills/proagent-router/SKILL.md"

# Colors
RED='\033[0;31m'
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
BOLD='\033[1m'
NC='\033[0m' # No Color

total_pass=0
total_warn=0
total_fail=0

pass() { echo -e "  ${GREEN}PASS${NC} $1"; total_pass=$((total_pass + 1)); }
warn() { echo -e "  ${YELLOW}WARN${NC} $1"; total_warn=$((total_warn + 1)); }
fail() { echo -e "  ${RED}FAIL${NC} $1"; total_fail=$((total_fail + 1)); }

echo -e "${BOLD}Plugin Validation Report${NC}"
echo "========================"
echo ""

# Collect all plugin directories
plugins=()
for dir in "$PLUGINS_DIR"/proagent-*/; do
  [ -d "$dir" ] || continue
  plugins+=("$(basename "$dir")")
done

if [ ${#plugins[@]} -eq 0 ]; then
  echo "No plugins found in $PLUGINS_DIR"
  exit 1
fi

echo "Found ${#plugins[@]} plugins"
echo ""

# ─── Per-Plugin Checks ───────────────────────────────────────────────

for plugin in "${plugins[@]}"; do
  plugin_dir="$PLUGINS_DIR/$plugin"
  # Extract the practice name (strip "proagent-" prefix)
  practice="${plugin#proagent-}"

  echo -e "${BOLD}── $plugin ──${NC}"

  plugin_status="PASS"

  # 1. Required files
  # plugin.json
  if [ -f "$plugin_dir/.claude-plugin/plugin.json" ]; then
    pass "plugin.json exists"
  else
    fail "plugin.json missing (.claude-plugin/plugin.json)"
    plugin_status="FAIL"
  fi

  # .mcp.json
  if [ -f "$plugin_dir/.mcp.json" ]; then
    pass ".mcp.json exists"
  else
    fail ".mcp.json missing"
    plugin_status="FAIL"
  fi

  # SKILL.md (in any skills/ subdirectory)
  skill_files=$(find "$plugin_dir/skills" -name "SKILL.md" 2>/dev/null || true)
  if [ -n "$skill_files" ]; then
    pass "SKILL.md exists"
  else
    fail "SKILL.md missing (skills/*/SKILL.md)"
    plugin_status="FAIL"
  fi

  # *-hub.md command
  hub_files=$(find "$plugin_dir/commands" -maxdepth 1 -name "*-hub.md" 2>/dev/null || true)
  if [ -n "$hub_files" ]; then
    pass "*-hub.md command exists"
  else
    # Router doesn't have hub command
    if [ "$practice" = "router" ]; then
      warn "*-hub.md missing (expected for router)"
    else
      fail "*-hub.md command missing"
      plugin_status="FAIL"
    fi
  fi

  # *-run.md command
  run_files=$(find "$plugin_dir/commands" -maxdepth 1 -name "*-run.md" 2>/dev/null || true)
  if [ -n "$run_files" ]; then
    pass "*-run.md command exists"
  else
    if [ "$practice" = "router" ]; then
      warn "*-run.md missing (expected for router)"
    else
      fail "*-run.md command missing"
      plugin_status="FAIL"
    fi
  fi

  # *-review.md command
  review_files=$(find "$plugin_dir/commands" -maxdepth 1 -name "*-review.md" 2>/dev/null || true)
  if [ -n "$review_files" ]; then
    pass "*-review.md command exists"
  else
    if [ "$practice" = "router" ]; then
      warn "*-review.md missing (expected for router)"
    else
      fail "*-review.md command missing"
      plugin_status="FAIL"
    fi
  fi

  # agents/*.md (warn if missing, skip for router)
  agent_files=$(find "$plugin_dir/agents" -name "*.md" 2>/dev/null || true)
  if [ -n "$agent_files" ]; then
    pass "agent definition exists"
  else
    if [ "$practice" = "router" ]; then
      warn "No agent definition (expected for router)"
    else
      warn "No agent definition found (agents/*.md)"
    fi
  fi

  # hooks.json
  if [ -f "$plugin_dir/hooks/hooks.json" ]; then
    pass "hooks.json exists"
  else
    fail "hooks.json missing (hooks/hooks.json)"
    plugin_status="FAIL"
  fi

  # CLAUDE.md
  if [ -f "$plugin_dir/CLAUDE.md" ]; then
    pass "CLAUDE.md exists"
  else
    fail "CLAUDE.md missing"
    plugin_status="FAIL"
  fi

  # README.md
  if [ -f "$plugin_dir/README.md" ]; then
    pass "README.md exists"
  else
    fail "README.md missing"
    plugin_status="FAIL"
  fi

  # 2. marketplace.json entry
  if [ -f "$MARKETPLACE_JSON" ] && jq -e ".plugins[] | select(.name == \"$plugin\")" "$MARKETPLACE_JSON" > /dev/null 2>&1; then
    pass "Listed in marketplace.json"
  else
    fail "Missing from marketplace.json"
    plugin_status="FAIL"
  fi

  # 3. .claude-plugin/marketplace.json entry
  if [ -f "$CLAUDE_PLUGIN_MARKETPLACE" ] && jq -e ".plugins[] | select(.name == \"$plugin\")" "$CLAUDE_PLUGIN_MARKETPLACE" > /dev/null 2>&1; then
    pass "Listed in .claude-plugin/marketplace.json"
  else
    fail "Missing from .claude-plugin/marketplace.json"
    plugin_status="FAIL"
  fi

  # 4. Root README.md mention
  if [ -f "$ROOT_README" ] && grep -q "$plugin" "$ROOT_README"; then
    pass "Mentioned in root README.md"
  else
    fail "Missing from root README.md"
    plugin_status="FAIL"
  fi

  # 5. Router SKILL.md mention (skip for router itself)
  if [ "$practice" != "router" ]; then
    if [ -f "$ROUTER_SKILL" ] && grep -q "$practice" "$ROUTER_SKILL"; then
      pass "Mentioned in router SKILL.md"
    else
      fail "Missing from router SKILL.md"
      plugin_status="FAIL"
    fi
  fi

  echo -e "  Status: ${BOLD}$plugin_status${NC}"
  echo ""
done

# ─── JSON Validation ─────────────────────────────────────────────────

echo -e "${BOLD}── JSON Validation ──${NC}"

if [ -f "$MARKETPLACE_JSON" ] && jq . "$MARKETPLACE_JSON" > /dev/null 2>&1; then
  pass "marketplace.json is valid JSON"
else
  fail "marketplace.json is invalid JSON"
fi

if [ -f "$CLAUDE_PLUGIN_MARKETPLACE" ] && jq . "$CLAUDE_PLUGIN_MARKETPLACE" > /dev/null 2>&1; then
  pass ".claude-plugin/marketplace.json is valid JSON"
else
  fail ".claude-plugin/marketplace.json is invalid JSON"
fi

echo ""

# ─── Summary ─────────────────────────────────────────────────────────

echo -e "${BOLD}Summary${NC}"
echo "======="
echo -e "  ${GREEN}PASS${NC}: $total_pass"
echo -e "  ${YELLOW}WARN${NC}: $total_warn"
echo -e "  ${RED}FAIL${NC}: $total_fail"
echo ""

if [ "$total_fail" -gt 0 ]; then
  echo -e "${RED}${BOLD}RESULT: FAIL${NC} — $total_fail issue(s) require attention"
  exit 1
else
  echo -e "${GREEN}${BOLD}RESULT: PASS${NC} — all checks passed ($total_warn warning(s))"
  exit 0
fi
