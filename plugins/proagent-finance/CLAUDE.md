# ProAgent Finance Plugin

This plugin provides comprehensive financial operations management for Claude Code.

## Plugin Structure

```
proagent-finance/
├── .claude-plugin/plugin.json    # Plugin manifest (name, version, category)
├── .mcp.json                     # MCP server configs (Slack, Google Drive, GitHub)
├── skills/
│   └── finance-assistant/SKILL.md # Core skill: Managing Financial Operations
├── commands/
│   ├── proagent-finance-hub.md    # Command hub: list and route to finance commands
│   ├── proagent-finance-run.md    # Execute: create-budget, forecast-revenue, analyze-costs, generate-invoice, financial-report
│   └── proagent-finance-review.md # Review: budgets, forecasts, cost-structures, financial-health
├── agents/
│   └── finance-specialist.md      # Finance specialist subagent for analysis and reporting
├── hooks/
│   └── hooks.json                 # Financial document validation, invoice naming, post-report summaries
├── CLAUDE.md                      # This file
└── README.md                      # User-facing documentation
```

## Usage

### Skill
Use the `proagent-finance:finance-assistant` skill when managing any financial operation. It covers budgeting, invoicing, revenue forecasting, P&L analysis, revenue tracking, cost optimization, cloud FinOps, payment processing (Stripe integration, PCI compliance), billing workflows, financial projections, and financial reporting.

### Commands
- `/proagent-finance-hub` -- See all available commands and choose the right workflow
- `/proagent-finance-run <mode>` -- Execute a workflow (create-budget, forecast-revenue, analyze-costs, generate-invoice, financial-report, financial-projections, cloud-cost-optimization)
- `/proagent-finance-review <type>` -- Run a financial review (budgets, forecasts, cost-structures, financial-health, budget-variance)

### Agent
The `proagent-finance:finance-specialist` agent can be dispatched as a subagent for financial analysis, invoice processing, budget variance tracking, cloud cost allocation analysis, payment processing integration (Stripe, PCI compliance), financial projections, and report generation. It produces structured reports with findings categorized by severity (CRITICAL, WARNING, NOTE).

### Hooks
Three hooks enforce financial document quality:
1. **Document validation:** Ensures invoices contain all required fields (number, date, client, line items, totals), budgets cover standard categories with contingency, and financial reports include executive summaries with date references
2. **Invoice naming:** Validates that invoice files follow the standardized naming convention (YYYY-MM-DD Vendor - Invoice - Description.ext) based on the invoice-organizer pattern
3. **Post-report summary:** After the finance-specialist agent completes analysis, formats findings as a severity-coded summary with key metrics and escalates critical budget overruns

### MCP Servers

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **Rube (Composio)**: SaaS automation gateway providing access to Stripe, Square, and Shopify via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

### External Asset References

This plugin incorporates patterns and techniques from these discovered assets across the Provectus ecosystem:

| Source Repo | Asset Path | Capability |
|-------------|-----------|------------|
| `agents` | `plugins/cloud-infrastructure/skills/cost-optimization/SKILL.md` | Cloud cost optimization and FinOps patterns |
| `agents` | `plugins/payment-processing/skills/stripe-integration/SKILL.md` | Stripe payment integration workflows |
| `agents` | `plugins/payment-processing/skills/pci-compliance/SKILL.md` | PCI compliance for payment processing |
| `agents` | `plugins/startup-business-analyst/commands/financial-projections.md` | Financial projections generation |
| `awesome-claude-skills` | `invoice-organizer/SKILL.md` | Invoice organization and processing |

