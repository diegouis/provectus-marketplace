# Provectus Practice Router Plugin

This plugin provides a single entry point (`/proagent`) that routes user requests to the appropriate Provectus practice specialist. Instead of remembering 15 different plugin commands, users describe what they need and the router handles dispatch.

## How It Works

1. User invokes `/proagent <request>`
2. Router analyzes the request to detect the domain (devops, ml-ai, security, etc.)
3. Router announces the detected practice
4. Router dispatches to the appropriate specialist agent via the Task tool
5. Specialist handles the request and returns results

## Routing Coverage

The router dispatches across all 15 Provectus practices:

- **agentic-engineering** — Agent systems, MCP servers, Claude extensions, plugins
- **sdlc** — Architecture, code review, releases, git workflows
- **platform** — Developer platforms, service catalogs, scaffolding
- **devops** — CI/CD, containers, IaC, monitoring, cloud ops
- **qa** — Test automation, E2E, coverage, accessibility
- **backend** — APIs, databases, microservices, auth
- **frontend** — React/Vue/Angular, design systems, components
- **delivery** — Sprint planning, estimation, status reports
- **security** — Vulnerability scanning, compliance, threat modeling
- **data** — ETL/ELT, dbt, Airflow, data quality
- **ml-ai** — Model training, MLOps, LLM apps, RAG
- **aws-ai** — Bedrock, AgentCore, AWS AI services
- **hr** — Hiring, onboarding, performance reviews, CV validation
- **sales** — Proposals, RFPs, competitive analysis
- **finance** — Budgeting, forecasting, P&L analysis

## Key Conventions

- Always announce the detected practice before dispatching
- When ambiguous, ask the user — never guess silently
- For cross-domain requests, identify primary and supporting practices
- Pass the full user context to specialist agents

## Plugin Structure

```
proagent-router/
  .claude-plugin/plugin.json
  skills/
    proagent-router/SKILL.md
  commands/proagent.md
  hooks/hooks.json
  CLAUDE.md
```
