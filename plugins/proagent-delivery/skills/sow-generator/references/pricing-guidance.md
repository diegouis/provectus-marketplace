# Pricing Guidance

Rate card structure, role-to-rate mapping, and pricing conventions for SOW generation.

---

## Rate Card Structure

Provectus uses a role-based rate card. Rates vary by:
- **Role** — Engineering, ML, Data, QA, Architecture, Design, Management
- **Seniority** — Junior, Mid, Senior, Lead/Principal
- **Engagement type** — T&M rates vs. fixed-price (fixed includes buffer)
- **Geography** — Onshore, nearshore, offshore blended teams
- **Duration** — Longer engagements may qualify for volume discounts

**Important:** Actual rate values are confidential and must be sourced from the current Provectus rate card. The SOW generator should use placeholder values (`$X,XXX`) and flag them for the SO to fill in with current rates.

---

## Standard Roles and Rate Tiers

### Engineering Roles
| Role | Tier | Typical Allocation | Notes |
|------|------|-------------------|-------|
| Solution Owner (SO) | Senior/Lead | 10-25% | Project governance, client relationship |
| Technical Lead | Senior/Lead | 50-100% | Architecture, code review, technical decisions |
| Backend Engineer | Mid-Senior | 100% | API, business logic, integrations |
| Frontend Engineer | Mid-Senior | 100% | UI/UX implementation, responsive design |
| Full-Stack Engineer | Mid-Senior | 100% | Combined backend + frontend |
| DevOps Engineer | Mid-Senior | 25-100% | Infrastructure, CI/CD, cloud operations |

### Data & AI Roles
| Role | Tier | Typical Allocation | Notes |
|------|------|-------------------|-------|
| ML Engineer (MLE I) | Mid-Senior | 50-100% | Model integration, RAG, embeddings |
| ML Engineer (MLE II) | Senior/Lead | 50-100% | Advanced ML, research, architecture |
| Data Engineer | Mid-Senior | 50-100% | Pipelines, ETL, data quality |
| Data Scientist | Mid-Senior | 50-100% | Analysis, modeling, experimentation |

### Specialist Roles
| Role | Tier | Typical Allocation | Notes |
|------|------|-------------------|-------|
| QA Engineer | Mid-Senior | 25-100% | Test strategy, automation, UAT |
| Security Engineer | Senior | 25-50% | Compliance, auditing, security review |
| Cloud Architect | Senior/Lead | 10-25% | System design, review, optimization |
| UI/UX Designer | Mid-Senior | 25-100% | User research, prototyping, design systems |
| Project Manager | Mid-Senior | 25-50% | Coordination, tracking, reporting |

---

## Pricing Models

### Flat-Rate
- Single hourly/daily/monthly rate for all team members
- Simplest to manage; preferred for small engagements (< 4 people)
- Rate is typically a blended average weighted by team composition
- **When to use:** Small teams, short engagements, client prefers simplicity

### Role-Based Rates
- Different rate per role/seniority
- More transparent; client sees what they pay for each capability
- Standard for T&M engagements
- **When to use:** Larger teams, mixed seniority, client wants rate transparency

### Blended Rate
- Weighted average rate across the planned team composition
- Simplifies billing while reflecting actual team makeup
- Recalculated if team composition changes significantly
- **When to use:** T&M engagements where the client wants a single rate but team is diverse

### Delivery-Based (Per-Deliverable)
- Price per deliverable or use case
- Requires well-defined scope (typically post-Discovery)
- Each deliverable has its own price, timeline, and acceptance criteria
- **When to use:** Milestone-based engagements, client wants to pay for outcomes

---

## Pricing Construction

### T&M Pricing (Sprint-Based)

Provectus T&M SOWs typically price by **pod per sprint** (2-week sprints), not hourly:

```
Cost per Sprint = Pod rate (blended team cost for 2-week sprint)
Estimated Total = Cost per Sprint × Number of Sprints
```

**Real example (Natera SOW #28):**

| Description | Duration (Sprints) | Cost per Sprint | Estimated Total Cost |
|---|---|---|---|
| AI Pod | 6 | $16,560 | $99,360 |

**Standard T&M language:**
> "Provectus estimates that [Client]'s total payment under this Statement of Work will be $[X] unless specified through a change order."

- Use the word "estimates" — T&M total is not guaranteed
- Include an invoice schedule table with monthly billing dates
- Note: "Actual billing based on time worked"

### Fixed-Price Pricing

```
Base Effort = ROM estimate (person-days at P50)
Buffered Effort = Base Effort × 1.20 (15-25% risk buffer)
Fixed Price = Buffered Effort × Blended Daily Rate
```

**Standard fixed-price language:**
> "[Client] total payment under this Statement of Work will be $[X]."

Note the difference from T&M: no "estimates" — the price is committed.

- Round to nearest $5K or $10K for clean numbers
- Payment schedule may be milestone-based or monthly
- Include assumptions that protect the price (if assumptions change, price may adjust via change order)
- Define "defect" (warranty) vs. "enhancement" (change order)

### Milestone-Based Pricing
```
Milestone Price = Effort for milestone deliverables × Blended Rate + Buffer
Total = Sum of all milestone prices
```
- Each milestone has independent pricing
- Client can compare cost-per-milestone for budget planning
- Milestone re-sequencing doesn't change total price (unless scope changes)

---

## Discount Guidelines

**Volume discounts:**
- Engagements > 6 months: consider 5-10% discount
- Engagements > 12 months: consider 10-15% discount
- Multi-project clients: portfolio discount up to 15%

**Strategic discounts:**
- Lighthouse account (reference client for new industry/technology): up to 15%
- Co-development partner: up to 20% with IP sharing agreement
- Non-profit or education: up to 25%

**Discount governance:**
- Discounts > 10% require Director approval
- Discounts > 20% require VP approval
- All discounts must be documented in the SOW with expiration terms

---

## Travel & Expenses

**Standard policy:**
- Travel expenses billed at cost with prior client approval
- Per diem rates follow company policy (or client-specified rates)
- Business class for flights > 6 hours
- Travel time billed at 50% of standard rate (or excluded, depending on engagement)

**Remote-first default:**
- State that the engagement is delivered remotely unless specified otherwise
- On-site visits (kickoff, reviews, workshops) billed as travel expenses
- Include estimated on-site frequency if applicable (e.g., "Monthly on-site visits during Phase 1")

---

## What Is NOT Included

Always state explicitly in the SOW:
- Third-party license fees (cloud services, SaaS tools, APIs)
- Cloud infrastructure costs (AWS, GCP, Azure)
- Hardware procurement
- Data acquisition or licensing costs
- Legal review of the SOW itself
- Training beyond knowledge transfer sessions included in scope
