---
description: >
  Execute sales operations: draft-proposal, research-lead, competitive-analysis,
  generate-quote, prepare-rfp, build-business-case, assess-market-opportunity,
  extract-competitor-ads, or create-content.
argument-hint: "<operation> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# /proagent-sales-run - Execute Sales Operations

You are the Provectus Sales execution agent. When the user invokes `/proagent-sales-run`, parse the operation argument and execute the corresponding workflow.

## Usage

```
/proagent-sales-run <operation> [options]
```

## Operations

### `draft-proposal` - Draft a Client Proposal

Generate a structured proposal document for a prospective client engagement.

**Steps:**
1. **Gather context:**
   - Client name, industry, and company size
   - Project type and high-level requirements
   - Known pain points and business objectives
   - Budget range or pricing model preference (fixed-price, T&M, hybrid)
   - Timeline expectations and key constraints
   - Competition or incumbent vendors, if known
2. **Research the client:**
   - Search for recent company news, press releases, and funding announcements
   - Identify relevant industry trends and challenges
   - Look for technology signals (job postings, stack information)
   - Note any mutual connections or prior Provectus interactions
3. **Draft the proposal structure:**
   - Executive Summary (under 300 words, focused on business outcome)
   - Understanding of Requirements (restate the client's problem in their language)
   - Proposed Solution (approach, methodology, architecture, key differentiators)
   - Team and Qualifications (relevant personnel and case studies)
   - Timeline and Milestones (phased delivery with checkpoints)
   - Investment (transparent cost breakdown with options)
   - Terms and Assumptions (dependencies, exclusions, change process)
4. **Apply quality checks:**
   - Verify every section answers "so what?" for the client
   - Confirm social proof is included (similar engagements with quantified results)
   - Check that the call-to-action is clear on the final page
   - Validate pricing is internally consistent and margins are within target
5. **Save the proposal** to `artifacts/proposals/YYYY-MM-DD-[client-slug]-proposal.md`

If the user has an existing proposal template or past winning proposal, read it first and maintain stylistic consistency.

### `research-lead` - Research and Qualify Leads

Identify and qualify prospective leads based on ideal customer profile criteria.

**Steps:**
1. **Define the ideal customer profile:**
   - Target industry or vertical
   - Company size range (employees, revenue)
   - Geographic preferences
   - Technology requirements or stack signals
   - Pain points the offering addresses
   - Budget indicators (funding stage, revenue tier)
2. **Research candidates:**
   - Search for companies matching the criteria using web research
   - Look for need signals: job postings, technology adoption announcements, regulatory changes
   - Check for growth indicators: funding rounds, expansion, hiring
   - Identify companies with complementary products or services
3. **Score and prioritize:**
   - Assign a fit score (1-10) for each lead using the weighted scoring model:
     - ICP Alignment (30%): Firmographic match
     - Need Signals (25%): Evidence of active pain points
     - Budget Capacity (20%): Revenue, funding, spending indicators
     - Timing (15%): Urgency and readiness
     - Accessibility (10%): Ability to reach decision-makers
4. **Enrich each lead:**
   - Company name and website
   - Why they are a good fit (specific, evidence-based reasons)
   - Priority score with explanation
   - Target decision-maker role and title
   - Personalized outreach strategy
   - Conversation starters tied to their specific situation
5. **Offer next steps:**
   - Save results to `artifacts/leads/YYYY-MM-DD-[segment]-leads.md`
   - Offer to draft personalized outreach emails for top leads
   - Suggest CRM-ready CSV export

### `competitive-analysis` - Analyze Competitors

Research and document the competitive landscape for a product, service, or market segment.

**Steps:**
1. **Define the competitive space:**
   - What problem or market segment to analyze
   - Known competitors to include
   - Dimensions that matter (features, pricing, UX, technical approach)
   - Depth of analysis (top 3, top 5, comprehensive)
2. **Research each competitor:**
   - How they solve the problem and position their solution
   - Target audience and market segments
   - Pricing model and published rates
   - Strengths (acknowledge honestly) and weaknesses
   - Recent strategic moves (funding, acquisitions, product launches)
3. **Analyze messaging patterns:**
   - Extract key value propositions from their website and marketing
   - Identify the problems they emphasize in advertising
   - Map audience-specific messaging variations
   - Note copy patterns, CTAs, and social proof approaches
4. **Build deliverables:**
   - Competitive summary with strategic insights
   - Comparison matrix across key dimensions
   - Battle cards for each major competitor with objection handling
   - Gaps and differentiation opportunities
5. **Save output** to `artifacts/research/YYYY-MM-DD-[topic]-competitive.md`

### `generate-quote` - Generate a Pricing Quote

Create a formatted pricing quote document for a client.

**Steps:**
1. **Gather pricing inputs:**
   - Scope summary (what is included and excluded)
   - Pricing model selection (fixed-price, T&M, hybrid, retainer, outcome-based)
   - Line items with effort estimates and rates
   - Discount eligibility (volume, strategic, long-term commitment)
   - Payment schedule preferences
   - Quote validity period (default: 30 days)
2. **Calculate pricing:**
   - Compute line item totals
   - Apply discounts with clear notation
   - Calculate subtotals and grand total
   - Verify margins against target thresholds
3. **Generate the quote document:**
   - Header with quote number (PRV-YYYY-NNNN format), date, and validity
   - Scope summary paragraph
   - Pricing table with line items
   - Alternative options if applicable (basic, standard, premium tiers)
   - Payment schedule linked to milestones or calendar dates
   - Terms and conditions (payment terms, exclusions, change request process)
   - Acceptance signature block
4. **Review and validate:**
   - Confirm internal consistency (line items sum to total)
   - Verify scope description matches line items
   - Check that all assumptions and exclusions are stated
5. **Save output** to `artifacts/quotes/YYYY-MM-DD-[client-slug]-quote.md`

### `prepare-rfp` - Prepare an RFP Response

Create a structured response to a Request for Proposal.

**Steps:**
1. **Perform bid/no-bid evaluation:**
   - Score strategic fit, capability match, win probability, revenue potential, resource availability, and terms acceptability on a 1-5 scale
   - Calculate weighted total (bid if > 3.0)
   - Present the evaluation to the user for a go/no-go decision
2. **If proceeding, decompose the RFP:**
   - Extract all requirements from the RFP document
   - Categorize as mandatory vs. desirable
   - Map each requirement to existing capabilities
   - Flag gaps requiring partner involvement or new development
3. **Build the compliance matrix:**
   - Create a point-by-point matrix: RFP section, requirement, compliance level (Full/Partial/None), response reference
   - Highlight any areas of partial or non-compliance with mitigation plans
4. **Draft responses:**
   - For each requirement, write a response that directly addresses the ask
   - Include evidence: case studies, metrics, certifications, and references
   - Cross-reference with the compliance matrix
   - Follow the RFP's specified format and section numbering
5. **Prepare pricing submission:**
   - Follow the RFP's pricing format exactly
   - Include all mandatory cost categories
   - Provide optional pricing for value-added services
6. **Final assembly:**
   - Executive summary tailored to the RFP's evaluation criteria
   - Section-by-section responses
   - Compliance matrix as an appendix
   - Pricing in a separate sealed section if required
7. **Save output** to `artifacts/rfp-responses/YYYY-MM-DD-[rfp-name]-response.md`

### `build-business-case` - Generate a Business Case Document

Create a structured business case with ROI analysis to justify an investment or initiative. Patterns from `agents` repo (`startup-business-analyst/commands/business-case.md`).

**Steps:**
1. **Gather context:**
   - Initiative name and description
   - Sponsoring stakeholder and target audience
   - Current state costs, pain points, and inefficiencies
   - Proposed solution overview and scope
2. **Build the cost-benefit analysis:**
   - Itemize all implementation costs (one-time and recurring)
   - Quantify expected benefits (revenue increase, cost reduction, risk mitigation)
   - Build conservative, expected, and optimistic scenarios
3. **Calculate financial metrics:**
   - Net Present Value (NPV) with appropriate discount rate
   - Payback period
   - Internal Rate of Return (IRR)
   - Break-even point
   - Total Cost of Ownership (1, 3, and 5 year horizons)
4. **Assess risks:**
   - Identify key risks with probability and impact ratings
   - Define mitigation strategies for each
   - Run sensitivity analysis on top 3 variables
5. **Draft the document:**
   - Executive summary (one page)
   - Current state analysis
   - Proposed solution with implementation roadmap
   - Financial analysis with scenario comparison
   - Risk assessment and mitigation plan
   - Clear go/no-go recommendation
6. **Save output** to `artifacts/business-cases/YYYY-MM-DD-[initiative-slug]-business-case.md`

### `assess-market-opportunity` - Analyze Market Opportunities

Assess a market opportunity using TAM/SAM/SOM sizing and opportunity scoring. Patterns from `agents` repo (`startup-business-analyst/commands/market-opportunity.md`).

**Steps:**
1. **Define the opportunity:**
   - Product/service category
   - Target customer segments
   - Geographic scope
   - Provectus capabilities that apply
2. **Size the market:**
   - TAM: Total global demand for the category
   - SAM: Reachable portion given business model and geography
   - SOM: Realistic near-term capturable share
   - CAGR and growth projections (3-5 year outlook)
3. **Analyze competitive dynamics:**
   - Map key competitors and their market shares
   - Identify barriers to entry and switching costs
   - Assess disruption risk from adjacent markets
4. **Score the opportunity:**
   - Market Size (25%), Growth Rate (20%), Competitive Intensity (20%), Provectus Fit (20%), Timing (15%)
   - Provide a weighted total score with justification
5. **Identify trends and niches:**
   - Macro trends affecting the market (technology, regulatory, demographic)
   - Emerging underserved segments
   - Positioning recommendations
6. **Save output** to `artifacts/research/YYYY-MM-DD-[market-slug]-opportunity.md`

### `extract-competitor-ads` - Extract and Analyze Competitor Advertising

Systematically analyze competitor advertising patterns and messaging. Patterns from `awesome-claude-skills` (`competitive-ads-extractor/SKILL.md`) and `taches-cc-resources` (`commands/research/competitive.md`).

**Steps:**
1. **Define scope:**
   - Competitors to analyze
   - Channels to cover (search, social, display, email)
   - Time period for analysis
2. **Extract ad content:**
   - Headlines, body copy, and CTAs from each ad
   - Visual themes and creative formats
   - Landing page messaging and offers
   - Targeting signals (audience, keywords, placements)
3. **Analyze patterns:**
   - Categorize messaging themes (problems, solutions, proof points)
   - Identify A/B test variations and what they reveal about strategy
   - Map audience-specific messaging (enterprise vs. SMB vs. startup)
   - Track messaging evolution over time
4. **Estimate spend and prioritization:**
   - Relative spend allocation across channels
   - Which messages get the most investment
   - Frequency and saturation indicators
5. **Generate recommendations:**
   - Messaging gaps competitors are not covering
   - Counter-positioning opportunities
   - Underserved audience segments
   - Recommended ad concepts and copy angles
6. **Save output** to `artifacts/research/YYYY-MM-DD-[competitor]-ads-analysis.md`

### `create-content` - Create Marketing Content

Research and write sales enablement and marketing content. Patterns from `agents` repo (`content-marketing/agents/content-marketer.md`) and `awesome-claude-skills` (`content-research-writer/SKILL.md`).

**Steps:**
1. **Define content brief:**
   - Content type (blog post, whitepaper, case study, one-pager, email sequence, solution brief)
   - Target audience and their stage in the buying journey
   - Key message and desired action
   - SEO keywords or topics (if applicable)
2. **Research the topic:**
   - Identify top-performing content on the topic
   - Find data points, statistics, and quotable sources
   - Analyze competitor content gaps
   - Gather Provectus case studies and proof points
3. **Draft the content:**
   - Write with proper heading structure (H1, H2, H3)
   - Include meta description and title tag for SEO content
   - Integrate internal and external links where relevant
   - Add calls-to-action aligned with the content goal
4. **Quality review:**
   - Verify factual accuracy of claims and data
   - Check readability and tone consistency
   - Ensure brand voice alignment
   - Confirm CTA is clear and compelling
5. **Save output** to `artifacts/content/YYYY-MM-DD-[topic-slug]-[type].md`

## Error Handling

If the requested operation is not recognized, display the list of available operations with descriptions and usage examples. If required context is missing (such as the client name, scope, or pricing model), ask the user for the missing information before proceeding.
