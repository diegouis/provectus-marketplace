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

3. **proagent-platform** — Grade: B → A- after fixes
   - Fixed: hooks.json rewritten to valid Claude Code format (was custom schema with invalid matcher objects and non-existent Notification event), command files renamed with proagent-platform- prefix, added argument-hint to hub command, plugin.json restructured with resources registry (replaced flat directory keys), updated CLAUDE.md and README.md structure diagrams

4. **proagent-devops** (126 assets) — Grade: C+ → A- after fixes
   - Fixed: hooks.json completely rewritten (was entirely custom schema with no executable hooks), added YAML frontmatter to all 3 commands (were missing entirely), plugin.json restructured from custom object-array format to standard resources registry, renamed hub from proagent-devops.md to proagent-devops-hub.md, changed agent model from opus to sonnet, removed invalid aws/gcp MCP entries (were CLIs not MCP servers), added env vars section to README, updated CLAUDE.md structure diagram

5. **proagent-qa** (110 assets) — Grade: C → A- after fixes
   - Fixed: hooks.json completely rewritten (was custom schema with pre-commit/post-test/pre-merge events that don't exist in Claude Code), added YAML frontmatter to SKILL.md (was missing entirely), added YAML frontmatter to agent (was missing name/description/model/tools), added frontmatter to all 3 commands, plugin.json restructured with resources registry (removed entrypoint/dependencies/tags non-standard keys), fixed MCP env vars (GITHUB_TOKEN→GITHUB_PERSONAL_ACCESS_TOKEN, GITLAB_TOKEN→GITLAB_PERSONAL_ACCESS_TOKEN, JIRA_*→ATLASSIAN_*, server-jira→server-atlassian), fixed CLAUDE.md mcp.json→.mcp.json reference, updated README env var names

6. **proagent-backend** (63 assets) — Grade: C+ → A- after fixes
   - Fixed: hooks.json completely rewritten (was custom schema identical to devops pattern), added YAML frontmatter to all 3 commands, plugin.json restructured with resources registry, changed agent model from opus to sonnet, replaced all 4 invalid MCP entries (gh/glab/aws/gcloud CLIs with usage arrays) with valid GitHub/GitLab MCP servers, fixed mcp.json→.mcp.json references in CLAUDE.md and README.md

7. **proagent-frontend** (60 assets) — Grade: C → A- after fixes
   - Fixed: hooks.json rewritten to valid Claude Code format (was custom schema), added YAML frontmatter to all 3 commands (argument-hint, allowed-tools), plugin.json restructured with resources registry (removed source_repos, flat arrays), fixed MCP env vars (GITHUB_TOKEN→GITHUB_PERSONAL_ACCESS_TOKEN, GITLAB_TOKEN→GITLAB_PERSONAL_ACCESS_TOKEN), added -y flag to Playwright npx, fixed mcp.json→.mcp.json references in CLAUDE.md, README.md, and hub command, updated hooks description in CLAUDE.md

8. **proagent-delivery** (52 assets) — Grade: C+ → A- after fixes
   - Fixed: hooks.json completely rewritten (was custom schema with name/event/rules/action_template objects), plugin.json restructured with resources registry (was flat directory paths with repository/email non-standard keys), agent model changed from inherit to sonnet, removed "Announce at start" directive from SKILL.md, added argument-hint and allowed-tools to all 3 commands, .mcp.json consolidated Jira+Confluence into single Atlassian server (@modelcontextprotocol/server-atlassian), fixed ATLASSIAN_SITE_URL→ATLASSIAN_DOMAIN across .mcp.json/CLAUDE.md/README.md, fixed mcp.json→.mcp.json reference in CLAUDE.md

9. **proagent-security** (51 assets) — Grade: C → A- after fixes
   - Fixed: hooks.json completely rewritten (was custom schema with tool_patterns/file_patterns/command_patterns/validations arrays), plugin.json restructured with resources registry (was object-array format with source_repos/mcp_integrations non-standard keys), replaced both invalid MCP entries (gh CLI and glab CLI with usage_examples/security_operations) with valid GitHub/GitLab MCP servers, agent model changed from opus to sonnet, added YAML frontmatter to all 3 commands (were missing entirely), fixed mcp.json→.mcp.json reference in CLAUDE.md

10. **proagent-data** (27 assets) — Grade: C → A- after fixes
    - Fixed: hooks.json completely rewritten (was custom schema with tool_patterns/file_patterns/command_patterns/validations/checks arrays), plugin.json restructured with resources registry (was object-array format with source_repos/mcp_integrations), replaced all 3 invalid MCP entries (aws CLI, gcloud CLI, gh CLI with usage_examples/required_env) with valid GitHub MCP server only, agent model changed from opus to sonnet, added YAML frontmatter to all 3 commands (were missing entirely), fixed mcp.json→.mcp.json reference in CLAUDE.md

11. **proagent-ml-ai** (22 assets) — Grade: C → A- after fixes
    - Fixed: hooks.json completely rewritten (was custom schema with tool_patterns/file_patterns/command_patterns/validations/checks arrays), plugin.json restructured with resources registry (was object-array format with source_repos/mcp_integrations, author as string→object), replaced all 3 invalid MCP entries (uvx awslabs.aws-documentation-mcp-server, google-cloud-mcp-server, github-mcp-server) with valid GitHub MCP server only, agent model changed from opus to sonnet, added YAML frontmatter to all 3 commands (were missing entirely), fixed mcp.json→.mcp.json references in CLAUDE.md and README.md

12. **proagent-hr** (22 assets) — Grade: C+ → A- after fixes
    - Fixed: hooks.json completely rewritten (was custom schema with pre-commit/pre-publish events, file_patterns, required_sections, flagged_terms), plugin.json restructured with resources registry (was flat arrays of objects, author as string→object, removed entrypoint/dependencies/tags), added YAML frontmatter to SKILL.md (was missing), added YAML frontmatter to agent (was missing name/description/model/tools), added frontmatter to all 3 commands (were missing), replaced all 4 invalid MCP entries (@anthropic/mcp-server-* packages) with valid @modelcontextprotocol/server-slack, server-google-drive, server-github, fixed mcp.json→.mcp.json references in CLAUDE.md, hub command, and README.md

13. **proagent-sales** (13 assets) — Grade: C → A- after fixes
    - Fixed: hooks.json completely rewritten (was custom schema with tool_patterns/file_patterns/validations/check_rules/on_failure), plugin.json restructured with resources registry (was object-array format with mcp_integrations/source_repos, author as string→object, removed category), replaced all 4 invalid MCP entries (@anthropic/mcp-* packages with usage/description objects) with valid @modelcontextprotocol/server-slack, server-google-drive, server-github, agent model changed from opus to sonnet, removed WebSearch/WebFetch from agent tools, added frontmatter to all 3 commands (were missing), fixed mcp.json→.mcp.json in CLAUDE.md

14. **proagent-finance** (4 assets) — Grade: C → A- after fixes
    - Fixed: hooks.json completely rewritten (was custom schema with tool_name/match_pattern/rules/check/severity/fix_hint/action_template), plugin.json restructured with resources registry (was flat directory paths, author email→url, removed repository/license/category/keywords), replaced all 3 invalid MCP entries (@anthropic/mcp-server-* packages) with valid @modelcontextprotocol/server-slack, server-google-drive, server-github, agent model changed from inherit to sonnet, added argument-hint and allowed-tools to all 3 commands, fixed mcp.json→.mcp.json in CLAUDE.md

### ALL 14 PLUGINS REVIEWED AND FIXED

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

## Next Steps

All 14 plugins have been reviewed and fixed. Remaining work:
- Commit and push the final batch of fixes (hr, sales, finance)
- Final validation pass across all plugins
- Apply improvements from IMPROVEMENT_PLAN.md (15 items, P0: Composio integrations, Agent Teams, AWOS workflow)
- Bump marketplace to v0.2.0
- Optionally: create a root CLAUDE.md for the marketplace itself
