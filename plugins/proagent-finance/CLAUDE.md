# ProAgent Finance Plugin

This plugin provides comprehensive financial operations management for Claude Code. It was synthesized from open-source repositories including awesome-claude-skills (invoice-organizer), agents (stripe-integration, quant-analyst), and Provectus finance practice patterns.

## Plugin Structure

```
proagent-finance/
├── .claude-plugin/plugin.json    # Plugin manifest (name, version, category)
├── mcp.json                      # MCP server configs (Google Docs, Gmail, Slack)
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
Use the `proagent-finance:finance-assistant` skill when managing any financial operation. It covers budgeting, invoicing, revenue forecasting, P&L analysis, revenue tracking, cost optimization, billing workflows, and financial reporting.

### Commands
- `/proagent-finance-hub` -- See all available commands and choose the right workflow
- `/proagent-finance-run <mode>` -- Execute a workflow (create-budget, forecast-revenue, analyze-costs, generate-invoice, financial-report)
- `/proagent-finance-review <type>` -- Run a financial review (budgets, forecasts, cost-structures, financial-health)

### Agent
The `proagent-finance:finance-specialist` agent can be dispatched as a subagent for financial analysis, invoice processing, budget variance tracking, and report generation. It produces structured reports with findings categorized by severity (CRITICAL, WARNING, NOTE).

### Hooks
Three hooks enforce financial document quality:
1. **Document validation:** Ensures invoices contain all required fields (number, date, client, line items, totals), budgets cover standard categories with contingency, and financial reports include executive summaries with date references
2. **Invoice naming:** Validates that invoice files follow the standardized naming convention (YYYY-MM-DD Vendor - Invoice - Description.ext) based on the invoice-organizer pattern
3. **Post-report summary:** After the finance-specialist agent completes analysis, formats findings as a severity-coded summary with key metrics and escalates critical budget overruns

### MCP Servers
Configure the following environment variables to enable integrations:
- `GOOGLE_APPLICATION_CREDENTIALS` / `GOOGLE_DOCS_OAUTH_TOKEN` -- Google Docs for financial document collaboration (budgets, reports, P&L statements)
- `GMAIL_OAUTH_TOKEN` -- Gmail for invoice delivery, payment reminders, and report distribution
- `SLACK_BOT_TOKEN` / `SLACK_TEAM_ID` -- Slack for real-time financial alerts (budget thresholds, payment confirmations, overdue escalations)

## Source Attribution

Key patterns and content were drawn from:
- **awesome-claude-skills/invoice-organizer** -- Invoice scanning, data extraction, standardized naming (YYYY-MM-DD Vendor - Invoice - Description.ext), folder organization by vendor/category/date, CSV summary generation for accounting handoff
- **agents/stripe-integration** -- Payment processing patterns (checkout sessions, subscription management, webhook handling), PCI-compliant payment flows, idempotent transaction processing, refund handling with audit trails
- **agents/quant-analyst** -- Quantitative analysis methodology (time series analysis, statistical forecasting), risk metrics (VaR concepts adapted to revenue risk), data quality validation practices, scenario modeling with sensitivity analysis
