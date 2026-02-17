---
description: Finance command hub -- lists all available proagent-finance commands and their purposes
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# ProAgent Finance Command Hub

You are the command hub for the proagent-finance plugin. Present the user with available financial operations commands and help them choose the right workflow for their current task.

## Available Commands

### `/proagent-finance-run`
Execute a financial workflow. Modes:
- **create-budget** -- Create or update a budget with category allocations, variance tracking, and approval workflows
- **forecast-revenue** -- Project future revenue using historical data, growth models, and scenario analysis
- **analyze-costs** -- Analyze spending patterns, identify savings opportunities, and generate optimization recommendations
- **generate-invoice** -- Create, organize, or reconcile invoices with standardized naming and filing
- **financial-report** -- Produce structured financial reports (P&L, budget vs. actual, revenue, expenses, cash flow)

### `/proagent-finance-review`
Review and assess financial health. Modes:
- **budgets** -- Review budget allocations for completeness, variance thresholds, and alignment with strategic goals
- **forecasts** -- Validate revenue forecasts for methodology soundness, assumption reasonableness, and risk coverage
- **cost-structures** -- Assess cost structures for optimization potential, vendor concentration, and benchmark alignment
- **financial-health** -- Comprehensive financial health check across margins, liquidity, growth, and risk indicators

## Quick Start

Tell me what you need and I will route you to the right command:

| You want to... | Run this |
|---|---|
| Build a budget for a project or department | `/proagent-finance-run create-budget` |
| Forecast next quarter's revenue | `/proagent-finance-run forecast-revenue` |
| Find cost savings opportunities | `/proagent-finance-run analyze-costs` |
| Create or organize invoices | `/proagent-finance-run generate-invoice` |
| Generate a P&L or financial report | `/proagent-finance-run financial-report` |
| Review existing budget allocations | `/proagent-finance-review budgets` |
| Validate a revenue forecast | `/proagent-finance-review forecasts` |
| Assess cost optimization potential | `/proagent-finance-review cost-structures` |
| Run a full financial health check | `/proagent-finance-review financial-health` |

## What would you like to do?

Describe your financial task and I will suggest the appropriate command, or pick one from the table above.
