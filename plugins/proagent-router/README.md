# proagent-router

Single entry point (`/proagent`) that routes user requests to the appropriate Provectus practice specialist. Instead of remembering 16 different plugin commands, users describe what they need and the router handles dispatch.

## Installation

### Option 1: Copy to your project

```bash
cp -r proagent-router/ /path/to/your-project/.claude/plugins/proagent-router/
```

### Option 2: Reference from the marketplace

```json
{
  "plugins": ["proagent-router"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-router /path/to/your-project/.claude/plugins/proagent-router
```

## Usage

```
/proagent <describe what you need>
```

### Examples

```
/proagent set up a CI/CD pipeline for our Node.js app
/proagent train a classification model on this dataset
/proagent write E2E tests for the checkout flow
/proagent review this PR for security issues
/proagent build a REST API for user management
/proagent set up Slack credentials
/proagent create a budget forecast for Q2
```

## How Routing Works

1. **Parse** — Analyze the request to identify what the user wants and which domain it falls under
2. **Match** — Map keywords, artifacts, and intent to the best practice from the routing table
3. **Announce** — Tell the user which practice is being dispatched to and why
4. **Dispatch** — Use the Task tool to invoke the appropriate specialist agent
5. **Return** — Present the specialist's response to the user

## Available Practices

| Practice | What It Handles |
|----------|----------------|
| **Agentic Engineering** | Claude Code extensions, MCP servers, multi-agent workflows, plugins |
| **SDLC** | Architecture, code review, testing strategy, releases, git workflows |
| **Platform** | Developer platforms, service catalogs, golden paths, scaffolding |
| **DevOps** | CI/CD, Docker, Kubernetes, Terraform, monitoring, cloud ops |
| **QA** | Test automation, Playwright, Cypress, coverage, E2E, accessibility |
| **Backend** | APIs, databases, microservices, auth, caching, queues |
| **Frontend** | React, Vue, Angular, design systems, responsive design, components |
| **Delivery** | Sprint planning, milestones, estimation, status reports, retrospectives |
| **Security** | Vulnerability scanning, compliance, secrets, threat modeling, OWASP |
| **Data** | ETL/ELT, dbt, Airflow, data warehousing, SQL, data quality |
| **ML/AI** | Model training, MLOps, experiment tracking, LLM apps, RAG, embeddings |
| **AWS AI** | Amazon Bedrock, AgentCore, AWS AI services, CDK, Knowledge Bases |
| **HR** | Hiring, interviews, onboarding, performance reviews, CV validation |
| **Sales** | Proposals, RFPs, competitive analysis, lead research, pipeline management |
| **Finance** | Budgeting, invoicing, forecasting, P&L analysis, cost optimization |
| **Connector Setup** | MCP credential configuration, Slack tokens, Google Drive OAuth |

## Component Inventory

| Component | Path | Purpose |
|-----------|------|---------|
| Plugin manifest | `.claude-plugin/plugin.json` | Name, version, description |
| MCP config | `.mcp.json` | Empty — router dispatches, not consumes |
| Core skill | `skills/proagent-router/SKILL.md` | Routing table, dispatch logic, ambiguity handling |
| Command | `commands/proagent.md` | `/proagent` slash command |
| Hooks | `hooks/hooks.json` | Lifecycle hooks |

## Version

- Plugin version: 0.2.0
- Category: router
- Author: Provectus
