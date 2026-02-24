## Sales Automation

Patterns drawn from `agents` repo (`customer-sales-automation/agents/customer-support.md` and `sales-automator.md`).

### Customer Support Automation

Automate common customer support interactions within the sales cycle:

- **Pre-sale inquiries** - Auto-respond to product/service questions with qualified answers and route to sales reps when buying signals are detected
- **Quote follow-ups** - Automated sequences to follow up on sent quotes at defined intervals
- **Meeting scheduling** - Coordinate calendar availability and send booking confirmations
- **FAQ handling** - Maintain and deliver answers to frequently asked questions with contextual upsell suggestions

### Sales Process Automation

Streamline repetitive sales tasks:

- **Lead routing** - Automatically assign inbound leads based on territory, industry, deal size, or round-robin rules
- **Data entry automation** - Extract deal details from emails, calls, and documents into CRM fields
- **Stage progression triggers** - Automatically update pipeline stages when milestone events occur (proposal sent, contract signed)
- **Alert generation** - Notify reps when deals go stale, contracts near renewal, or competitors are mentioned by prospects

## Content Marketing

Patterns drawn from `agents` repo (`content-marketing/agents/content-marketer.md`) and `awesome-claude-skills` (`content-research-writer/SKILL.md`, `domain-name-brainstormer/SKILL.md`).

### Content Research and Writing

Research-driven content creation for sales enablement and marketing:

1. **Topic Research** - Identify high-value content topics using keyword analysis, competitor content gaps, and audience questions
2. **SEO-Optimized Writing** - Draft blog posts, whitepapers, and case studies optimized for search visibility with proper heading structure, meta descriptions, and internal linking
3. **Sales Enablement Content** - Create one-pagers, solution briefs, and email nurture sequences that support the sales team
4. **Thought Leadership** - Draft executive bylines, opinion pieces, and industry analysis articles that position Provectus as an authority

### Domain Name Brainstorming

Generate and evaluate domain name candidates for new products, ventures, or campaigns:

- Brainstorm names based on brand positioning, target keywords, and audience
- Check availability patterns and suggest alternatives
- Score candidates on memorability, pronounceability, and brand fit
- Recommend TLD strategies (.com, .io, .ai, etc.)

## Competitive Advertising Analysis

Patterns drawn from `awesome-claude-skills` (`competitive-ads-extractor/SKILL.md`) and `taches-cc-resources` (`commands/research/competitive.md`).

### Ad Extraction and Analysis

Systematically analyze competitor advertising across channels:

1. **Ad Discovery** - Identify competitor ads across search, social, and display channels
2. **Message Extraction** - Extract headlines, body copy, CTAs, value propositions, and offers from each ad
3. **Pattern Analysis** - Categorize messaging themes, identify A/B test variations, and map audience targeting
4. **Spend Estimation** - Estimate relative ad spend and budget allocation across channels
5. **Gap Identification** - Find messaging angles and audience segments competitors are not covering
6. **Actionable Recommendations** - Suggest counter-positioning strategies and underserved messaging opportunities

### Competitive Research Command

Structured competitive research following the `taches-cc-resources` research command pattern:

- Define research scope (market segment, geographic focus, competitor list)
- Gather data from public sources (websites, press releases, job postings, reviews, social media)
- Synthesize findings into standardized competitive profiles
- Produce comparison matrices and strategic recommendations

## Business Case Generation

Patterns drawn from `agents` repo (`startup-business-analyst/commands/business-case.md`).

### Business Case Structure

Generate structured business case documents that justify investments and initiatives:

1. **Executive Summary** - Problem statement, proposed solution, and expected ROI in one page
2. **Current State Analysis** - Document existing costs, inefficiencies, risks, and missed opportunities
3. **Proposed Solution** - Describe the initiative with scope, approach, and timeline
4. **Cost-Benefit Analysis** - Quantify all costs (implementation, ongoing, opportunity) and benefits (revenue, savings, risk reduction)
5. **ROI Calculation** - Net present value, payback period, internal rate of return, and break-even analysis
6. **Risk Assessment** - Identify risks with probability, impact, and mitigation strategies
7. **Implementation Roadmap** - Phased plan with milestones and resource requirements
8. **Recommendation** - Clear go/no-go recommendation with supporting rationale

### ROI Modeling

- Build financial models with conservative, expected, and optimistic scenarios
- Include sensitivity analysis showing which variables most affect outcomes
- Calculate total cost of ownership over 1, 3, and 5 year horizons
- Compare build vs. buy vs. partner options when applicable

## Market Opportunity Analysis

Patterns drawn from `agents` repo (`startup-business-analyst/commands/market-opportunity.md`).

### Market Sizing Framework

Assess market opportunities using structured top-down and bottom-up analysis:

1. **TAM (Total Addressable Market)** - Total market demand for the product/service category globally
2. **SAM (Serviceable Addressable Market)** - Portion of TAM reachable with current business model and geography
3. **SOM (Serviceable Obtainable Market)** - Realistic share capturable in the near term given competitive dynamics
4. **Growth Projections** - CAGR estimates based on industry trends, adoption curves, and historical data

### Opportunity Scoring

Evaluate market opportunities on multiple dimensions:

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Market Size | 25% | TAM/SAM/SOM attractiveness |
| Growth Rate | 20% | Current and projected CAGR |
| Competitive Intensity | 20% | Number and strength of incumbents |
| Provectus Fit | 20% | Alignment with capabilities and positioning |
| Timing | 15% | Market readiness and window of opportunity |

### Trend Analysis

- Identify macro trends affecting the target market (technology, regulatory, demographic, economic)
- Map emerging niches and underserved segments
- Assess disruption risk from new entrants and adjacent markets
- Recommend positioning strategy based on market dynamics

## Cross-Practice: ROM Estimation

Reference the delivery practice ROM estimation skill (`proagent-delivery/skills/rom-estimate/SKILL.md`) when building proposal pricing. This enables rough order of magnitude estimates for project scoping that feed directly into pricing models and quote generation.
