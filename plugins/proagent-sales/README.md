# proagent-sales

Provectus Sales practice plugin for Claude Code. Provides production-tested proposal drafting, lead research, competitive analysis, pricing, RFP response, deal pipeline management, sales automation, content marketing, business case generation, and market opportunity analysis patterns drawn from actual Provectus repositories.

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
/proagent-sales-run draft-proposal          # Draft a client proposal or SOW
/proagent-sales-run research-lead           # Research and qualify prospective leads
/proagent-sales-run competitive-analysis    # Analyze competitors in a market segment
/proagent-sales-run generate-quote          # Generate a pricing quote for a client
/proagent-sales-run prepare-rfp             # Prepare a structured RFP response
/proagent-sales-run build-business-case     # Generate a business case with ROI analysis
/proagent-sales-run assess-market-opportunity # Analyze market opportunities (TAM/SAM/SOM)
/proagent-sales-run extract-competitor-ads  # Extract and analyze competitor advertising
/proagent-sales-run create-content          # Create marketing and sales enablement content
```

### Review Command

Review sales artifacts and strategy:

```
/proagent-sales-review                   # Select a review target interactively
/proagent-sales-review proposal          # Review a proposal for completeness and quality
/proagent-sales-review pricing           # Review pricing for margin and competitiveness
/proagent-sales-review pipeline          # Review pipeline health metrics
/proagent-sales-review deal-strategy     # Review strategy for a specific deal
/proagent-sales-review business-case     # Review a business case for financial rigor
/proagent-sales-review market-opportunity # Review a market opportunity analysis
/proagent-sales-review content           # Review marketing or sales enablement content
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
- Business case template with ROI, NPV, payback period, and sensitivity analysis
- Market opportunity framework with TAM/SAM/SOM sizing and opportunity scoring
- Content marketing brief and SEO-optimized writing patterns
- Competitor ad extraction and messaging analysis templates

### Automated Checks
- Proposal template validation ensuring all required sections are present
- Placeholder text detection to prevent sending unfinished documents to clients
- Pricing consistency checks verifying line items sum correctly
- Competitive intelligence freshness alerts for data older than 90 days

### External Asset Sources
Assets integrated from 4 repositories: `agents`, `awesome-claude-skills`, `taches-cc-resources`, `provectus-marketplace`

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| Rube | `rube.app/mcp` | SaaS automation gateway (Salesforce, HubSpot, Pipedrive, etc.) |

## Version

- Plugin version: 0.3.0
- Category: sales
- Author: Provectus
