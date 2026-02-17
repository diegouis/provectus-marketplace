# ProAgent Marketplace — Continuation Plan

## What Was Built

A monorepo plugin marketplace at `./provectus-marketplace/` with **14 ProAgent plugins** generated from **843 assets** across **17 source repositories**. The marketplace is a git repo pushed to **https://github.com/diegouis/provectus-marketplace** (private, under `diegouis` account).

## Marketplace Structure

```
provectus-marketplace/
├── marketplace.json              # Marketplace manifest (14 plugins)
├── scan-reports/                 # Raw scan data (4 batch JSON reports)
├── catalog/                      # Unified catalog + 14 per-practice manifests
│   ├── catalog.json
│   ├── catalog-summary.md
│   ├── gaps.json
│   └── proagent-<practice>-manifest.json (x14)
└── plugins/                      # 14 proagent-* plugins (~140 files total)
    ├── proagent-agentic-engineering/
    ├── proagent-sdlc/
    ├── proagent-platform/
    ├── proagent-devops/
    ├── proagent-qa/
    ├── proagent-backend/
    ├── proagent-frontend/
    ├── proagent-delivery/
    ├── proagent-security/
    ├── proagent-data/
    ├── proagent-ml-ai/
    ├── proagent-hr/
    ├── proagent-sales/
    └── proagent-finance/
```

## Each Plugin Contains

```
proagent-<practice>/
├── .claude-plugin/plugin.json    # Metadata, version, resources registry
├── skills/<practice>-assistant/SKILL.md  # Core skill (gerund name)
├── commands/
│   ├── proagent-<practice>-hub.md        # Capabilities overview
│   ├── proagent-<practice>-run.md        # Task runner (5+ modes)
│   └── proagent-<practice>-review.md     # Reviewer (3-4 modes)
├── agents/<practice>-specialist.md       # Specialist subagent
├── hooks/hooks.json                      # Lifecycle hooks
├── .mcp.json                             # MCP server configs
├── CLAUDE.md                             # Claude context
└── README.md                             # Installation & usage
```

## Plugin Review Status

### Completed Reviews (fixed & pushed)

1. **proagent-agentic-engineering** (commit `e0977a6`) — Grade: A-
   - Fixed: MCP env var mismatch, PreToolUse hook now blocks with exit 2, SessionStart scoped to agentic projects, added resources registry to plugin.json, added allowed-tools to hub command

2. **proagent-sdlc** (commit `dcbdfd7`) — Grade: B+ → A- after fixes
   - Fixed: hooks.json rewritten to valid Claude Code format (was custom schema that wouldn't execute), command files renamed with proagent-sdlc- prefix, added argument-hint and allowed-tools to all commands, added version to plugin.json, set agent model to sonnet, fixed ATLASSIAN_SITE_URL → ATLASSIAN_DOMAIN, removed non-standard "Announce" directive

### Pending Reviews (12 remaining)

Review in this order (by asset count / complexity):

3. **proagent-platform** (127 assets) — Note: CLAUDE.md and README.md were created by the orchestrator, not the generator agent. May need extra attention.
4. **proagent-devops** (126 assets)
5. **proagent-qa** (110 assets)
6. **proagent-backend** (63 assets)
7. **proagent-frontend** (60 assets)
8. **proagent-delivery** (52 assets)
9. **proagent-security** (51 assets)
10. **proagent-data** (27 assets)
11. **proagent-ml-ai** (22 assets)
12. **proagent-hr** (22 assets)
13. **proagent-sales** (13 assets)
14. **proagent-finance** (4 assets)

## Common Issues Found in Reviews (check for these in every plugin)

| Issue | What to Check |
|-------|---------------|
| **hooks.json format** | Must use `{"hooks": {"EventName": [{"matcher": "...", "hooks": [{"type": "command", "command": "...", "timeout": N}]}]}}` — NOT custom schemas |
| **Command file naming** | Must be `proagent-<practice>-hub.md`, not just `hub.md` |
| **Command frontmatter** | Must have `argument-hint` and `allowed-tools` if using Bash or scanning |
| **plugin.json completeness** | Must have `version`, `resources` registry with paths to skills/agents/commands/hooks/mcp |
| **MCP env var consistency** | Env var names must match across .mcp.json, CLAUDE.md, and README.md |
| **Agent model** | Should be explicit (`sonnet` for most, `opus` for review-heavy), not `inherit` |
| **SKILL.md** | No "Announce at start" directives; must have trigger terms and scope boundaries in description |
| **.mcp.json existence** | Some plugins had `mcp.json` renamed to `.mcp.json` — verify the dotfile exists |

## MCP Integrations Configured

Slack, Google Docs, Gmail, Google Meet, Google Calendar, AWS, GCP, GitHub, GitLab, Jira, Confluence, Playwright, Pencil, Excalidraw, Eraser.io

## How to Continue

```
# In a new Claude Code session:
cd "/Users/diegofernandomartinezayala/My Drive (dmartinezayala@provectus.com)/Projects/Agentic Coding/provectus-marketplace"

# Then ask:
"Review the proagent-platform plugin following the review checklist in CONTINUATION_PLAN.md. Read all 10 files, assess against the common issues list, grade it, and apply fixes."
```

Repeat for each remaining plugin, then:
- Commit and push after each fix batch
- After all 14 are reviewed, do a final validation pass
- Optionally: create a root CLAUDE.md for the marketplace itself
