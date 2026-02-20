---
name: finance-assistant
description: Use when managing financial operations -- budgeting, invoicing, revenue forecasting, P&L analysis, cost optimization, cloud FinOps, payment processing (Stripe, PCI compliance), financial projections, billing workflows, and financial reporting
---

# Managing Financial Operations

## Overview

This skill orchestrates financial operations across budgeting, invoicing, forecasting, P&L analysis, revenue tracking, cost optimization, cloud FinOps, payment processing (Stripe integration, PCI compliance), financial projections, billing, and financial reporting. It incorporates patterns from the `agents` repo (cloud-infrastructure cost-optimization, payment-processing stripe-integration and pci-compliance skills, startup-business-analyst financial-projections) and the `awesome-claude-skills` repo (invoice-organizer).

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
- Building financial projections for startups and growth-stage companies
- Analyzing and optimizing cloud infrastructure costs (FinOps)
- Allocating cloud costs across teams, projects, and business units
- Integrating Stripe payment processing with PCI-compliant workflows
- Running budget variance analysis with threshold-based alerts

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

Automates invoice generation, organization, and reconciliation. Invoice organization follows patterns from the `awesome-claude-skills` repo `invoice-organizer/SKILL.md`.

**Invoice generation:**
- Create professional invoices from project data, time entries, or deliverables
- Include: invoice number (sequential), date, due date, client details, line items, subtotal, tax, total
- Support multiple currencies with exchange rate notation
- Generate in Markdown, CSV, or structured JSON for accounting system import

**Invoice organization:**
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

Project future revenue using historical data, growth rates, and scenario modeling.

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

### 7. Cloud Cost Optimization (FinOps)

Analyze and optimize cloud infrastructure spending using patterns from the `agents` repo `plugins/cloud-infrastructure/skills/cost-optimization/SKILL.md`.

**Cloud cost analysis approach:**
1. Inventory cloud resources across providers (AWS, GCP, Azure)
2. Map costs to teams, projects, and business units using tagging and cost allocation
3. Identify idle and underutilized resources (instances, storage, databases)
4. Evaluate reserved instance and savings plan coverage vs. on-demand spend
5. Analyze data transfer costs and cross-region traffic patterns
6. Review storage tier optimization (hot vs. warm vs. cold vs. archive)
7. Assess containerized workload efficiency (right-sizing pods, node utilization)

**Cost allocation dimensions:**
- By team or department (engineering, data, ML, platform)
- By project or product line
- By environment (production, staging, development, sandbox)
- By service category (compute, storage, networking, database, ML/AI)

**Optimization levers:**
- Reserved instances / savings plans for predictable baseline workloads
- Spot/preemptible instances for fault-tolerant batch processing
- Auto-scaling policies tuned to actual demand patterns
- Storage lifecycle policies (auto-tier to cheaper storage classes)
- Right-sizing recommendations based on CPU/memory utilization metrics
- Cleanup of orphaned resources (unattached EBS volumes, stale snapshots, unused Elastic IPs)

**Output:** Cloud cost optimization report with per-resource savings estimates, implementation priority, and projected monthly/annual savings.

### 8. Financial Projections

Build forward-looking financial models for startups and growth-stage companies using patterns from the `agents` repo `plugins/startup-business-analyst/commands/financial-projections.md`.

**Projection types:**
- **Revenue projections:** Bottom-up (units x price) and top-down (TAM x capture rate) models
- **Expense projections:** Hiring plan-driven personnel costs, infrastructure scaling models, marketing spend curves
- **Cash flow projections:** Monthly cash in/out with runway calculation and fundraising trigger points
- **Unit economics:** CAC, LTV, LTV/CAC ratio, payback period projections over time
- **Break-even analysis:** Fixed and variable cost modeling to determine revenue threshold for profitability

**Key steps:**
1. Define projection horizon (typically 12-36 months for startups, 12 months for growth-stage)
2. Build revenue model: pricing tiers, expected customer acquisition, expansion revenue, churn assumptions
3. Build expense model: headcount plan, infrastructure scaling, vendor costs, marketing budget
4. Calculate monthly cash flow: net burn rate, cash runway, funding milestones
5. Sensitivity analysis: test impact of varying growth rate, churn, and hiring pace
6. Present investor-ready output with assumptions clearly documented

**Output format:**
```
Financial Projections - [Company] - [Period]
├── Revenue Model (by stream, monthly/quarterly)
├── Expense Model (by category, headcount-driven)
├── Cash Flow Projection (monthly, cumulative)
├── Unit Economics (CAC, LTV, payback, margins)
├── Break-Even Analysis (months to profitability)
├── Sensitivity Matrix (key variable impacts)
└── Assumptions Log (all inputs documented)
```

### 9. Budget Variance Analysis

Dedicated budget variance tracking and analysis with automated alerting thresholds.

**Variance analysis workflow:**
1. Load current budget allocations and actual spending data
2. Calculate variance per line item: absolute ($) and relative (%)
3. Apply threshold classification:
   - **On track:** Within 10% of allocation (favorable or neutral)
   - **Warning:** 10-20% over allocation -- flag for review
   - **Critical:** Over 20% -- requires immediate action and approval
4. Calculate year-to-date cumulative budget utilization per category
5. Project run-rate to period end: will current spending rate exhaust the budget?
6. Identify categories consistently under budget (reallocation opportunity)
7. Generate variance report with drill-down by category, department, and month

**Automated alerts:**
- Weekly: summary of any categories approaching warning threshold
- Monthly: full variance report with trend analysis
- Immediate: notification when any category crosses critical threshold (20%+ over)

**Output:** Budget variance report with color-coded status per category, run-rate projections, reallocation recommendations, and escalation items.

### 10. Billing and Payment Processing (Stripe, PCI Compliance)

Manage billing workflows and payment integrations. Incorporates Stripe integration patterns from the `agents` repo `plugins/payment-processing/skills/stripe-integration/SKILL.md` and PCI compliance guidance from `plugins/payment-processing/skills/pci-compliance/SKILL.md`.

**Billing workflows:**
- Generate billing schedules from contracts (monthly, quarterly, milestone-based)
- Track payment status: pending, sent, paid, overdue, disputed
- Automate payment reminders at configurable intervals (7 days, 14 days, 30 days overdue)
- Handle partial payments and payment plan installments
- Process refunds with audit trail and reason codes

**Payment integration patterns:**
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

**PCI compliance requirements:**
- Never store raw card numbers, CVV, or magnetic stripe data in application databases
- Use Stripe Elements, Checkout, or Payment Intents for client-side card collection (tokenization)
- Enforce HTTPS/TLS for all payment-related API communication
- Implement webhook signature verification (`Stripe-Signature` header) to prevent spoofed events
- Log payment events with masked card details (last 4 digits only) for audit trails
- Maintain SAQ-A or SAQ-A-EP compliance scope when using hosted payment pages
- Review PCI DSS requirements annually and document compliance controls

### 11. Financial Reporting

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
- **Stripe:** Payment processing, subscription billing, webhook-driven payment status updates (per `agents` repo stripe-integration and pci-compliance patterns)
- **Cloud providers (AWS, GCP, Azure):** Cost Explorer, Billing APIs, and tagging for cloud cost allocation and FinOps (per `agents` repo cost-optimization patterns)
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

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- Financial workflow and approval chain diagrams
- Budget allocation and cost flow visualizations
- Reporting pipeline and data aggregation maps
- Invoice processing and payment flow diagrams

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details


## Workflow Summary

```
Budget Planning --> Invoice Management --> Revenue Tracking --> P&L Analysis --> Reporting
      |                    |                     |                   |              |
      v                    v                     v                   v              v
  Allocate by       Generate/organize      Track MRR/ARR       Margin analysis  Executive
  category with     invoices, reconcile    by source and        cost ratios      summaries
  variance gates    against payments       type, flag churn     period compare   and forecasts

Cloud FinOps -----> Financial Projections --> Budget Variance --> Payment Processing
      |                    |                     |                   |
      v                    v                     v                   v
  Cloud cost         Revenue/expense        Threshold-based     Stripe integration
  allocation by      models, break-even     alerts, run-rate    PCI compliance
  team/project       unit economics         projections         webhook automation
```
