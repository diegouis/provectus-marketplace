# Provectus Marketplace

Practice-specific plugins for Claude Code and Claude Desktop, built from 843 assets across 17 Provectus repositories.

## Plugins

| Plugin | Practice | Description |
|--------|----------|-------------|
| [proagent-agentic-engineering](plugins/proagent-agentic-engineering) | Agentic Engineering | AI agent systems, MCP servers, multi-agent orchestration, prompt engineering |
| [proagent-sdlc](plugins/proagent-sdlc) | SDLC | Architecture, code review, testing strategy, release management, git workflows |
| [proagent-platform](plugins/proagent-platform) | Platform | Service catalogs, golden paths, scaffolding, MCP development, DX optimization |
| [proagent-devops](plugins/proagent-devops) | DevOps | CI/CD, Docker/Kubernetes, Terraform/IaC, monitoring, incident response |
| [proagent-qa](plugins/proagent-qa) | QA | Test automation, Playwright/Cypress, regression testing, coverage, accessibility |
| [proagent-backend](plugins/proagent-backend) | Backend | APIs, databases, microservices, auth, caching, queues, performance |
| [proagent-frontend](plugins/proagent-frontend) | Frontend | React/Vue/Angular, design systems, WCAG 2.1 AA, responsive design |
| [proagent-delivery](plugins/proagent-delivery) | Delivery | Sprint planning, milestones, status reports, risk management, retrospectives |
| [proagent-security](plugins/proagent-security) | Security | Vulnerability scanning, compliance, secrets management, threat modeling, OWASP |
| [proagent-data](plugins/proagent-data) | Data | ETL/ELT, dbt, Airflow, data warehousing, SQL optimization, data quality |
| [proagent-ml-ai](plugins/proagent-ml-ai) | ML/AI | Model training, MLOps, experiment tracking, LLM apps, RAG, embeddings |
| [proagent-hr](plugins/proagent-hr) | HR | Hiring, interviews, onboarding, performance reviews, compensation |
| [proagent-sales](plugins/proagent-sales) | Sales | Proposals, RFPs, competitive analysis, lead research, pipeline management |
| [proagent-finance](plugins/proagent-finance) | Finance | Budgeting, invoicing, forecasting, P&L analysis, cost optimization |

## Installation

### Claude Code (CLI)

Install a single plugin from a local checkout:

```bash
claude plugin install ./plugins/proagent-devops
```

Or add plugins to your project's `.claude/settings.json` so they load automatically for the whole team:

```json
{
  "plugins": {
    "proagent-devops": {
      "source": "file:./provectus-marketplace/plugins/proagent-devops",
      "version": "0.2.0",
      "enabled": true
    },
    "proagent-backend": {
      "source": "file:./provectus-marketplace/plugins/proagent-backend",
      "version": "0.2.0",
      "enabled": true
    }
  }
}
```

### Claude Desktop

Each plugin's `.mcp.json` contains the MCP server configurations. Copy the servers you need into your Claude Desktop config:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

**Important notes for Claude Desktop:**

1. **Remote MCP servers** (Excalidraw, Rube) use `"url"` in `.mcp.json`, but Claude Desktop does not support the `url` format. Wrap them with `mcp-remote`:
   ```json
   {
     "excalidraw": {
       "command": "npx",
       "args": ["-y", "mcp-remote", "https://mcp.excalidraw.com/mcp"]
     }
   }
   ```

2. **Google Drive and Google Workspace** require OAuth authentication before they will connect. Run the auth flow first:
   - Google Drive: `npx -y @modelcontextprotocol/server-gdrive auth`
   - Google Workspace (`mcp-gsuite`): Requires `.accounts.json` and OAuth setup — see [mcp-gsuite docs](https://github.com/MarkusMaal/mcp-gsuite)

3. **GitLab** — If using a self-hosted GitLab instance (e.g., `gitlab.provectus.com`), update `GITLAB_API_URL` to point to your instance:
   ```json
   "GITLAB_API_URL": "https://gitlab.provectus.com/api/v4"
   ```
   The `GITLAB_PERSONAL_ACCESS_TOKEN` must be generated on that same instance (not `gitlab.com`).

4. **Skills, commands, agents, and hooks** are Claude Code (CLI) features only — they do not work in Claude Desktop. Desktop gets MCP server integrations. To use plugin knowledge in Desktop, paste the plugin's `CLAUDE.md` and `skills/*/SKILL.md` content into a Project's custom instructions.

5. **Edit the config while Claude Desktop is closed** — it may overwrite your changes on startup if edited while running.

## Plugin Anatomy

Every plugin follows the same structure:

```
proagent-<practice>/
├── .claude-plugin/
│   └── plugin.json          # Metadata: name, version, description, resources
├── skills/
│   └── <practice>-assistant/
│       └── SKILL.md          # Core skill — activates on trigger terms (includes Excalidraw diagramming)
├── commands/
│   ├── proagent-<practice>-hub.md    # /proagent-<practice>-hub — overview and routing
│   ├── proagent-<practice>-run.md    # /proagent-<practice>-run — execute workflows
│   └── proagent-<practice>-review.md # /proagent-<practice>-review — review artifacts
├── agents/
│   └── <practice>-specialist.md      # Specialist subagent for the practice domain
├── hooks/
│   └── hooks.json            # Lifecycle hooks: validation, formatting, notifications
├── .mcp.json                 # MCP servers (Slack, Google Drive, Gmail/Calendar, GitHub, and more)
├── CLAUDE.md                 # Context loaded into Claude sessions
└── README.md                 # Plugin-specific docs
```

### Components

| Component | What it does |
|-----------|-------------|
| **Skill** | Model-invoked capability that activates autonomously when Claude detects relevant trigger terms in the conversation |
| **Commands** | User-invoked slash commands (`/proagent-*-hub`, `/proagent-*-run`, `/proagent-*-review`) |
| **Agent** | Specialist subagent that can be dispatched via the Task tool for domain-specific work |
| **Hooks** | Shell commands that run on lifecycle events (PreToolUse, PostToolUse, SessionStart) for validation and automation |
| **MCP Servers** | External tool connections — GitHub, Slack, Google Drive, Gmail, Calendar, Rube (Composio), and more |

## MCP Integrations

Every plugin ships with a core set of MCP servers. Additional servers are included per practice where relevant.

### Core MCP Servers (all 14 plugins)

| Server | Package | What it provides |
|--------|---------|-----------------|
| **Slack** | `slack-mcp-server@latest` | Channels, messages, users, threads — full Slack workspace access via xoxc/xoxd auth |
| **Google Drive** | `@modelcontextprotocol/server-gdrive` | Drive file listing, search, read. Docs exported as Markdown, Sheets as CSV, Slides as text |
| **Google Workspace** | `mcp-gsuite` (via `uvx`) | Gmail (list, search, send, draft, modify) + Google Calendar (list, create, update, delete events) |
| **GitHub** | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions, code search |
| **Excalidraw** | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language |

### Additional MCP Servers (per practice)

| Server | Package | Plugins |
|--------|---------|---------|
| **GitLab** | `@modelcontextprotocol/server-gitlab` | agentic-engineering, sdlc, platform, devops, qa, backend, frontend, security |
| **Atlassian (Jira/Confluence)** | `@modelcontextprotocol/server-atlassian` | sdlc, qa, delivery |
| **Playwright** | `@playwright/mcp@latest` | agentic-engineering, qa, frontend |
| **Rube (Composio)** | `https://rube.app/mcp` | agentic-engineering, platform, devops, frontend, delivery, data, hr, sales, finance |

### Rube / Composio

Nine plugins include the [Rube](https://rube.app) MCP server, a universal SaaS automation gateway powered by Composio. It provides three tools:

| Tool | Purpose |
|------|---------|
| `RUBE_SEARCH_TOOLS` | Discover available actions for any connected app |
| `RUBE_MANAGE_CONNECTIONS` | Authenticate and manage SaaS connections |
| `RUBE_MULTI_EXECUTE_TOOL` | Execute actions across connected apps |

This gives plugins access to Salesforce, HubSpot, Stripe, BambooHR, Jira, Figma, and 200+ more SaaS apps without individual MCP server setup.

### Environment Variables

| Variable | Used by |
|----------|---------|
| `SLACK_MCP_XOXC_TOKEN` / `SLACK_MCP_XOXD_TOKEN` | Slack |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | GitHub |
| `GITLAB_PERSONAL_ACCESS_TOKEN` / `GITLAB_API_URL` | GitLab |
| `ATLASSIAN_API_TOKEN` / `ATLASSIAN_EMAIL` / `ATLASSIAN_DOMAIN` | Jira, Confluence |
| Google Drive uses OAuth browser flow (`gcp-oauth.keys.json`) | Google Drive |
| Google Workspace uses OAuth (`.gauth.json` + `.accounts.json`) | Gmail, Calendar |

## Key Features

### Agent Teams

Plugins for agentic-engineering, SDLC, and QA support multi-agent orchestration:

- **Multi-Reviewer Code Review** — Parallel agents evaluate correctness, performance, security, and maintainability simultaneously
- **Hypothesis-Driven Debugging** — Analysis of Competing Hypotheses (ACH) methodology with parallel evidence collection
- **Parallel Feature Development** — One-owner-per-file rule with concurrent implementation agents

### AWOS Workflow

The SDLC, delivery, and agentic-engineering plugins implement the 8-step specification-to-implementation pipeline:

1. Product Requirements → 2. Roadmap → 3. Architecture → 4. Spec → 5. Tech Spec → 6. Task Breakdown → 7. Implementation → 8. Verification

Each step requires explicit user confirmation before proceeding.

### Mandatory Confirmation Pattern

Destructive or high-impact operations always pause for user approval. Plugins for agentic-engineering, SDLC, and delivery enforce confirmation gates at key decision points.

## Statistics

| Metric | Count |
|--------|-------|
| Plugins | 14 |
| Skills | 15 |
| Commands | 42 |
| Agents | 20 |
| Hooks | 39 |
| MCP Servers (core) | 5 (Slack, Google Drive, Google Workspace, GitHub, Excalidraw) |
| MCP Servers (additional) | 4 (GitLab, Atlassian, Playwright, Rube) |
| MCP Integrations | 31 |
| Source Assets | 843 |
| Source Repos | 17 |

## Project Structure

```
provectus-marketplace/
├── marketplace.json       # Marketplace manifest with all plugin metadata
├── plugins/               # 14 practice plugins
│   ├── proagent-agentic-engineering/
│   ├── proagent-sdlc/
│   ├── proagent-platform/
│   ├── proagent-devops/
│   ├── proagent-qa/
│   ├── proagent-backend/
│   ├── proagent-frontend/
│   ├── proagent-delivery/
│   ├── proagent-security/
│   ├── proagent-data/
│   ├── proagent-ml-ai/
│   ├── proagent-hr/
│   ├── proagent-sales/
│   └── proagent-finance/
├── catalog/               # Asset catalog from repo scanning
└── scan-reports/          # Raw scan reports per repo batch
```

## License

MIT
