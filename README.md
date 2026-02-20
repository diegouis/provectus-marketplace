# Provectus Marketplace

Practice-specific plugins for Claude Code and Claude Desktop, built from 867 assets across 16 Provectus repositories.

## Plugins

| Plugin | Practice | Description |
|--------|----------|-------------|
| [proagent-agentic-engineering](plugins/proagent-agentic-engineering) | Agentic Engineering | AI agent systems, MCP servers, multi-agent orchestration, autonomous coding loops, context engineering |
| [proagent-sdlc](plugins/proagent-sdlc) | SDLC | Architecture, code review, debugging, ADRs, C4 diagrams, release management, PITER framework |
| [proagent-platform](plugins/proagent-platform) | Platform | Service catalogs, golden paths, scaffolding, document generation, plugin lifecycle, DX |
| [proagent-devops](plugins/proagent-devops) | DevOps | CI/CD, Docker/Kubernetes, Terraform/IaC, secrets management, GitOps, cloud cost optimization |
| [proagent-qa](plugins/proagent-qa) | QA | Test automation, TDD, LLM judge evaluation, Playwright, mock/replay backends, coverage |
| [proagent-backend](plugins/proagent-backend) | Backend | APIs, databases, microservices, CQRS/event sourcing, MCP server development, auth |
| [proagent-frontend](plugins/proagent-frontend) | Frontend | React/Vue/Angular, design systems, canvas design, WCAG 2.1 AA, theme factory |
| [proagent-delivery](plugins/proagent-delivery) | Delivery | Sprint planning, standup notes, PRD creation, internal comms, agentic KPIs, ROM estimation |
| [proagent-security](plugins/proagent-security) | Security | Vulnerability scanning, agent sandboxing, risk classification, threat modeling, OWASP, audit workflows |
| [proagent-data](plugins/proagent-data) | Data | ETL/ELT, dbt, Airflow, business analytics, bioinformatics pipelines, SQL optimization |
| [proagent-ml-ai](plugins/proagent-ml-ai) | ML/AI | Model training, knowledge graphs, meta-prompting, LLM judge, RAG, AWS Bedrock |
| [proagent-hr](plugins/proagent-hr) | HR | Hiring, CV validation, GDPR compliance, resume generation, growth analysis, onboarding |
| [proagent-sales](plugins/proagent-sales) | Sales | Proposals, sales automation, content marketing, business cases, market opportunity analysis |
| [proagent-documentation](plugins/proagent-documentation) | Documentation | Repo analysis, doc generation (README/architecture/API/onboarding/runbook), Confluence publishing and sync |
| [proagent-finance](plugins/proagent-finance) | Finance | Budgeting, cloud FinOps, financial projections, Stripe/PCI, budget variance analysis |

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
      "version": "0.3.0",
      "enabled": true
    },
    "proagent-backend": {
      "source": "file:./provectus-marketplace/plugins/proagent-backend",
      "version": "0.3.0",
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

### Core MCP Servers (all 15 plugins)

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
| **GitLab** | `@modelcontextprotocol/server-gitlab` | agentic-engineering, sdlc, platform, devops, qa, backend, frontend, security, documentation |
| **Atlassian (Jira/Confluence)** | `@modelcontextprotocol/server-atlassian` | sdlc, qa, delivery, documentation |
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
| Plugins | 15 |
| Skills | 16 |
| Commands | 45 |
| Agents | 23 |
| Hooks | 43 |
| MCP Servers (core) | 5 (Slack, Google Drive, Google Workspace, GitHub, Excalidraw) |
| MCP Servers (additional) | 4 (GitLab, Atlassian, Playwright, Rube) |
| MCP Integrations | 37 |
| Source Assets | 867 |
| Source Repos | 16 |
| Marketplace Version | 0.3.0 |

## Project Structure

```
provectus-marketplace/
├── marketplace.json       # Marketplace manifest with all plugin metadata
├── plugins/               # 15 practice plugins
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
│   ├── proagent-finance/
│   └── proagent-documentation/
├── catalog/               # Asset catalog from repo scanning
└── scan-reports/          # Raw scan reports per repo batch
```

## License

MIT
