# proagent-sales

Provectus Sales practice plugin for Claude Code. Provides production-tested proposal drafting, lead research, competitive analysis, pricing, RFP response, and deal pipeline management patterns drawn from actual Provectus repositories.

## Installation

### Option 1: Copy to your project

Copy the `proagent-sales/` directory into your project's `.claude/plugins/` directory:

```bash
cp -r proagent-sales/ /path/to/your-project/.claude/plugins/proagent-sales/
```

### Option 2: Reference from the marketplace

If your project uses the Provectus marketplace plugin loader, add the plugin to your configuration:

```json
{
  "plugins": ["proagent-sales"]
}
```

### Option 3: Symlink for development

```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-sales /path/to/your-project/.claude/plugins/proagent-sales
```

## Prerequisites

Configure the following environment variables for MCP integrations:

| Variable | Required For | Description |
|----------|-------------|-------------|
| `SLACK_BOT_TOKEN` | Slack integration | Bot token for sales channel notifications |
| `SLACK_TEAM_ID` | Slack integration | Slack workspace ID |
| `GOOGLE_APPLICATION_CREDENTIALS` | Google Docs, Gmail, Calendar | Path to Google service account credentials |

## Usage

### Hub Command

View all available sales capabilities:

```
/proagent-sales-hub
```

### Run Commands

Execute sales operations:

```
/proagent-sales-run draft-proposal       # Draft a client proposal or SOW
/proagent-sales-run research-lead        # Research and qualify prospective leads
/proagent-sales-run competitive-analysis # Analyze competitors in a market segment
/proagent-sales-run generate-quote       # Generate a pricing quote for a client
/proagent-sales-run prepare-rfp          # Prepare a structured RFP response
```

### Review Command

Review sales artifacts and strategy:

```
/proagent-sales-review                   # Select a review target interactively
/proagent-sales-review proposal          # Review a proposal for completeness and quality
/proagent-sales-review pricing           # Review pricing for margin and competitiveness
/proagent-sales-review pipeline          # Review pipeline health metrics
/proagent-sales-review deal-strategy     # Review strategy for a specific deal
```

### Using the Sales Specialist Agent

The plugin includes a sales specialist agent that can be invoked for complex business development tasks:

```
Ask the sales-specialist to research 10 fintech companies that need data platform services
```

### Using the Skill Directly

The sales assistant skill is available for any business development task:

```
Use the sales-assistant skill to draft a proposal for a cloud migration engagement
```

## What This Plugin Provides

### Templates and Frameworks
- Client proposal structure with executive summary, solution, timeline, and pricing
- Statement of work template with deliverables and acceptance criteria
- Competitive battle card format with objection handling scripts
- Lead scoring model with weighted qualification criteria
- Quote document with line items, payment schedule, and terms
- RFP compliance matrix with point-by-point response tracking
- Pipeline stage definitions with entry/exit criteria and health metrics
- Cold email sequence templates (value-first introduction, follow-up, breakup)

### Automated Checks
- Proposal template validation ensuring all required sections are present
- Placeholder text detection to prevent sending unfinished documents to clients
- Pricing consistency checks verifying line items sum correctly
- Competitive intelligence freshness alerts for data older than 90 days

### MCP Integrations
- **Slack** - Deal notifications, proposal review requests, competitive intelligence sharing
- **Google Docs** - Collaborative proposal editing, RFP response coordination, playbook maintenance
- **Gmail** - Outreach email drafting, follow-up sequences, proposal delivery
- **Google Calendar** - Discovery calls, proposal presentations, pipeline review cadences

## Source Repositories

This plugin is built from production patterns across 5 Provectus repositories with 13 total assets (8 high-reuse). Key sources include:

- **awesome-claude-skills** - Lead research assistant for prospect identification and competitive ads extractor for messaging analysis
- **agents** - Sales automation agent for email sequences, proposals, and objection handling scripts
- **taches-cc-resources** - Competitive research framework and options comparison methodology
- **proagent** - Stakeholder management patterns for enterprise deal engagement
- **skills** - Brand guidelines for consistent proposal and presentation styling

## Version

- Plugin version: 0.1.0
- Category: sales
- Author: Provectus
