# Provectus Asset Catalog Summary

**Generated:** 2026-02-16
**Total Assets:** ~843 (deduplicated across all repos)
**Source Repos:** 19 (14 primary + 5 workspace/config repos)
**Practices Covered:** 14/14

## Asset Type Distribution

| Type | Count |
|------|-------|
| skills | ~148 |
| commands | ~97 |
| agents | ~32 |
| hooks | ~18 |
| mcp_configs | 3 |
| scripts | ~297 |
| docs | ~142 |
| templates | ~67 |
| configs | ~139 |

## Reuse Potential Distribution

| Rating | Count | Percentage |
|--------|-------|------------|
| high | ~573 | 68% |
| medium | ~219 | 26% |
| low | ~51 | 6% |

## Per-Practice Overview

| Practice | Plugin | Readiness | Skills | Cmds | Agents | Hooks | MCP | Total | High Reuse | Key Gaps |
|----------|--------|-----------|--------|------|--------|-------|-----|-------|------------|----------|
| agentic-engineering | proagent-agentic-engineering | ready | 92 | 68 | 25 | 15 | 3 | 612 | 445 | None |
| delivery | proagent-delivery | ready | 10 | 16 | 0 | 0 | 0 | 52 | 42 | Agent, Hooks, MCP |
| sales | proagent-sales | ready | 5 | 2 | 1 | 0 | 0 | 13 | 8 | Cmds <3, Hooks, MCP |
| hr | proagent-hr | ready | 8 | 0 | 1 | 0 | 0 | 22 | 14 | Cmds, Hooks, MCP |
| finance | proagent-finance | ready | 2 | 0 | 1 | 0 | 0 | 4 | 2 | Cmds, Hooks, MCP |
| devops | proagent-devops | ready | 8 | 8 | 5 | 2 | 0 | 126 | 89 | MCP |
| frontend | proagent-frontend | ready | 14 | 0 | 2 | 0 | 0 | 60 | 34 | Cmds, Hooks, MCP |
| backend | proagent-backend | ready | 10 | 1 | 5 | 0 | 0 | 63 | 42 | Cmds, Hooks, MCP |
| sdlc | proagent-sdlc | ready | 24 | 42 | 5 | 6 | 0 | 208 | 157 | MCP |
| data | proagent-data | ready | 7 | 0 | 3 | 0 | 0 | 27 | 20 | Cmds, Hooks, MCP |
| ml-ai | proagent-ml-ai | ready | 9 | 1 | 1 | 0 | 0 | 22 | 18 | Cmds, Hooks, MCP |
| security | proagent-security | ready | 4 | 3 | 1 | 2 | 0 | 51 | 37 | MCP |
| platform | proagent-platform | ready | 14 | 5 | 0 | 0 | 1 | 127 | 80 | Agent, Hooks |
| qa | proagent-qa | ready | 13 | 14 | 5 | 3 | 1 | 110 | 80 | None |

## Gap Analysis Summary

| Practice | Readiness | Missing Components |
|----------|-----------|-------------------|
| agentic-engineering | ready | None - complete |
| delivery | ready | Agent definition; Hook definitions; MCP config |
| sales | ready | Commands (need 3, have 2); Hook definitions; MCP config |
| hr | ready | Commands (need 3, have 0); Hook definitions; MCP config |
| finance | ready | Commands (need 3, have 0); Hook definitions; MCP config |
| devops | ready | MCP config |
| frontend | ready | Commands (need 3, have 0); Hook definitions; MCP config |
| backend | ready | Commands (need 3, have 1); Hook definitions; MCP config |
| sdlc | ready | MCP config |
| data | ready | Commands (need 3, have 0); Hook definitions; MCP config |
| ml-ai | ready | Commands (need 3, have 1); Hook definitions; MCP config |
| security | ready | MCP config |
| platform | ready | Agent definition; Hook definitions |
| qa | ready | None - complete |

## Practices Fully Ready for Plugin Generation

These practices have skills + commands and can be generated immediately:
1. **agentic-engineering** - 612 assets, fully complete
2. **qa** - 110 assets, fully complete
3. **sdlc** - 208 assets, only missing MCP
4. **devops** - 126 assets, only missing MCP
5. **security** - 51 assets, only missing MCP
6. **delivery** - 52 assets, needs agent/hooks/MCP generation

## Practices Needing Component Generation

These practices have skills but need commands, hooks, and/or MCP configs generated:
1. **frontend** - 60 assets, strong skills but no commands
2. **backend** - 63 assets, strong skills but only 1 command
3. **data** - 27 assets, good skills but no commands
4. **ml-ai** - 22 assets, strong ML skills but only 1 command
5. **hr** - 22 assets, good skills but no commands
6. **sales** - 13 assets, decent skills but only 2 commands
7. **finance** - 4 assets, minimal - needs heavy generation
8. **platform** - 127 assets, no agent definition

## Source Repository Contribution Matrix

| Repo | Total Assets | Key Practices |
|------|-------------|---------------|
| ralph-orchestrator | 100 | agentic-engineering, sdlc, qa, devops |
| proagent | 91 | ALL 14 practices covered |
| tac | 90 | agentic-engineering, sdlc, qa, devops |
| casdk-harness | 85 | agentic-engineering, devops, platform, backend |
| proagent-repo GUI | 79 | agentic-engineering, sdlc, security, devops |
| skills (Anthropic) | 72 | agentic-engineering, platform, frontend, qa |
| gastown | 69 | agentic-engineering, sdlc, devops |
| planning-with-files | 59 | agentic-engineering, sdlc |
| taches-cc-resources | 55 | agentic-engineering, sdlc, delivery |
| claude-ui | 53 | frontend, backend, security |
| superpowers | 51 | agentic-engineering, sdlc, qa |
| awos | 49 | agentic-engineering, sdlc, delivery |
| Auto-Claude | 40 | devops, sdlc, security, qa |
| awesome-claude-skills | 36 | agentic-engineering (30+ skills) |
| agents (wshobson) | 31 | ALL major practices (72 plugins) |
| awesome-claude-code | 20 | agentic-engineering, devops |
| specs | 11 | agentic-engineering, platform |
| root-claude-config | 3 | agentic-engineering, sdlc |
| root-setup | 1 | devops, platform |

## Detailed Practice Breakdown

### agentic-engineering (proagent-agentic-engineering)

**Readiness:** ready
**Source Repos:** All 19 repos contribute
**Recommended Integrations:** GitHub, GitLab, Slack, Confluence

This is the foundational practice with the largest asset pool. Key high-value assets:

**skills (92):**
- [high] `awesome-claude-skills` - 30+ skills (artifacts-builder, changelog-generator, connect-apps, document-skills, skill-creator, etc.)
- [high] `casdk-harness` - 12 skills (api-development, code-review, debugging, documentation, git-workflow, testing-strategies, plugin skills)
- [high] `planning-with-files` - 17 IDE-specific skill definitions
- [high] `ralph-orchestrator` - 12 skills (code-assist, pdd, eval, tui-validate, etc.)
- [high] `proagent-repo GUI` - 14 TAC skills (adw, core-four, autonomy, trust-ladder, etc.)
- [high] `superpowers` - 13 skills (brainstorming, writing-plans, TDD, systematic-debugging, SDD, etc.)
- [high] `taches-cc-resources` - 2 skills (create-agent-skills, create-hooks)
- [high] `skills` (Anthropic) - 16+ skills (docx, pdf, pptx, xlsx, canvas, MCP builder, etc.)

**commands (68):**
- [high] `awos` - 16 commands (product, roadmap, architecture, spec, tech, tasks, implement, verify + Claude wrappers)
- [high] `tac` - 22+ commands across tac-2 through tac-6
- [high] `taches-cc-resources` - 27 commands (meta-prompting, research, mental frameworks)
- [high] `superpowers` - 3 commands (brainstorm, write-plan, execute-plan)
- [high] `casdk-harness` - 2 commands (create-agent, research)

**agents (25):**
- [high] `casdk-harness` - 17 agents (Python/TS/React/Go/Node experts, DB experts, infra engineers, SDET)
- [high] `superpowers` - 2 agents (code-reviewer)
- [high] `taches-cc-resources` - 3 agents (auditors)
- [high] `ralph-orchestrator` - 1 agent (code-assist)
- [high] `awos` - 1 agent (doc-writer)

### delivery (proagent-delivery)

**Readiness:** ready (skills + commands present)
**Source Repos:** awos, proagent, taches-cc-resources, awesome-claude-skills, ralph-orchestrator, skills, specs
**Recommended Integrations:** Jira, Slack, Google Meet, Google Calendar, Confluence, Google Docs

**skills (10):** meeting-facilitation, spec-creation, risk-assessment, status-reporting, stakeholder-management, internal-comms, find-code-tasks, agentic-kpis, and others
**commands (16):** product, roadmap, weekly-standup, add-to-todos, check-todos, plus mental framework commands (pareto, first-principles, etc.)
**templates (5):** product-definition, roadmap, project-charter, 3p-updates

### sales (proagent-sales)

**Readiness:** ready (skills present)
**Source Repos:** awesome-claude-skills, proagent, skills, taches-cc-resources, agents
**Recommended Integrations:** Slack, Google Docs, Gmail, Google Calendar, Jira

**skills (5):** competitive-ads-extractor, domain-name-brainstormer, lead-research-assistant, brand-guidelines, stakeholder-management
**commands (2):** competitive research, options analysis
**agents (1):** sales-automator

### hr (proagent-hr)

**Readiness:** ready (skills present)
**Source Repos:** awesome-claude-skills, proagent, skills, agents, specs
**Recommended Integrations:** Slack, Google Docs, Gmail, Google Calendar, Google Meet

**skills (8):** developer-growth-analysis, meeting-insights-analyzer, tailored-resume-generator, onboarding-coordination, interview-process, performance-review, internal-comms
**agents (1):** hr-pro
**templates (4):** company-newsletter, faq-answers, 3p-updates, general-comms

### finance (proagent-finance)

**Readiness:** ready (has skills)
**Source Repos:** awesome-claude-skills, agents
**Recommended Integrations:** Google Docs, Gmail, Slack

**skills (2):** invoice-organizer, stripe-integration
**agents (1):** quant-analyst
**Note:** This is the smallest practice - needs significant generation of commands, hooks, and MCP configs

### devops (proagent-devops)

**Readiness:** ready
**Source Repos:** Auto-Claude, casdk-harness, gastown, proagent, ralph-orchestrator, tac, agents, and more
**Recommended Integrations:** GitHub, GitLab, AWS, GCP, Slack, Jira

**skills (8):** cicd-pipeline, kubernetes-orchestration, docker-containerization, cloud-architecture, postmortem-writing, github-actions-templates, using-git-worktrees, release-bump
**commands (8):** deploy, start, install, incident-response presets
**agents (5):** docker-engineer, k8s-engineer, gcp-architect, gitlab-ci-expert, kubernetes-architect
**configs (50+):** CI/CD workflows, Docker Compose configs, Prometheus/Grafana configs

### frontend (proagent-frontend)

**Readiness:** ready (strong skills)
**Source Repos:** Auto-Claude, awesome-claude-skills, casdk-harness, claude-ui, proagent, skills, agents
**Recommended Integrations:** GitHub, GitLab, Playwright, Pencil, Excalidraw

**skills (14):** component-design, state-management, responsive-design, artifacts-builder, brand-guidelines, canvas-design, theme-factory, frontend-design, web-artifacts-builder, algorithmic-art, WCAG audit
**agents (2):** dev-typescript-expert, dev-react-expert
**templates (10+):** React components (Avatar, Badge, Button, Card), theme definitions

### backend (proagent-backend)

**Readiness:** ready (strong skills + agents)
**Source Repos:** casdk-harness, claude-ui, proagent, agents, skills, specs
**Recommended Integrations:** GitHub, GitLab, AWS, GCP

**skills (10):** api-design, database-schema, security-hardening, performance-optimization, code-review, debugging, api-development, api-design-principles, mcp-builder
**commands (1):** api-scaffold
**agents (5):** dev-python-expert, dev-go-expert, dev-nodejs-expert, backend-architect, python-pro

### sdlc (proagent-sdlc)

**Readiness:** ready
**Source Repos:** Nearly all repos contribute
**Recommended Integrations:** GitHub, GitLab, Jira, Confluence, Slack

**skills (24):** changelog-generator, code-review, debugging, documentation, git-workflow, planning-with-files, brainstorming, writing-plans, executing-plans, SDD, TDD, systematic-debugging, verification, code-assist, codebase-summary, pdd, code-task-generator
**commands (42):** architecture, spec, tech, tasks, implement, verify, bug, chore, feature, commit, pull_request, classify_issue, document, review, debug, create-plan, run-plan, and many more
**agents (5):** dev-code-review-expert, dev-refactor-agent, conductor, code-reviewer

### data (proagent-data)

**Readiness:** ready (skills present)
**Source Repos:** awesome-claude-skills, casdk-harness, claude-ui, proagent, tac, agents, specs
**Recommended Integrations:** AWS, GCP, GitHub, Google Docs

**skills (7):** xlsx, data-visualization, exploratory-data-analysis, statistical-analysis, feature-engineering, dbt-transformation-patterns, database-schema
**agents (3):** db-postgres-expert, db-sql-expert, business-analyst

### ml-ai (proagent-ml-ai)

**Readiness:** ready (skills present)
**Source Repos:** awesome-claude-skills, proagent, tac, agents, specs
**Recommended Integrations:** AWS, GCP, GitHub, Google Docs

**skills (9):** model-training, feature-engineering, model-selection, hyperparameter-tuning, model-evaluation, experiment-tracking, model-deployment, langsmith-fetch
**commands (1):** train-model
**agents (1):** llm-architect
**templates (1):** ml-project-starter

### security (proagent-security)

**Readiness:** ready
**Source Repos:** Auto-Claude, casdk-harness, gastown, proagent-repo GUI, tac, agents, and more
**Recommended Integrations:** GitHub, GitLab, AWS, GCP, Slack

**skills (4):** security-hardening, trust-ladder, adversarial-review preset
**commands (3):** cmd_zte, e2e/test_sql_injection, evaluate-repository
**agents (1):** security-auditor
**hooks (2):** pre-commit with vulnerability detection
**configs (12+):** CodeQL, Bandit, dependabot, VirusTotal scanning, ZTE configs

### platform (proagent-platform)

**Readiness:** ready
**Source Repos:** Nearly all repos contribute
**Recommended Integrations:** GitHub, GitLab, Slack, AWS, GCP

**skills (14):** connect-apps, file-organizer, skill-creator, template-skill, skill-share, system-design, cloud-architecture, architecture-documentation, maturity-model, templating, docx, pdf, pptx, xlsx
**commands (5):** skill_create, setup-statusline
**mcp (1):** Google Drive MCP server
**scripts (30+):** CLI tools, installer scripts, integrations (Slack, GitHub, GitLab, Google Drive)

### qa (proagent-qa)

**Readiness:** ready (fully complete)
**Source Repos:** Multiple repos contribute
**Recommended Integrations:** GitHub, GitLab, Playwright, Jira, Slack

**skills (13):** webapp-testing, automated-testing, e2e-testing, api-testing, testing-strategies, TDD, verification-before-completion, validation-pyramid, tui-validate, evaluate-presets, eval
**commands (14):** verify, test, test_e2e, resolve_failed_test, resolve_failed_e2e_test, tdd-cycle, audit-skill, audit-slash-command, audit-subagent, verify-behaviors, update-behaviors
**agents (5):** test-sdet-expert, skill-auditor, slash-command-auditor, subagent-auditor
**hooks (3):** pre-commit with lint+test, Cursor hooks
**mcp (1):** Playwright MCP for E2E testing

## Key Findings

1. **All 14 practices have at least 1 skill** - Every practice qualifies as "ready" for the skills criterion
2. **Only 2 practices are fully complete** (agentic-engineering, qa) with all 5 component types
3. **MCP configs are the biggest gap** - Only 3 MCP configs exist across all practices
4. **Hooks are the second biggest gap** - Only 6 practices have hooks
5. **Commands need generation for 7 practices** - hr, finance, frontend, data, ml-ai need commands built
6. **68% of assets are high-reuse** - Strong foundation for plugin generation
7. **proagent repo is the most cross-cutting** - Covers all 14 practices
8. **The `agents` repo (wshobson) has 72 pre-built plugins** - Massive reuse opportunity

## Recommended Generation Priority

1. **Phase 1 - Low effort:** devops, sdlc, security (only need MCP configs)
2. **Phase 2 - Medium effort:** delivery, platform (need agent/hooks generation)
3. **Phase 3 - Higher effort:** frontend, backend, data, ml-ai (need commands + hooks + MCP)
4. **Phase 4 - Highest effort:** hr, sales, finance (need most component types generated)
