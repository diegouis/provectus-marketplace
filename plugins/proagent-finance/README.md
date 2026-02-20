# proagent-finance

A Claude Code plugin for comprehensive financial operations management. Covers budgeting, invoicing, revenue forecasting, P&L analysis, cost optimization, cloud FinOps, payment processing (Stripe, PCI compliance), financial projections, budget variance analysis, billing workflows, and financial reporting. Incorporates assets from 3 source repos: `agents`, `awesome-claude-skills`, and `provectus-marketplace`.

**Version:** 0.3.0
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

**Build financial projections:**
```
/proagent-finance-run financial-projections
```
Build forward-looking financial models for startups and growth-stage companies: revenue projections (bottom-up and top-down), expense models (headcount-driven), cash flow projections with runway calculation, unit economics (CAC, LTV, payback period), and break-even analysis. Based on patterns from the `agents` repo `plugins/startup-business-analyst/commands/financial-projections.md`.

**Optimize cloud costs (FinOps):**
```
/proagent-finance-run cloud-cost-optimization
```
Analyze cloud infrastructure spending across AWS, GCP, and Azure. Identifies idle resources, right-sizing opportunities, reserved instance coverage gaps, storage tier optimization, and orphaned resources. Produces prioritized recommendations with estimated savings. Based on patterns from the `agents` repo `plugins/cloud-infrastructure/skills/cost-optimization/SKILL.md`.

**Check financial health:**
```
/proagent-finance-review financial-health
```
Runs a comprehensive assessment across profitability (gross/operating/net margins), liquidity (cash position, burn rate, runway), growth (revenue growth, MRR/ARR, churn), and risk (concentration, dependency, seasonal vulnerability). Outputs a scored dashboard with action items.

**Review budget variances:**
```
/proagent-finance-review budget-variance
```
Compares actuals against budget with threshold-based classification (on track, warning, critical). Includes run-rate projections to predict budget exhaustion, reallocation recommendations from under-budget to over-budget categories, and root cause analysis for material variances.

**Review budget completeness:**
```
/proagent-finance-review budgets
```
Loads current budget and actual spending data, calculates variances per category, flags items exceeding warning (10%) and critical (20%) thresholds, and assesses allocations against industry benchmarks.

## Components

| Component | Name | Purpose |
|-----------|------|---------|
| Skill | `proagent-finance:finance-assistant` | Core skill covering all financial operations (11 capabilities) |
| Command | `proagent-finance-hub` | Command hub and routing |
| Command | `proagent-finance-run` | Execute financial workflows (7 modes) |
| Command | `proagent-finance-review` | Financial reviews and assessments (5 modes) |
| Agent | `proagent-finance:finance-specialist` | Subagent for analysis, projections, FinOps, and report generation |
| Hook | Financial document validation | Invoice fields, budget categories, report structure |
| Hook | Invoice naming validation | Standardized filename convention enforcement |
| Hook | Post-report summary | Severity-coded findings and budget overrun escalation |

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| Rube | `rube.app/mcp` | SaaS automation gateway (Stripe, Square, Shopify, etc.) |

Set the environment variables for the services your team uses. Unused servers will not be started.

### External Asset Sources

This plugin integrates patterns from assets discovered across the Provectus ecosystem (14 total assets from 3 repos):

| Source Repo | Asset | Integrated As |
|-------------|-------|---------------|
| `agents` | `plugins/cloud-infrastructure/skills/cost-optimization/SKILL.md` | Cloud FinOps capability + `cloud-cost-optimization` run mode |
| `agents` | `plugins/payment-processing/skills/stripe-integration/SKILL.md` | Stripe integration patterns in billing capability |
| `agents` | `plugins/payment-processing/skills/pci-compliance/SKILL.md` | PCI compliance guidance in billing capability |
| `agents` | `plugins/startup-business-analyst/commands/financial-projections.md` | Financial projections capability + `financial-projections` run mode |
| `awesome-claude-skills` | `invoice-organizer/SKILL.md` | Invoice organization patterns in invoicing capability |

