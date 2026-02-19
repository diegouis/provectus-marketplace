---
description: "Execute a financial workflow: create-budget, forecast-revenue, analyze-costs, generate-invoice, or financial-report"
argument-hint: "<mode>"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# ProAgent Finance Run

You are the financial operations execution engine for the proagent-finance plugin. Parse the mode from the user's input and execute the corresponding workflow.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word or hyphenated phrase of `$ARGUMENTS` to determine the mode. If no mode is provided, ask the user to choose: `create-budget`, `forecast-revenue`, `analyze-costs`, `generate-invoice`, or `financial-report`.

---

## Mode: create-budget

Create or update a budget with structured category allocations and variance tracking.

**Announce:** "Starting budget creation workflow. I'll work through budget categories with you, using historical data where available."

### Process

1. **Gather context:**
   - Ask for the budget scope: project, department, or company-wide
   - Ask for the budget period: monthly, quarterly, or annual
   - Look for historical spending data: prior budgets, invoice summaries, bank statements, accounting exports
   - If historical data exists, calculate baseline spending per category

2. **Define categories:**
   - Personnel: salaries, benefits, contractors, bonuses
   - Software & Tools: licenses, SaaS subscriptions, development tools
   - Infrastructure: cloud hosting, servers, networking, storage
   - Professional Services: legal, accounting, consulting, auditing
   - Marketing & Sales: advertising, events, collateral, CRM
   - Travel & Entertainment: flights, hotels, meals, client entertainment
   - Office & Facilities: rent, utilities, supplies, equipment
   - Contingency: reserve for unplanned expenses (recommend 5-10% of total)

3. **Propose allocations:**
   - For each category, propose an allocation based on historical spending, planned initiatives, and industry benchmarks
   - Present alternatives: conservative (10% below baseline), moderate (at baseline), aggressive (10% above for growth areas)
   - Wait for user confirmation per category before proceeding
   - Example: "Based on your last 12 months of software spending ($4,200/month average), I recommend a monthly allocation of $4,500 to accommodate the planned Datadog addition. Conservative option: $4,000 (requires cutting one subscription). Which do you prefer?"

4. **Build budget document:**
   - Create structured CSV or Markdown table with monthly columns
   - Include summary row with totals
   - Add variance tracking columns: budget, actual, variance ($), variance (%)
   - Include assumptions section documenting rationale for each allocation

5. **Set up variance alerts:**
   - Define threshold for each category (default: 10% over budget triggers warning, 20% triggers escalation)
   - Document approval workflow for over-budget items
   - Create template for monthly budget review check-in

6. **Finalize:**
   - Save budget document to appropriate location
   - Present summary: total budget, top 3 categories by allocation, contingency amount
   - Suggest next step: "Budget created. Set a monthly reminder to run `/proagent-finance-review budgets` for variance tracking."

---

## Mode: forecast-revenue

Project future revenue using historical data, growth models, and scenario analysis.

**Announce:** "Starting revenue forecast. I'll analyze historical revenue data and build projections with scenario modeling."

### Process

1. **Collect historical data:**
   - Look for revenue records: invoices, payment logs, accounting exports, CRM data
   - Minimum requirement: 6 months of monthly revenue data (12-24 months preferred)
   - Parse and validate: remove duplicates, handle missing months, flag anomalies
   - Segment by revenue type: recurring (subscriptions, retainers), one-time (projects, consulting), usage-based

2. **Calculate baseline metrics:**
   - Average monthly revenue (trailing 3, 6, and 12 months)
   - Month-over-month growth rate (individual and compound)
   - Revenue standard deviation (volatility measure)
   - Seasonality index: compare each month to annual average to detect seasonal patterns
   - Revenue concentration: percentage from top 1, 3, 5, and 10 clients

3. **Apply forecasting models:**

   **Linear trend analysis:**
   - Fit linear regression: Revenue = a + b * month_number
   - Calculate R-squared to assess fit quality
   - Project forward using the trend line
   - Best for: stable businesses with consistent growth

   **Compound growth projection:**
   - Calculate CMGR (Compound Monthly Growth Rate): (end_revenue / start_revenue)^(1/months) - 1
   - Project forward: future_revenue = current * (1 + CMGR)^months
   - Best for: growing businesses with accelerating revenue

   **Moving average with seasonality:**
   - Calculate 12-month moving average for trend
   - Compute seasonal indices per month
   - Project: trend_value * seasonal_index
   - Best for: businesses with clear seasonal patterns

4. **Build scenario models:**
   - **Best case:** Higher growth rate assumption, new client wins, expansion revenue
   - **Base case:** Current trajectory with moderate assumptions
   - **Worst case:** Client churn, market downturn, delayed deals
   - Document explicit assumptions for each scenario
   - Calculate probability-weighted expected value

5. **Generate forecast report:**
   ```
   ## Revenue Forecast: [Period]

   ### Historical Performance
   | Metric | Value |
   |--------|-------|
   | Trailing 12-month revenue | $X |
   | Average monthly revenue | $X |
   | MoM growth rate | X% |
   | Revenue volatility (std dev) | $X |

   ### Projections
   | Period | Best Case | Base Case | Worst Case |
   |--------|-----------|-----------|------------|
   | 3 months | $X | $X | $X |
   | 6 months | $X | $X | $X |
   | 12 months | $X | $X | $X |

   ### Key Assumptions
   - [assumption 1]
   - [assumption 2]

   ### Risks and Sensitivities
   - [risk 1 with impact quantification]
   ```

6. **Present and save:**
   - Save forecast document
   - Highlight key insight: "At current growth rate, you'll cross $X ARR by [date]"
   - Recommend review cadence: monthly for high-growth, quarterly for stable businesses

---

## Mode: analyze-costs

Analyze spending patterns, identify savings opportunities, and recommend optimizations.

**Announce:** "Starting cost analysis. I'll categorize expenses, identify trends, and find optimization opportunities."

### Process

1. **Gather expense data:**
   - Locate expense records: invoices, bank statements, accounting exports, receipt folders
   - Use the invoice-organizer pattern to scan and extract data from invoice files if needed
   - Parse into structured format: date, vendor, amount, category, description

2. **Categorize and aggregate:**
   - Auto-categorize expenses into standard categories (software, infrastructure, personnel, services, travel, office, marketing)
   - Calculate totals per category: monthly, quarterly, annual
   - Calculate percentage of total spend per category
   - Identify top 10 vendors by total spend

3. **Trend analysis:**
   - Calculate MoM change per category
   - Flag categories with >15% increase over trailing 3-month average
   - Identify seasonal spending patterns
   - Compute cost-per-employee and cost-per-revenue-dollar ratios

4. **Identify optimization opportunities:**

   **Software license audit:**
   - List all software subscriptions with cost and seat count
   - Flag underutilized licenses (ask about usage if data not available)
   - Identify overlapping tools (e.g., multiple project management tools, multiple CI/CD tools)
   - Calculate potential savings from consolidation or tier downgrades

   **Vendor consolidation:**
   - Group vendors by category
   - Flag categories with 3+ vendors (consolidation opportunity)
   - Estimate volume discount potential from consolidation

   **Contract renegotiation:**
   - Identify contracts approaching renewal (within 90 days)
   - Flag contracts with above-market rates (compare against known benchmarks)
   - Calculate leverage: total spend with vendor, contract duration, switching cost

   **Infrastructure right-sizing:**
   - Review cloud spending patterns for over-provisioning signals
   - Flag resources with consistently low utilization
   - Calculate potential savings from reserved instances or committed use discounts

5. **Generate optimization report:**
   ```
   ## Cost Optimization Report

   ### Spending Summary
   | Category | Monthly | Annual | % of Total | Trend |
   |----------|---------|--------|------------|-------|

   ### Top Recommendations
   | # | Recommendation | Est. Savings | Effort | Priority |
   |---|---------------|--------------|--------|----------|
   | 1 | [specific action] | $X/month | Low/Med/High | High |

   ### Quick Wins (< 1 week to implement)
   - [action with savings]

   ### Medium-Term (1-4 weeks)
   - [action with savings]

   ### Strategic (1-3 months)
   - [action with savings]

   ### Total Potential Savings: $X/month ($X/year)
   ```

---

## Mode: generate-invoice

Create, organize, or reconcile invoices.

**Announce:** "Starting invoice workflow. I'll help you generate new invoices or organize existing ones."

### Process

1. **Determine sub-mode:**
   - If user says "create" or "generate": enter Invoice Creation mode
   - If user says "organize" or "sort": enter Invoice Organization mode (follows invoice-organizer pattern)
   - If user says "reconcile" or "match": enter Reconciliation mode
   - If unclear, ask: "Would you like to (1) create a new invoice, (2) organize existing invoices, or (3) reconcile invoices against payments?"

2. **Invoice Creation:**
   - Collect required fields: client name, client address, invoice date, due date (default: Net 30), line items
   - For each line item: description, quantity, unit price, total
   - Calculate subtotal, tax (ask for applicable rate), total
   - Generate sequential invoice number: `INV-YYYY-NNNN`
   - Produce invoice in Markdown format with professional layout:
     ```
     # INVOICE

     **From:** [Your Company]
     **To:** [Client Name and Address]

     **Invoice #:** INV-2026-0001
     **Date:** 2026-02-16
     **Due Date:** 2026-03-18

     | Description | Qty | Unit Price | Total |
     |-------------|-----|------------|-------|
     | [item 1]    | 1   | $X,XXX.00  | $X,XXX.00 |

     **Subtotal:** $X,XXX.00
     **Tax (X%):** $XXX.00
     **Total Due:** $X,XXX.00

     **Payment Terms:** Net 30
     **Payment Methods:** [Bank transfer / Stripe / Check]
     ```
   - Save to `invoices/YYYY-MM-DD Client - Invoice - INV-YYYY-NNNN.md`

3. **Invoice Organization:**
   - Scan the target folder for invoice files (PDF, JPG, PNG, documents)
   - For each file, extract: vendor/company name, invoice number, date, amount, description
   - Rename to standardized format: `YYYY-MM-DD Vendor - Invoice - Description.ext`
   - Sort into folder structure based on user preference (by vendor, category, date, or tax category)
   - Generate summary CSV: Date, Vendor, Invoice Number, Description, Amount, Category, File Path
   - Present completion summary: files processed, date range, total amount, vendors identified

4. **Reconciliation:**
   - Load invoice records and payment records (bank statements, payment processor exports)
   - Match invoices to payments by amount and date proximity (within configurable window, default 5 business days)
   - Identify: matched (invoice + payment found), unpaid (invoice without payment), unmatched payment (payment without invoice)
   - Flag potential duplicates: same vendor + same amount within 7 days
   - Generate reconciliation report:
     ```
     ## Invoice Reconciliation Report

     ### Summary
     - Matched: X invoices ($X total)
     - Unpaid: X invoices ($X outstanding)
     - Unmatched payments: X ($X total)
     - Potential duplicates: X

     ### Unpaid Invoices (Action Required)
     | Invoice # | Vendor | Amount | Date | Days Overdue |
     |-----------|--------|--------|------|-------------|

     ### Unmatched Payments (Needs Investigation)
     | Payment Date | Amount | Source | Notes |
     |-------------|--------|--------|-------|
     ```

---

## Mode: financial-report

Produce structured financial reports for stakeholders.

**Announce:** "Starting financial report generation. I'll analyze your financial data and produce a structured report."

### Process

1. **Determine report type:**
   - If specified in arguments, use that type
   - Otherwise ask: "What type of report do you need? Options: `pnl` (profit & loss), `budget-vs-actual`, `revenue`, `expenses`, `cash-flow`, `executive-summary`, `ar-aging` (accounts receivable aging)"

2. **P&L Report:**
   - Gather revenue data (invoices, payment records) and expense data (bills, receipts, payroll)
   - Structure into standard P&L format: Revenue, COGS, Gross Profit, OpEx, Operating Income, Net Income
   - Calculate margins: gross, operating, net
   - If prior period data available, add period-over-period comparison columns
   - Highlight material variances (>10% change from prior period)

3. **Budget vs. Actual Report:**
   - Load current budget document and actual spending data
   - Calculate variance per line item: absolute ($) and relative (%)
   - Color-code: under budget (favorable), within 10% (on track), over 10% (warning), over 20% (critical)
   - Add year-to-date column showing cumulative budget utilization
   - Include forecast to year-end: will current spending rate exhaust the budget?

4. **Revenue Report:**
   - Break down revenue by source, client, product line, and type (recurring vs. one-time)
   - Calculate key metrics: MRR, ARR, NRR, ARPA, growth rates
   - Show trailing 12-month trend chart (ASCII or table format)
   - Highlight top clients by revenue contribution
   - Flag concentration risks (any client >20% of revenue)

5. **Expense Report:**
   - Categorize all expenses with vendor-level detail
   - Calculate per-category totals and percentage of revenue
   - Show month-over-month trend per category
   - Benchmark against targets or prior year
   - Include top 10 vendors by spend

6. **Cash Flow Report:**
   - Operating activities: revenue collected minus expenses paid
   - Investing activities: equipment purchases, deposits
   - Financing activities: loans, equity, dividends
   - Net cash position and 90-day projection
   - Flag potential cash shortfalls with timing

7. **Executive Summary:**
   - 5-8 key financial metrics with trend indicators
   - Revenue and margin highlights
   - Budget utilization status
   - Cash position and runway
   - Top 3 risks and top 3 opportunities
   - Recommended actions

8. **AR Aging Report:**
   - Bucket outstanding invoices: current, 1-30 days, 31-60 days, 61-90 days, 90+ days
   - Calculate total outstanding per bucket
   - Identify highest-risk accounts (large balances in 60+ day buckets)
   - Calculate DSO (Days Sales Outstanding)
   - Recommend collection actions per bucket

9. **Save and distribute:**
   - Save report to `reports/financial-report-YYYY-MM-DD-[type].md`
   - Generate CSV companion file for data-heavy reports
   - Suggest distribution: "Report ready. Share via `/proagent-finance-run` with Gmail integration for email distribution."
