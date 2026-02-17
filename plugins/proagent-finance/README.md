# proagent-finance

A Claude Code plugin for comprehensive financial operations management. Covers budgeting, invoicing, revenue forecasting, P&L analysis, cost optimization, billing workflows, and financial reporting.

**Version:** 0.1.0
**Category:** Finance
**License:** MIT

## Installation

Copy the `proagent-finance` directory into your Claude Code plugins directory, or reference it from your project's `.claude/plugins/` configuration.

## Quick Start

Run `/proagent-finance-hub` to see all available commands and pick the right workflow for your task.

### Common Workflows

**Create a project budget:**
```
/proagent-finance-run create-budget
```
Interactively build a budget with category allocations based on historical spending data. The agent works through each cost category (personnel, software, infrastructure, services, travel, office, marketing, contingency), proposes allocations with conservative/moderate/aggressive options, and sets up variance tracking thresholds.

**Forecast next quarter's revenue:**
```
/proagent-finance-run forecast-revenue
```
Analyzes historical revenue data, applies appropriate forecasting methods (linear trend, growth rate projection, or moving average with seasonal adjustment), and builds best-case/base-case/worst-case scenario projections with explicit assumptions and confidence intervals.

**Find cost savings:**
```
/proagent-finance-run analyze-costs
```
Scans expense data, categorizes spending, identifies trends, and produces a prioritized optimization report covering software license audits, vendor consolidation, contract renegotiation, and infrastructure right-sizing with estimated savings per recommendation.

**Generate and organize invoices:**
```
/proagent-finance-run generate-invoice
```
Create new invoices with professional formatting and sequential numbering, organize existing invoice files using standardized naming (YYYY-MM-DD Vendor - Invoice - Description.ext), or reconcile invoices against payment records to identify unpaid and unmatched transactions.

**Produce a P&L statement:**
```
/proagent-finance-run financial-report pnl
```
Generates a structured profit and loss statement with revenue segmentation, COGS, gross margin, operating expenses, and net income. Includes period-over-period comparison and margin trend analysis.

**Check financial health:**
```
/proagent-finance-review financial-health
```
Runs a comprehensive assessment across profitability (gross/operating/net margins), liquidity (cash position, burn rate, runway), growth (revenue growth, MRR/ARR, churn), and risk (concentration, dependency, seasonal vulnerability). Outputs a scored dashboard with action items.

**Review budget variances:**
```
/proagent-finance-review budgets
```
Loads current budget and actual spending data, calculates variances per category, flags items exceeding warning (10%) and critical (20%) thresholds, and assesses allocations against industry benchmarks.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | `proagent-finance:finance-assistant` | Core skill covering all financial operations |
| Command | `proagent-finance-hub` | Command hub and routing |
| Command | `proagent-finance-run` | Execute financial workflows (5 modes) |
| Command | `proagent-finance-review` | Financial reviews and assessments (4 modes) |
| Agent | `proagent-finance:finance-specialist` | Subagent for analysis and report generation |
| Hook | Financial document validation | Invoice fields, budget categories, report structure |
| Hook | Invoice naming validation | Standardized filename convention enforcement |
| Hook | Post-report summary | Severity-coded findings and budget overrun escalation |

## MCP Integrations

The plugin ships with MCP server configurations for:

| Server | Purpose | Required Environment Variable |
|--------|---------|-------------------------------|
| Google Docs | Budget documents, financial reports, P&L statements | `GOOGLE_APPLICATION_CREDENTIALS`, `GOOGLE_DOCS_OAUTH_TOKEN` |
| Gmail | Invoice delivery, payment reminders, report distribution | `GOOGLE_APPLICATION_CREDENTIALS`, `GMAIL_OAUTH_TOKEN` |
| Slack | Budget alerts, payment notifications, overdue escalations | `SLACK_BOT_TOKEN`, `SLACK_TEAM_ID` |

Set the environment variables for the services your team uses. Unused servers will not be started.

## Source Repositories

This plugin synthesizes patterns and content from open-source repositories:

- **awesome-claude-skills/invoice-organizer** -- Automated invoice scanning and extraction, standardized file naming (YYYY-MM-DD Vendor - Invoice - Description.ext), multi-format support (PDF, images, documents), folder organization by vendor/category/date/tax-category, CSV summary generation for accounting software import
- **agents/stripe-integration** -- Payment processing patterns (checkout sessions, Payment Intents, subscription lifecycle), webhook event handling (payment_intent.succeeded, customer.subscription.updated, charge.refunded), PCI-compliant payment flows, customer management, refund processing with audit trails, idempotent webhook processing
- **agents/quant-analyst** -- Quantitative financial analysis methodology, time series forecasting, risk metrics and portfolio concepts adapted for business revenue analysis, data quality validation, scenario modeling with sensitivity analysis, statistical methods using pandas/numpy/scipy patterns
