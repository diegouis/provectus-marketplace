# Provectus Sales Practice Plugin

This plugin provides the Sales practice context for the Provectus agentic coding platform. It equips Claude with production-tested business development patterns drawn from actual Provectus repositories for proposal creation, lead research, competitive intelligence, pricing, and deal management.

## Practice Scope

The Sales practice covers seven operational domains:

1. **Proposal Drafting** - Structured client proposals and statements of work with executive summaries, solution designs, timelines, pricing, and terms
2. **RFP Response Preparation** - Bid/no-bid evaluation, requirements decomposition, compliance matrices, and coordinated multi-section responses
3. **Lead Research and Qualification** - Ideal customer profiling, lead scoring, data enrichment, and personalized outreach strategy
4. **Competitive Analysis** - Competitor positioning, battle cards, messaging analysis, comparison matrices, and differentiation opportunities
5. **Pricing and Quote Generation** - Pricing model selection, margin analysis, formatted quote documents, and payment schedule design
6. **Deal Pipeline Management** - Stage tracking, health metrics, stalled deal intervention, revenue forecasting, and win/loss analysis
7. **Stakeholder Engagement** - Buying committee mapping, engagement cadences, champion coaching, and executive communication

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

- **Slack**: Post deal updates, pipeline notifications, and team communications
- **Google Drive**: Create and collaborate on proposals, quotes, and competitive analyses
- **GitHub**: Repository access for sales documentation and template version control
- **Rube (Composio)**: SaaS automation gateway providing access to Salesforce, HubSpot, Pipedrive, Close, LinkedIn, and Zoho CRM via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## Source Repositories

This plugin draws patterns from: awesome-claude-skills, agents, taches-cc-resources, proagent, and skills.

## Plugin Structure

```
proagent-sales/
  .claude-plugin/plugin.json
  skills/sales-assistant/SKILL.md
  commands/proagent-sales-hub.md
  commands/proagent-sales-run.md
  commands/proagent-sales-review.md
  agents/sales-specialist.md
  hooks/hooks.json
  .mcp.json
  CLAUDE.md
  README.md
```
