---
name: finance-assistant
description: Use when managing financial operations -- budgeting, invoicing, revenue forecasting, P&L analysis, cost optimization, billing workflows, and financial reporting
---

# Managing Financial Operations

## Overview

This skill orchestrates financial operations across budgeting, invoicing, forecasting, P&L analysis, revenue tracking, cost optimization, billing, and financial reporting. It draws on proven patterns from awesome-claude-skills/invoice-organizer (automated invoice processing and document organization), agents/stripe-integration (payment processing, subscription billing, and webhook-driven financial workflows), and agents/quant-analyst (financial modeling, risk metrics, and time series forecasting).

**Announce at start:** "I'm using the proagent-finance:finance-assistant skill to manage this financial operation."

## When to Use

- Creating or updating project, department, or company budgets
- Generating, organizing, or reconciling invoices and receipts
- Forecasting revenue using historical data and growth models
- Analyzing profit and loss statements across time periods
- Tracking revenue streams and identifying trends
- Optimizing costs by analyzing spending patterns and vendor contracts
- Setting up or managing billing and payment processing workflows
- Producing financial reports for stakeholders, audits, or compliance

## Capabilities

### 1. Budgeting

Build structured budgets with line-item detail, category allocation, and variance tracking. Follows a collaborative approach: review historical spending, identify cost centers, propose allocations, and confirm with stakeholders before finalizing.

**Key steps:**
- Gather historical spending data from invoices, bank statements, or accounting exports
- Identify cost categories: personnel, software/tools, infrastructure, professional services, travel, office, marketing
- Propose allocations based on historical patterns and planned initiatives
- Build monthly/quarterly/annual budget spreadsheet with formulas
- Set up variance tracking: budget vs. actual with percentage deviation
- Flag line items exceeding threshold (default: 10% over budget)

**Budget document structure:**
```
budget-YYYY.csv / budget-YYYY.xlsx
├── Summary (total budget, allocated, remaining)
├── By Category (personnel, software, infra, services, travel, office, marketing)
├── By Month (Jan-Dec columns with actuals overlay)
├── Variance Analysis (budget vs. actual, % deviation, trend)
└── Notes (assumptions, planned changes, risk items)
```

### 2. Invoicing

Automates invoice generation, organization, and reconciliation. Draws directly on the awesome-claude-skills/invoice-organizer pattern for reading, extracting, renaming, and sorting financial documents.

**Invoice generation:**
- Create professional invoices from project data, time entries, or deliverables
- Include: invoice number (sequential), date, due date, client details, line items, subtotal, tax, total
- Support multiple currencies with exchange rate notation
- Generate in Markdown, CSV, or structured JSON for accounting system import

**Invoice organization (from invoice-organizer):**
- Scan folders for invoice files (PDF, images, documents)
- Extract key fields: vendor, invoice number, date, amount, description, payment method
- Rename to standardized format: `YYYY-MM-DD Vendor - Invoice - Description.ext`
- Sort into logical folder structure: by vendor, category, time period, or tax category
- Generate summary CSV with all invoice details for accountant handoff

**Reconciliation:**
- Match invoices against bank statements or payment records
- Identify unmatched transactions (missing invoices or unrecorded payments)
- Flag duplicate invoices by comparing vendor, amount, and date proximity
- Produce reconciliation report with matched, unmatched, and duplicate lists

### 3. Revenue Forecasting

Project future revenue using historical data, growth rates, and scenario modeling. Applies quantitative analysis patterns from agents/quant-analyst for time series analysis and statistical forecasting.

**Forecasting methods:**
- **Linear trend:** Fit a linear regression to historical monthly revenue data
- **Moving average:** Apply 3-month, 6-month, or 12-month moving averages to smooth seasonality
- **Growth rate projection:** Calculate compound monthly growth rate (CMGR) and project forward
- **Scenario modeling:** Build best-case, base-case, and worst-case projections with explicit assumptions

**Key steps:**
1. Collect historical revenue data (minimum 6 months, ideally 12-24 months)
2. Clean and validate data: remove one-time anomalies, adjust for seasonality
3. Calculate baseline metrics: average monthly revenue, growth rate, standard deviation
4. Apply forecasting model appropriate to data characteristics
5. Generate 3-month, 6-month, and 12-month projections
6. Present confidence intervals based on historical variance
7. Document assumptions and sensitivity to key variables

**Output format:**
```
Revenue Forecast - [Period]
├── Historical Summary (trailing 12-month revenue, MoM growth, avg monthly)
├── Projections (3/6/12 month with confidence bands)
├── Scenario Analysis (best/base/worst with assumptions)
├── Key Drivers (top revenue sources, growth contributors)
└── Risks (concentration risk, churn, market factors)
```

### 4. P&L Analysis

Produce and analyze profit and loss statements with structured breakdowns, margin calculations, and period-over-period comparisons.

**P&L structure:**
```
Revenue
  - Product/Service Revenue (by line)
  - Recurring Revenue (subscriptions, retainers)
  - One-time Revenue (projects, consulting)
  = Total Revenue

Cost of Goods Sold (COGS)
  - Direct Labor
  - Infrastructure Costs
  - Third-party Services
  = Gross Profit (Revenue - COGS)
  = Gross Margin %

Operating Expenses (OpEx)
  - Personnel (salaries, benefits, contractors)
  - Software & Tools
  - Office & Facilities
  - Marketing & Sales
  - Professional Services (legal, accounting)
  - Travel & Entertainment
  = Total OpEx

  = Operating Income (Gross Profit - OpEx)
  = Operating Margin %

Other Income/Expenses
  - Interest, taxes, depreciation
  = Net Income
  = Net Margin %
```

**Analysis dimensions:**
- Period-over-period comparison (MoM, QoQ, YoY)
- Category breakdown with percentage of revenue
- Margin trend analysis (gross, operating, net)
- Expense ratio monitoring (OpEx as % of revenue)
- Contribution margin by product line or client

### 5. Revenue Tracking

Monitor revenue streams in real time with structured dashboards and alerts.

**Tracking dimensions:**
- By source: product lines, service lines, client accounts
- By type: recurring (MRR/ARR), one-time, usage-based
- By period: daily, weekly, monthly, quarterly, annual
- By status: invoiced, collected, outstanding, overdue

**Key metrics:**
- Monthly Recurring Revenue (MRR) and Annual Recurring Revenue (ARR)
- Net Revenue Retention (NRR): expansion minus churn
- Average Revenue Per Account (ARPA)
- Revenue concentration: top-10 client dependency percentage
- Days Sales Outstanding (DSO): average collection time
- Revenue growth rate (MoM, QoQ, YoY)

### 6. Cost Optimization

Analyze spending patterns, identify savings opportunities, and recommend optimizations.

**Analysis approach:**
1. Categorize all expenses by type, vendor, and department
2. Calculate cost trends (increasing, stable, decreasing) per category
3. Benchmark against industry standards or internal targets
4. Identify optimization opportunities:
   - Underutilized software licenses (usage < 50% of seats)
   - Duplicate or overlapping tool subscriptions
   - Vendor consolidation opportunities (3+ vendors in same category)
   - Contract renegotiation candidates (approaching renewal, above-market rates)
   - Infrastructure right-sizing (over-provisioned cloud resources)
5. Quantify potential savings per recommendation
6. Prioritize by effort-to-impact ratio

**Output:** Cost optimization report with ranked recommendations, estimated savings, implementation effort, and timeline.

### 7. Billing and Payment Processing

Manage billing workflows and payment integrations. Draws on agents/stripe-integration for payment processing patterns including checkout flows, subscription management, webhook handling, and refund processing.

**Billing workflows:**
- Generate billing schedules from contracts (monthly, quarterly, milestone-based)
- Track payment status: pending, sent, paid, overdue, disputed
- Automate payment reminders at configurable intervals (7 days, 14 days, 30 days overdue)
- Handle partial payments and payment plan installments
- Process refunds with audit trail and reason codes

**Payment integration patterns (from stripe-integration):**
- Checkout session creation for one-time and recurring payments
- Subscription lifecycle management (create, upgrade, downgrade, cancel)
- Webhook event handling for payment confirmation and failure notification
- Customer payment method management
- PCI-compliant payment flows using hosted checkout or Payment Intents
- Idempotent webhook processing to prevent duplicate transactions

**Stripe webhook events to handle:**
- `payment_intent.succeeded` -- Mark invoice as paid, trigger fulfillment
- `payment_intent.payment_failed` -- Notify finance team, flag invoice
- `customer.subscription.updated` -- Update billing records
- `customer.subscription.deleted` -- Process cancellation, adjust MRR
- `invoice.payment_succeeded` -- Record recurring payment
- `charge.refunded` -- Update ledger, adjust revenue

### 8. Financial Reporting

Generate structured financial reports for stakeholders, board meetings, audits, and compliance.

**Report types:**
- **Executive summary:** High-level KPIs (revenue, margins, cash position, burn rate)
- **Monthly financial report:** P&L, balance sheet highlights, cash flow summary, key variances
- **Budget vs. actual:** Variance analysis by category with explanations for material deviations
- **Revenue report:** By source, by client, by product line, with trend analysis
- **Expense report:** By category, by department, with optimization recommendations
- **Cash flow projection:** Operating, investing, financing activities with 90-day outlook
- **Accounts receivable aging:** Current, 30-day, 60-day, 90-day+ buckets with collection risk assessment

**Report format:**
- Structured Markdown tables for readability
- CSV export for accounting software import
- Key metrics highlighted with trend indicators (up/down/flat vs. prior period)
- Executive summary section at top with 3-5 key takeaways
- Appendix with methodology notes and data sources

## Integration Points

- **Google Docs:** Budget documents, financial reports, P&L statements shared with stakeholders
- **Gmail:** Invoice delivery, payment reminders, financial report distribution, overdue notices
- **Slack:** Budget alerts, payment notifications, revenue milestone announcements, expense approvals
- **Stripe:** Payment processing, subscription billing, webhook-driven payment status updates
- **Accounting software:** CSV/JSON export compatible with QuickBooks, Xero, FreshBooks

## Composio App Automations

This plugin integrates with Composio-powered SaaS automation skills via the Rube MCP server. These skills connect to real external services for end-to-end workflow automation.

### Available Automations

| Skill | Service | Key Capabilities |
|-------|---------|-----------------|
| stripe-automation | Stripe | Payment processing, subscription management, invoice generation, refund handling |
| square-automation | Square | Point-of-sale transactions, inventory management, payment processing, reporting |
| shopify-automation | Shopify | Order management, product catalog, payment tracking, storefront operations |

### Usage Pattern

All Composio automations follow a three-step workflow:

1. **Discover tools**: Use `RUBE_SEARCH_TOOLS` with a use case description to find available tools and their schemas
2. **Connect service**: Use `RUBE_MANAGE_CONNECTIONS` to activate the toolkit connection (handles OAuth automatically)
3. **Execute actions**: Use `RUBE_MULTI_EXECUTE_TOOL` with the discovered tool slug and schema-compliant arguments

### Configuration

Add the Rube MCP server to your `.mcp.json`:
```json
"rube": {
  "url": "https://rube.app/mcp"
}
```

Source: `awesome-claude-skills` Composio app automation skills

## Workflow Summary

```
Budget Planning --> Invoice Management --> Revenue Tracking --> P&L Analysis --> Reporting
      |                    |                     |                   |              |
      v                    v                     v                   v              v
  Allocate by       Generate/organize      Track MRR/ARR       Margin analysis  Executive
  category with     invoices, reconcile    by source and        cost ratios      summaries
  variance gates    against payments       type, flag churn     period compare   and forecasts
```
