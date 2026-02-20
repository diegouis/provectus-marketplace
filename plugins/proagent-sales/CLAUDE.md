# Provectus Sales Practice Plugin

This plugin provides the Sales practice context for the Provectus agentic coding platform. It equips Claude with production-tested business development patterns drawn from actual Provectus repositories for proposal creation, lead research, competitive intelligence, pricing, and deal management.

## Practice Scope

The Sales practice covers eleven operational domains:

1. **Proposal Drafting** - Structured client proposals and statements of work with executive summaries, solution designs, timelines, pricing, and terms
2. **RFP Response Preparation** - Bid/no-bid evaluation, requirements decomposition, compliance matrices, and coordinated multi-section responses
3. **Lead Research and Qualification** - Ideal customer profiling, lead scoring, data enrichment, and personalized outreach strategy (enhanced by `lead-research-assistant` from `awesome-claude-skills`)
4. **Competitive Analysis** - Competitor positioning, battle cards, messaging analysis, comparison matrices, and differentiation opportunities (enhanced by `competitive-ads-extractor` from `awesome-claude-skills` and `competitive.md` from `taches-cc-resources`)
5. **Pricing and Quote Generation** - Pricing model selection, margin analysis, formatted quote documents, and payment schedule design
6. **Deal Pipeline Management** - Stage tracking, health metrics, stalled deal intervention, revenue forecasting, and win/loss analysis
7. **Stakeholder Engagement** - Buying committee mapping, engagement cadences, champion coaching, and executive communication
8. **Sales Automation** - Automated customer support workflows and sales process automation (from `agents` repo: `customer-support.md`, `sales-automator.md`)
9. **Content Marketing** - Content research, SEO-driven writing, marketing content creation, and domain name brainstorming (from `agents` repo: `content-marketer.md` and `awesome-claude-skills`: `content-research-writer`, `domain-name-brainstormer`)
10. **Business Case Generation** - Structured business case documents with ROI analysis, cost-benefit modeling, and investment justification (from `agents` repo: `startup-business-analyst/commands/business-case.md`)
11. **Market Opportunity Analysis** - TAM/SAM/SOM estimation, market sizing, trend analysis, and opportunity scoring (from `agents` repo: `startup-business-analyst/commands/market-opportunity.md`)

## Key Conventions

When performing sales tasks, follow these standards:

### Proposals
- Lead with the client's problem, not Provectus capabilities
- Keep executive summaries under 300 words
- Include quantified social proof from similar engagements
- Provide at least two pricing options so the client chooses how to engage
- Address objections preemptively in the Terms section
- Always include a clear call-to-action on the final page

### Lead Research
- Score all leads using the weighted model: ICP Alignment (30%), Need Signals (25%), Budget Capacity (20%), Timing (15%), Accessibility (10%)
- Provide evidence-based reasons for each lead's fit score
- Include personalized outreach strategies, not generic templates
- Offer to save results in CRM-importable format

### Competitive Intelligence
- Acknowledge competitor strengths honestly; clients trust fair analysis
- Include source dates on all competitive data
- Refresh intelligence every 90 days
- Build battle cards with specific objection handling, not vague claims

### Pricing
- Verify that line items sum correctly before presenting quotes
- Include scope assumptions and exclusions in every quote
- Set validity periods (default 30 days)
- Document the change request process and rates

### Pipeline Management
- Maintain 3-4x pipeline coverage against quota
- Flag deals stalled beyond typical stage duration
- Document win/loss reasons for every closed deal
- Forecast using stage-weighted probabilities, not gut feel

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **Rube (Composio)**: SaaS automation gateway providing access to Salesforce, HubSpot, Pipedrive, Close, LinkedIn, and Zoho CRM via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## Cross-Practice References

- **ROM Estimation** (delivery practice) - Use `proagent-delivery/skills/rom-estimate/SKILL.md` for rough order of magnitude estimates when building pricing for proposals and quotes

## External Asset Sources

This plugin draws from assets discovered across multiple Provectus repositories:

| Source Repo | Assets | Capabilities |
|-------------|--------|-------------|
| `agents` | `customer-support.md`, `sales-automator.md`, `content-marketer.md`, `business-case.md`, `market-opportunity.md` | Sales automation, customer support workflows, content marketing, business case and market opportunity analysis |
| `awesome-claude-skills` | `competitive-ads-extractor/SKILL.md`, `content-research-writer/SKILL.md`, `domain-name-brainstormer/SKILL.md`, `lead-research-assistant/SKILL.md` | Competitive ad analysis, content research/writing, domain brainstorming, lead research |
| `taches-cc-resources` | `commands/research/competitive.md` | Competitive analysis research command patterns |
| `provectus-marketplace` | `proagent-sales/*`, `proagent-delivery/skills/rom-estimate/SKILL.md` | Core sales plugin, cross-practice ROM estimation |

## Plugin Structure

```
proagent-sales/
  .claude-plugin/plugin.json
  skills/
    sales-assistant/SKILL.md
  commands/proagent-sales-hub.md
  commands/proagent-sales-run.md
  commands/proagent-sales-review.md
  agents/sales-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
