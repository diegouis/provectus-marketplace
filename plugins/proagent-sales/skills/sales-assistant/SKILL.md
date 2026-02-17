---
name: sales-assistant
description: Driving Sales & Business Development - proposals, RFP responses, pricing strategies, CRM management, deal pipeline tracking, competitive analysis, lead research, and quote generation. Use when performing any sales, business development, or client acquisition task.
---

# Driving Sales & Business Development

Comprehensive sales skill covering the full lifecycle of business development from lead identification through deal closure and account management. Built from production-tested patterns across Provectus sales and consulting teams.

## When to Use This Skill

- Drafting proposals and statements of work for prospective clients
- Responding to RFPs with structured, compliant submissions
- Researching and qualifying leads for outreach campaigns
- Building competitive intelligence on market players
- Creating pricing models and generating client quotes
- Managing deal pipeline stages and forecasting revenue
- Crafting personalized cold outreach sequences
- Preparing sales presentations and pitch decks
- Analyzing win/loss patterns to improve conversion rates
- Stakeholder mapping and engagement planning for enterprise deals

## Proposal Drafting

### Proposal Structure

Every proposal should follow this ordered progression, derived from `agents/plugins/customer-sales-automation/agents/sales-automator.md`:

1. **Executive Summary** - The client's problem restated in their language, your approach in one paragraph, and the expected business outcome
2. **Understanding of Requirements** - Demonstrate that you have listened; restate scope, constraints, and success criteria
3. **Proposed Solution** - Technical approach, methodology, architecture, and tooling with clear rationale
4. **Team and Qualifications** - Key personnel, relevant experience, and case studies that mirror the client's situation
5. **Timeline and Milestones** - Phased delivery plan with checkpoints and deliverables per phase
6. **Pricing** - Transparent cost breakdown with options (fixed-price, T&M, hybrid) and payment schedule
7. **Terms and Assumptions** - Dependencies, exclusions, change request process, and risk mitigations
8. **Appendices** - Resumes, certifications, architecture diagrams, references

### Proposal Writing Principles

Derived from the sales-automator agent pattern:

- Lead with value, not features; every section should answer "so what?" for the client
- Personalize using research on the client's industry, recent news, and stated pain points
- Keep executive summaries under 300 words; decision-makers scan, they do not read
- Include one clear call-to-action on the final page
- Reference specific outcomes from similar engagements with quantified results
- Address objections preemptively in the Terms section

### Proposal Template

```markdown
# [Project Name] Proposal

**Prepared for:** [Client Name]
**Prepared by:** Provectus
**Date:** [Date]
**Valid until:** [Date + 30 days]

---

## Executive Summary

[Client Name] is facing [specific challenge from discovery]. We propose
[solution approach] delivered over [timeline] to achieve [measurable outcome].

Based on our experience with [similar client/project], we expect this
engagement to [quantified benefit].

## Understanding of Requirements

### Business Context
[Client's strategic goals and how this project fits]

### Technical Requirements
[Specific deliverables and acceptance criteria]

### Success Criteria
| Metric | Current State | Target State |
|--------|--------------|--------------|
| [KPI 1] | [Baseline] | [Goal] |
| [KPI 2] | [Baseline] | [Goal] |

## Proposed Solution

### Approach
[Methodology and phasing]

### Architecture
[Technical design and tooling choices with rationale]

### Key Differentiators
- [Why our approach is better suited than alternatives]

## Team

| Role | Name | Relevant Experience |
|------|------|-------------------|
| Project Lead | [Name] | [Experience] |
| Technical Lead | [Name] | [Experience] |

## Timeline

| Phase | Duration | Deliverables | Milestone |
|-------|----------|-------------|-----------|
| Discovery | 2 weeks | Requirements doc | Kickoff sign-off |
| Build | 6 weeks | Working system | Demo review |
| Launch | 2 weeks | Production deployment | Go-live |

## Investment

| Component | Effort | Rate | Cost |
|-----------|--------|------|------|
| [Phase/Component] | [Hours] | [Rate] | [Amount] |
| **Total** | | | **[Total]** |

Payment terms: [Net 30 / milestone-based / etc.]

## Assumptions and Terms

- [Key assumption 1]
- [Key assumption 2]
- Change requests handled via [process]
```

## Lead Research and Qualification

### Ideal Customer Profile Definition

Derived from `awesome-claude-skills/lead-research-assistant/SKILL.md`:

When researching leads, build a profile across these dimensions:

1. **Company Firmographics** - Industry, employee count, revenue range, funding stage, headquarters location
2. **Technology Signals** - Current tech stack, recent technology adoptions, job postings for specific skills
3. **Pain Point Indicators** - Publicly stated challenges, industry trends affecting them, regulatory pressures
4. **Budget Signals** - Recent funding rounds, expansion announcements, IT spending patterns
5. **Timing Signals** - Fiscal year timing, contract renewal periods, strategic initiative announcements

### Lead Scoring Model

For each lead, assign a fit score (1-10) based on:

| Dimension | Weight | Score Criteria |
|-----------|--------|---------------|
| ICP Alignment | 30% | How closely they match the ideal customer profile |
| Need Signals | 25% | Evidence of active pain points your solution addresses |
| Budget Capacity | 20% | Revenue, funding, and spending indicators |
| Timing | 15% | Urgency and readiness to buy |
| Accessibility | 10% | Ability to reach decision-makers |

### Lead Research Output Format

```markdown
# Lead Research Results

## Summary
- Total leads found: [X]
- High priority (8-10): [X]
- Medium priority (5-7): [X]
- Average fit score: [X]

---

## Lead 1: [Company Name]

**Website**: [URL]
**Priority Score**: [X/10]
**Industry**: [Industry]
**Size**: [Employee count / revenue range]

**Why They Are a Good Fit**:
[2-3 specific reasons based on their business]

**Target Decision Maker**: [Role/Title]

**Value Proposition for Them**:
[Specific benefit for this company]

**Outreach Strategy**:
[Personalized approach - mention specific pain points, recent news]

**Conversation Starters**:
- [Specific point 1]
- [Specific point 2]
```

## Competitive Analysis

### Competitive Research Framework

Derived from `taches-cc-resources/commands/research/competitive.md`:

For each competitor, analyze:

1. **Solution Positioning** - How they describe their offering and who they target
2. **Pricing Model** - Published pricing, packaging tiers, and discounting patterns
3. **Strengths** - What they genuinely do well; do not be dismissive
4. **Weaknesses** - Where they fall short or overextend
5. **Win/Loss Patterns** - Situations where they win deals vs. where they lose

### Competitive Battle Card Template

```markdown
## Battle Card: [Competitor Name]

### Quick Overview
- **Founded:** [Year]
- **Size:** [Employees / Revenue]
- **Primary Market:** [Target segment]
- **Key Clients:** [Notable logos]

### Their Pitch
[How they position themselves - in their own words]

### Strengths (acknowledge honestly)
- [Strength 1]
- [Strength 2]

### Weaknesses (our advantages)
- [Weakness 1 → our advantage]
- [Weakness 2 → our advantage]

### Common Objections and Responses
| Objection | Response |
|-----------|----------|
| "[Their strength claim]" | "[Our counter with evidence]" |
| "[Price comparison]" | "[Value justification]" |

### When We Win Against Them
- [Scenario/criteria where we consistently win]

### When We Lose to Them
- [Scenario/criteria where they have advantage]
- **Mitigation:** [How to address this in deals]

### Comparison Matrix
| Capability | Us | Them |
|-----------|-----|------|
| [Feature 1] | [Rating] | [Rating] |
| [Feature 2] | [Rating] | [Rating] |
```

### Ad and Messaging Analysis

Derived from `awesome-claude-skills/competitive-ads-extractor/SKILL.md`:

When analyzing competitor marketing:

- Extract and categorize messaging themes (problems highlighted, use cases targeted, value propositions)
- Identify successful ad patterns (visual formats, copy length, CTA styles)
- Map audience targeting by ad variation (enterprise vs. SMB vs. startup messaging)
- Track messaging evolution over time to detect strategic shifts
- Identify gaps in competitor messaging that represent positioning opportunities

## Pricing and Quote Generation

### Pricing Strategy Framework

Build pricing models around these components:

1. **Cost-Plus Baseline** - Calculate fully loaded cost (labor, tools, overhead) and target margin
2. **Value-Based Adjustment** - Adjust pricing based on the measurable business value delivered to the client
3. **Competitive Positioning** - Position relative to market alternatives (premium, parity, or value)
4. **Risk Allocation** - Adjust for fixed-price risk premiums, scope uncertainty buffers, and technology risk

### Pricing Models

| Model | When to Use | Risk Profile |
|-------|-------------|-------------|
| Fixed Price | Clear scope, well-understood requirements, short duration | Higher risk to seller |
| Time and Materials | Evolving scope, R&D projects, ongoing engagements | Higher risk to buyer |
| Hybrid (T&M with cap) | Moderate uncertainty, client needs budget predictability | Balanced risk |
| Retainer | Ongoing advisory, support, or fractional team | Predictable for both |
| Outcome-Based | High-confidence ROI, measurable KPIs, strong track record | Highest risk to seller |

### Quote Document Template

```markdown
# Quote: [Project/Service Name]

**Client:** [Client Name]
**Quote #:** [PRV-YYYY-NNNN]
**Date:** [Date]
**Valid Until:** [Date + 30 days]

## Scope Summary
[One paragraph describing what is included]

## Pricing Options

### Option A: [Model Name]
| Line Item | Quantity | Unit Price | Total |
|-----------|----------|-----------|-------|
| [Service/Phase 1] | [Units] | [Price] | [Total] |
| [Service/Phase 2] | [Units] | [Price] | [Total] |
| **Subtotal** | | | **[Amount]** |
| Discount ([X]%) | | | -[Amount] |
| **Total** | | | **[Amount]** |

### Option B: [Alternative Model]
[Same structure with different packaging]

## Payment Schedule
| Milestone | Amount | Due Date |
|-----------|--------|----------|
| Project kickoff | [X]% | [Date] |
| Phase 1 delivery | [X]% | [Date] |
| Final delivery | [X]% | [Date] |

## Terms
- Payment terms: Net 30
- Currency: USD
- Excludes: [Out of scope items]
- Change requests: Quoted separately at [rate]

## Acceptance
Signature: _________________________
Name: _________________________
Date: _________________________
```

## RFP Response Preparation

### RFP Response Process

1. **Bid/No-Bid Decision** - Evaluate alignment with capabilities, strategic fit, win probability, and resource availability
2. **Requirements Decomposition** - Break the RFP into individual requirements and map each to your capabilities
3. **Compliance Matrix** - Create a point-by-point compliance matrix showing how each requirement is met
4. **Response Drafting** - Write responses that directly address each requirement with evidence and examples
5. **Pricing Submission** - Prepare pricing per the RFP's specified format
6. **Review and Polish** - Executive review, compliance check, and final formatting

### Compliance Matrix Template

```markdown
| RFP Section | Requirement | Compliance | Response Reference | Notes |
|-------------|-------------|------------|-------------------|-------|
| 3.1 | [Requirement text] | Full / Partial / None | Section 4.1 | [Notes] |
| 3.2 | [Requirement text] | Full / Partial / None | Section 4.2 | [Notes] |
```

### Bid/No-Bid Evaluation

| Criterion | Score (1-5) | Weight | Notes |
|-----------|------------|--------|-------|
| Strategic fit | [Score] | 20% | [Alignment with company direction] |
| Capability match | [Score] | 25% | [Can we deliver what they need?] |
| Win probability | [Score] | 20% | [Relationship, incumbency, competition] |
| Revenue potential | [Score] | 15% | [Deal size and follow-on opportunity] |
| Resource availability | [Score] | 10% | [Do we have the team?] |
| Terms acceptability | [Score] | 10% | [Are the contract terms reasonable?] |
| **Weighted Total** | | | **Bid if > 3.0** |

## Deal Pipeline Management

### Pipeline Stages

| Stage | Entry Criteria | Exit Criteria | Typical Duration |
|-------|---------------|---------------|------------------|
| Prospecting | Lead identified | Discovery call scheduled | 1-2 weeks |
| Discovery | Initial meeting held | Requirements understood, champion identified | 1-3 weeks |
| Proposal | Requirements confirmed | Proposal submitted and presented | 1-2 weeks |
| Negotiation | Proposal reviewed by client | Terms agreed, verbal commitment | 1-4 weeks |
| Closed Won | Contract signed | Project kickoff scheduled | 1 week |
| Closed Lost | Deal explicitly lost | Loss analysis documented | - |

### Pipeline Health Metrics

| Metric | Healthy Range | Action if Outside |
|--------|--------------|-------------------|
| Win rate | 25-40% | Review qualification criteria if below; qualify harder |
| Average deal cycle | 4-8 weeks | Investigate stalled deals if above |
| Pipeline coverage | 3-4x quota | Increase prospecting if below |
| Stage conversion rates | Steady or improving | Analyze drop-off points |
| Average deal size | Trending up or stable | Review pricing strategy if declining |
| Forecast accuracy | Within 10% of actual | Improve stage criteria definitions |

## Outreach and Follow-Up

### Cold Email Sequence Pattern

Derived from `agents/plugins/customer-sales-automation/agents/sales-automator.md`:

**Email 1: Value-First Introduction**
- Subject line: Specific to their pain point, under 50 characters
- Open with research insight about their company
- One sentence on how you solve that specific problem
- Social proof: one similar client result with a number
- CTA: Ask for 15 minutes, not a demo

**Email 2: Follow-Up (Day 3)**
- Reference Email 1 briefly
- Share a relevant case study or insight
- Different angle on the same pain point
- Same CTA, rephrased

**Email 3: Breakup (Day 7)**
- Acknowledge they are busy
- Provide one more piece of value (article, benchmark, insight)
- Offer to reconnect when timing is better
- No pressure CTA

### Outreach Personalization Variables

For each prospect, research and incorporate:
- Recent company news or announcements
- Specific job postings that signal relevant needs
- Mutual connections or shared experiences
- Industry-specific challenges affecting their vertical
- Technology decisions visible in their stack

## Stakeholder Engagement for Enterprise Deals

### Stakeholder Mapping

Derived from `proagent/roles/project-manager/skills/stakeholder-management.md`:

For enterprise deals, map the buying committee using a Power/Interest grid:

- **Champion** (High Power, High Interest) - Your internal advocate; nurture this relationship
- **Economic Buyer** (High Power, Variable Interest) - Controls budget; communicate ROI and risk mitigation
- **Technical Evaluator** (Variable Power, High Interest) - Validates technical fit; provide depth and proof
- **End Users** (Low Power, High Interest) - Will use the solution; demonstrate ease of use and value
- **Blocker** (Variable Power, Variable Interest) - May resist; understand their concerns and address directly

### Engagement Cadence by Stakeholder Type

| Stakeholder | Frequency | Format | Content Focus |
|------------|-----------|--------|---------------|
| Champion | Weekly | 1:1 call or Slack | Deal progress, obstacles, coaching |
| Economic Buyer | Bi-weekly | Email summary | ROI, risk, timeline, investment |
| Technical Evaluator | As needed | Deep-dive sessions | Architecture, security, integration |
| End Users | During demos | Interactive demos | Workflow improvements, ease of use |

## Composio App Automations

This plugin integrates with Composio-powered SaaS automation skills via the Rube MCP server. These skills connect to real external services for end-to-end workflow automation.

### Available Automations

| Skill | Service | Key Capabilities |
|-------|---------|-----------------|
| salesforce-automation | Salesforce | CRM record management, opportunity tracking, lead conversion, report generation |
| hubspot-automation | HubSpot | Contact management, deal pipeline tracking, marketing automation, email sequences |
| pipedrive-automation | Pipedrive | Deal management, activity tracking, pipeline visualization, sales reporting |
| close-automation | Close | Lead management, calling workflows, email sequences, pipeline analytics |
| linkedin-automation | LinkedIn | Profile research, connection requests, messaging, lead prospecting |
| zoho-crm-automation | Zoho CRM | Contact management, deal tracking, workflow automation, analytics |

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

## Reference Assets

| Asset | Source | Description |
|-------|--------|-------------|
| Lead Research Assistant | `awesome-claude-skills/lead-research-assistant/SKILL.md` | Lead identification, qualification, and outreach strategy |
| Competitive Ads Extractor | `awesome-claude-skills/competitive-ads-extractor/SKILL.md` | Competitor ad analysis and messaging extraction |
| Sales Automator Agent | `agents/plugins/customer-sales-automation/agents/sales-automator.md` | Cold emails, follow-ups, proposals, and sales scripts |
| Competitive Research | `taches-cc-resources/commands/research/competitive.md` | Structured competitive landscape analysis |
| Options Comparison | `taches-cc-resources/commands/research/options.md` | Side-by-side option evaluation with recommendations |
| Stakeholder Management | `proagent/roles/project-manager/skills/stakeholder-management.md` | Stakeholder identification, engagement, and communication |
| Brand Guidelines | `skills/skills/brand-guidelines/SKILL.md` | Visual styling for branded sales materials |
