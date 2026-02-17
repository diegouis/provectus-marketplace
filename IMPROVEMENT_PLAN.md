# Improvement Plan -- Post-Update Analysis

**Generated:** 2026-02-16
**Repos Analyzed:** agents (17 commits), awesome-claude-skills (14 commits), casdk-harness (12 commits), taches-cc-resources (3 commits), Auto-Claude (218 commits)

## Summary

Five upstream repositories received significant updates since the last marketplace sync. The most impactful changes are:

1. **agents repo** modernized all 73 plugins to a new `plugin.json` format, eliminated cross-plugin dependencies, added an Agent Teams plugin for multi-agent orchestration, added comprehensive Python development skills, and bumped to marketplace v1.5.1. The marketplace now has 63 focused plugins with clear category assignments.

2. **awesome-claude-skills** added 78 Composio app automation skills (covering Gmail, Slack, Jira, HubSpot, Salesforce, GitHub, and 72 more SaaS tools) plus a Composio SDK skill with detailed rules for building agent applications. These connect to real external services via the Rube MCP server.

3. **casdk-harness** added the AWOS (Agentic Workflow Operating System) 8-step workflow as a full plugin with 8 specialized agents, mandatory user confirmation gates, session persistence, and a shared `lib/` module. This is a production-ready specification-to-implementation pipeline.

4. **taches-cc-resources** added a `setup-ralph` skill for autonomous coding loops and an `ask-me-questions` slash command for requirement gathering.

5. **Auto-Claude** improvements (PR review, OOM prevention, Sentry integration, 100% backend test coverage) are mostly internal but inform best practices for the QA and DevOps plugins.

---

## High Priority Improvements

### 1. Add Composio App Automation Skills to Relevant Practice Plugins

- **Source**: `awesome-claude-skills/marketplace.json` -- 78 new app automation skills
- **Affects plugins**: proagent-sales, proagent-hr, proagent-delivery, proagent-finance, proagent-devops, proagent-data, proagent-frontend, proagent-platform, proagent-agentic-engineering
- **What changed**: The awesome-claude-skills repo now includes 78 Composio-powered automation skills that connect to real SaaS applications (Slack, Gmail, Google Calendar, Jira, HubSpot, Salesforce, GitHub, GitLab, Confluence, Notion, Linear, etc.) via the Rube MCP server. Each skill follows a consistent pattern: discover tools with `RUBE_SEARCH_TOOLS`, check connection with `RUBE_MANAGE_CONNECTIONS`, execute with `RUBE_MULTI_EXECUTE_TOOL`.
- **Action needed**:
  - **proagent-sales**: Add `salesforce-automation`, `hubspot-automation`, `pipedrive-automation`, `close-automation`, `linkedin-automation` skills. These directly fill the "Commands (need 3, have 2)" gap by providing actionable CRM integrations.
  - **proagent-hr**: Add `bamboohr-automation`, `google-calendar-automation`, `slack-automation`, `gmail-automation` skills. This practice has 0 commands -- Composio skills can provide the missing capability.
  - **proagent-delivery**: Add `jira-automation`, `linear-automation`, `asana-automation`, `clickup-automation`, `monday-automation`, `confluence-automation`, `slack-automation`, `google-calendar-automation` skills. Fills the "Agent definition" and "MCP config" gaps.
  - **proagent-finance**: Add `stripe-automation`, `square-automation`, `shopify-automation`, `invoice-organizer` references. This practice has only 4 assets -- Composio skills dramatically expand it.
  - **proagent-devops**: Add `github-automation`, `gitlab-automation`, `circleci-automation`, `vercel-automation`, `render-automation`, `datadog-automation`, `sentry-automation`, `pagerduty-automation`. Fills the "MCP config" gap.
  - **proagent-data**: Add `googlesheets-automation`, `airtable-automation`, `supabase-automation`, `amplitude-automation`, `mixpanel-automation`, `posthog-automation`, `segment-automation`. Fills the missing commands gap.
  - **proagent-platform**: Add `slack-automation`, `notion-automation`, `confluence-automation`, `google-drive-automation`. Fills "Agent definition" and "Hook definitions" gaps.
  - Add `rube` MCP server as a recommended integration across all practice plugins in their `.mcp.json` files.

### 2. Incorporate Agent Teams Multi-Agent Orchestration Pattern

- **Source**: `agents/plugins/agent-teams/` (v1.0.2) in the agents repo marketplace.json
- **Affects plugins**: proagent-agentic-engineering, proagent-sdlc, proagent-qa
- **What changed**: The agents repo added a new `agent-teams` plugin (v1.0.2) that orchestrates multi-agent teams for parallel code review, hypothesis-driven debugging, and coordinated feature development using Claude Code's native Agent Teams capability. This is a dedicated orchestration layer.
- **Action needed**:
  - **proagent-agentic-engineering**: Update the "Multi-Agent Orchestration" section (Section 7) in `skills/agentic-engineering-assistant/SKILL.md` to reference the Agent Teams plugin patterns. Add Agent Teams as a reference orchestration approach alongside SDD and parallel dispatch.
  - **proagent-sdlc**: Add Agent Teams patterns to code review workflows. The agent-teams plugin specifically supports parallel code review (security + performance + style simultaneously), which directly maps to SDLC review workflows.
  - **proagent-qa**: Integrate Agent Teams debugging patterns (hypothesis-driven debugging with multiple agents testing theories in parallel).

### 3. Add AWOS 8-Step Workflow to SDLC and Delivery Plugins

- **Source**: `casdk-harness/src/harness/plugins/awos_workflow/` -- 8 agents, 1 skill, 1 command, shared lib, templates
- **Affects plugins**: proagent-sdlc, proagent-delivery, proagent-agentic-engineering
- **What changed**: The casdk-harness repo added a complete AWOS workflow plugin with:
  - 8 specialized agents (product, roadmap, architecture, spec, tech, tasks, implement, verify)
  - Mandatory user confirmation gates (configurable per step via `AWOS_SPEC_REFINEMENT`)
  - Session persistence (`awos_session.json`) for resume capability
  - File-based step detection for automatic workflow resumption
  - Consolidated `lib/` module with `session.py` and `step_detector.py`
  - Output templates for each specification artifact
- **Action needed**:
  - **proagent-sdlc**: Add the AWOS workflow pattern as a reference in the SDLC skill. The 8-step pipeline (Product Vision -> Roadmap -> Architecture -> Spec -> Tech Plan -> Tasks -> Implement -> Verify) is a complete specification-to-delivery methodology. Reference the mandatory confirmation pattern as a best practice for autonomous development.
  - **proagent-delivery**: Incorporate the AWOS product/roadmap/architecture steps as delivery planning patterns. The AWOS `context/product/product.md`, `roadmap.md`, and `architecture.md` templates should be referenced as project artifact templates.
  - **proagent-agentic-engineering**: Reference the AWOS plugin structure as an exemplary multi-agent plugin with shared lib, session persistence, and step detection. Update the "Plugin Development" section to reference the `lib/` consolidation pattern.

### 4. Adopt New Plugin.json Format from Agents Repo

- **Source**: `agents/.claude-plugin/marketplace.json` (v1.5.1, 73 plugins)
- **Affects plugins**: All 14 proagent plugins
- **What changed**: The agents repo modernized all plugins to include standardized fields: `name`, `source`, `description`, `version` (semver), `author` (object with name/email/url), `homepage`, `license`, `category`. Cross-plugin dependencies were eliminated. The marketplace manifest now includes 63 unique plugins with clear category assignments (development, workflows, testing, quality, ai-ml, data, operations, infrastructure, performance, modernization, database, security, api, marketing, documentation, business, blockchain, finance, payments, gaming, accessibility, languages).
- **Action needed**:
  - Verify all 14 proagent `plugin.json` files include: `version` (semver), `author` with structured fields, `license`, `category`, and `homepage` fields. Currently the proagent plugins (e.g., `proagent-data`) have these fields but some upstream conventions may differ.
  - Add `homepage` field pointing to the provectus-marketplace repository.
  - Ensure `version` follows semver and is bumped for this update cycle (0.1.0 -> 0.2.0).
  - Validate that no proagent plugin has cross-plugin dependencies (matching upstream pattern of self-contained plugins).

### 5. Incorporate Composio SDK Skill for Agentic Engineering

- **Source**: `awesome-claude-skills/composio-sdk/SKILL.md` plus 28 rule files in `rules/`
- **Affects plugins**: proagent-agentic-engineering, proagent-platform
- **What changed**: A comprehensive Composio SDK skill was added with deep guidance on building AI agents using Composio's Tool Router and direct execution patterns. It includes 28 detailed rule files covering session management, authentication flows, toolkit querying, event-driven triggers, CRUD patterns, custom tools, and multi-tenancy. This is a production-ready guide for building agents that connect to 200+ external services.
- **Action needed**:
  - **proagent-agentic-engineering**: Add Composio SDK patterns to the "MCP Server Development" section. The Tool Router pattern (session-based isolation, dynamic toolkit config, automatic auth management) is a significant new approach to agent-service integration that complements the existing FastMCP/MCP TypeScript SDK guidance.
  - **proagent-platform**: Reference the Composio SDK skill as a platform engineering tool for building service integrations. The session management, multi-tenancy, and webhook patterns are directly relevant to platform teams building developer tools.

---

## Medium Priority Improvements

### 6. Update Python Development Skill Content

- **Source**: `agents/plugins/python-development/` (v1.2.1) in agents repo
- **Affects plugins**: proagent-backend
- **What changed**: The agents repo includes a modernized Python development plugin with Python 3.12+, Django, FastAPI, async patterns, and production best practices at version 1.2.1.
- **Action needed**: Review `proagent-backend` Python guidance against the updated upstream `python-development` plugin. Ensure the backend skill references Python 3.12+ features (improved error messages, `ExceptionGroup`, `TaskGroup`, new typing features) and updated FastAPI/Django best practices.

### 7. Add Tailwind CSS v4 Patterns to Frontend Plugin

- **Source**: `agents/plugins/frontend-mobile-development/` in agents repo (references Tailwind v4 skill)
- **Affects plugins**: proagent-frontend
- **What changed**: The agents repo updated frontend skills to include Tailwind CSS v4 patterns (CSS-first configuration, removal of `tailwind.config.js`, new `@theme` directive, CSS variables-first approach).
- **Action needed**: Update `proagent-frontend` skill with Tailwind CSS v4 migration patterns and new conventions. This is relevant because Provectus teams building frontends need current CSS framework guidance.

### 8. Add Mandatory Confirmation Pattern as a Standard Practice

- **Source**: `casdk-harness/src/harness/plugins/awos_workflow/skills/awos-orchestrate/SKILL.md`
- **Affects plugins**: proagent-sdlc, proagent-agentic-engineering, proagent-delivery
- **What changed**: The AWOS workflow introduced a mandatory confirmation pattern: after each step, the agent must STOP, present output, and wait for explicit user approval (Approve/Edit/Redo). This prevents autonomous runaway and ensures collaborative specification development. The pattern is configurable via `AWOS_SPEC_REFINEMENT` setting.
- **Action needed**:
  - Document this as a best practice in `proagent-agentic-engineering` under the "Multi-Agent Orchestration" section.
  - Add to `proagent-sdlc` as a recommended pattern for any multi-step autonomous workflow.
  - Reference in `proagent-delivery` for milestone-based planning workflows where stakeholder approval is required between phases.

### 9. Expand MCP Integration Lists Based on Composio Coverage

- **Source**: `awesome-claude-skills/marketplace.json` -- 78 app automation skills
- **Affects plugins**: All 14 proagent plugins (via `marketplace.json` and `.mcp.json` files)
- **What changed**: The marketplace now has Composio-powered integrations for 78+ SaaS applications. The `provectus-marketplace/marketplace.json` currently lists only 11 MCP integrations: GitHub, GitLab, Slack, Google Docs, Gmail, Google Calendar, AWS, GCP, Jira, Confluence, Playwright.
- **Action needed**: Update `provectus-marketplace/marketplace.json` `mcp_integrations_available` list to include the Composio-powered integrations that are most relevant to Provectus teams: HubSpot, Salesforce, Notion, Linear, Asana, Datadog, Sentry, PagerDuty, Stripe, BambooHR, Figma, Vercel, CircleCI, Confluence (already listed), Discord, Microsoft Teams.

### 10. Add Session Persistence Patterns from AWOS and casdk-harness

- **Source**: `casdk-harness/src/harness/plugins/awos_workflow/lib/session.py` and `checkpoint.py`
- **Affects plugins**: proagent-agentic-engineering, proagent-sdlc
- **What changed**: The AWOS workflow uses `awos_session.json` for tracking workflow state (current step, completed steps, user confirmations). The casdk-harness has a mature checkpoint system with auto-save, atomic writes, and recovery. This pattern enables reliable resume capability for long-running agentic workflows.
- **Action needed**:
  - **proagent-agentic-engineering**: Document session persistence as a recommended pattern for multi-step plugins. Include both the JSON session file approach (AWOS) and the checkpoint approach (casdk-harness).
  - **proagent-sdlc**: Reference session persistence as an approach to context management in long-running development workflows.

### 11. Incorporate YouTube Design Concept Extractor for Frontend/Design Workflows

- **Source**: agents repo (referenced in commit summary as "YouTube design concept extractor")
- **Affects plugins**: proagent-frontend
- **What changed**: A new skill/tool was added for extracting design concepts from YouTube videos -- useful for design system research, UI/UX pattern discovery, and competitor analysis.
- **Action needed**: If the skill is substantial, reference it in `proagent-frontend` as a design research tool. Lower priority since Provectus teams are less likely to use YouTube-based design research in daily workflows.

---

## Low Priority / Future Improvements

### 12. Align Plugin Category Taxonomy with Agents Repo

- **Source**: `agents/.claude-plugin/marketplace.json` -- 21 categories
- **Affects plugins**: provectus-marketplace catalog and classification
- **What changed**: The agents repo uses a granular category taxonomy with 21 categories (development, workflows, testing, quality, ai-ml, data, operations, infrastructure, performance, modernization, database, security, api, marketing, documentation, business, blockchain, finance, payments, gaming, accessibility, languages). The provectus marketplace uses 14 practice-based categories.
- **Action needed**: No immediate action required -- the Provectus practice-based taxonomy (agentic-engineering, sdlc, platform, devops, qa, backend, frontend, delivery, security, data, ml-ai, hr, sales, finance) is better suited for a consulting firm's organizational structure. However, consider adding secondary category tags from the agents repo taxonomy to improve cross-referencing. This would help when mapping upstream plugin updates to marketplace plugins.

### 13. Reference Auto-Claude PR Review and OOM Prevention Patterns

- **Source**: Auto-Claude develop branch (218 commits)
- **Affects plugins**: proagent-qa, proagent-devops
- **What changed**: Auto-Claude added structured PR review output, recovery mechanisms, terminal paste size capping, OOM/orphaned agent prevention, and Sentry integration for Python subprocesses. These are production hardening patterns for automated agent systems.
- **Action needed**:
  - **proagent-qa**: Consider documenting the structured PR review output format as a reference for automated code review workflows.
  - **proagent-devops**: Reference OOM prevention and orphaned agent cleanup patterns as operational best practices for running agent workloads in production.
  - Lower priority because these are internal Auto-Claude concerns, not directly reusable plugin content.

### 14. Add taches-cc-resources New Commands to Relevant Plugins

- **Source**: `taches-cc-resources` -- `setup-ralph` skill, `ask-me-questions` command
- **Affects plugins**: proagent-agentic-engineering, proagent-sdlc
- **What changed**: A `setup-ralph` skill for configuring autonomous coding loops and an `ask-me-questions` command for structured requirement gathering were added.
- **Action needed**:
  - **proagent-agentic-engineering**: Reference the `setup-ralph` pattern as an approach to bootstrapping autonomous agent loops.
  - **proagent-sdlc**: Reference `ask-me-questions` as a requirement gathering command pattern. This maps to the "Requirements Elicitation" phase of SDLC.
  - Note: These files were not found in the expected paths during analysis, which suggests they may have been added very recently or use different naming. Verify exact paths before incorporating.

### 15. Bump Marketplace Version and Update Statistics

- **Source**: All repo updates combined
- **Affects plugins**: `provectus-marketplace/marketplace.json`
- **What changed**: The upstream repos collectively added ~100 new assets (78 Composio skills, AWOS plugin with 20+ files, Agent Teams plugin, Python development updates, Tailwind v4 skill, Composio SDK with 28 rules).
- **Action needed**: After incorporating improvements, update:
  - `marketplace.json` version from `0.1.0` to `0.2.0`
  - `statistics.total_assets_cataloged` to reflect new asset count
  - `mcp_integrations_available` to include Composio/Rube
  - Individual plugin `assets_count` fields
  - Re-run `catalog/generate_catalog.py` to refresh `catalog.json` and `gaps.json`

---

## Implementation Priority Matrix

| Priority | Item | Effort | Impact | Plugins Affected |
|----------|------|--------|--------|-----------------|
| P0 | 1. Composio App Automations | High | Very High | 9 plugins |
| P0 | 2. Agent Teams Orchestration | Medium | High | 3 plugins |
| P0 | 3. AWOS 8-Step Workflow | Medium | High | 3 plugins |
| P1 | 4. Plugin.json Format Alignment | Low | Medium | 14 plugins |
| P1 | 5. Composio SDK for Agentic Eng | Medium | High | 2 plugins |
| P1 | 6. Python Development Updates | Low | Medium | 1 plugin |
| P1 | 7. Tailwind CSS v4 | Low | Medium | 1 plugin |
| P1 | 8. Mandatory Confirmation Pattern | Low | High | 3 plugins |
| P2 | 9. MCP Integration List Expansion | Low | Medium | All plugins |
| P2 | 10. Session Persistence Patterns | Low | Medium | 2 plugins |
| P2 | 11. YouTube Design Extractor | Low | Low | 1 plugin |
| P3 | 12. Category Taxonomy Alignment | Low | Low | Catalog only |
| P3 | 13. Auto-Claude Production Patterns | Low | Low | 2 plugins |
| P3 | 14. taches-cc New Commands | Low | Low | 2 plugins |
| P3 | 15. Version Bump and Statistics | Low | Medium | marketplace.json |

---

## Key Gaps Now Fillable

The upstream updates directly address several gaps identified in `catalog/gaps.json`:

| Practice | Previous Gap | Now Fillable Via |
|----------|-------------|-----------------|
| proagent-sales | Commands (need 3, have 2) | Composio: salesforce, hubspot, pipedrive automation |
| proagent-hr | Commands (need 3, have 0) | Composio: bamboohr, google-calendar, slack automation |
| proagent-finance | Commands (need 3, have 0) | Composio: stripe, square, shopify automation |
| proagent-delivery | Agent, Hooks, MCP | AWOS agents + Composio: jira, asana, linear automation |
| proagent-devops | MCP config | Composio: github, gitlab, datadog, sentry, pagerduty |
| proagent-frontend | Commands, Hooks, MCP | Composio: figma, canva automation + Tailwind v4 skill |
| proagent-backend | Commands, Hooks, MCP | Python dev updates + Composio: supabase, github |
| proagent-data | Commands, Hooks, MCP | Composio: googlesheets, airtable, amplitude, mixpanel |
| proagent-ml-ai | Commands, Hooks, MCP | Composio: github automation + agents repo ML plugins |
| proagent-platform | Agent, Hooks | AWOS context-engineering patterns + Composio: slack, notion |
