# Engagement Model Patterns

Reference guide for structuring SOWs across different engagement models.

---

## Time & Materials (T&M)

**Best for:** Evolving requirements, R&D projects, ongoing support, engagements where scope will change frequently.

**Characteristics:**
- Client pays for hours/days worked at agreed rates
- Scope is directional, not fixed — priorities can shift sprint-to-sprint
- Client controls what gets built and in what order
- Lower risk for the provider, higher flexibility for the client
- Typical duration: ongoing or defined engagement window (e.g., 6 months)

**SOW structure:**
- Scope section describes workstreams and objectives, not fixed deliverables
- Deliverables are planned sprint-by-sprint, not enumerated upfront
- Rate card defines pricing (no total project price)
- Monthly billing in arrears based on timesheets
- Team composition may flex based on needs

**Key clauses:**
- Minimum engagement period (e.g., 3 months)
- Notice period for team changes (e.g., 2 weeks)
- Notice period for engagement termination (e.g., 30 days)
- Rate card validity period (e.g., 12 months)
- Timesheet approval process and cadence

**When to recommend:**
- Client has a product team and wants to extend capacity
- Requirements are emerging or subject to frequent change
- Innovation or R&D work where outcomes are uncertain
- Long-term engagements with shifting priorities

---

## Fixed-Price

**Best for:** Well-defined scope, compliance-driven projects, budget-constrained clients, one-time builds.

**Characteristics:**
- Client pays a fixed total for defined scope and deliverables
- Scope is locked — changes require formal Change Orders
- Higher risk for the provider (must estimate accurately), lower risk for the client
- Requires thorough Discovery phase to define scope accurately
- Typical duration: bounded (e.g., 12-16 weeks)

**SOW structure:**
- Scope section is exhaustive with specific deliverables and quantities
- Every deliverable has explicit acceptance criteria
- Total project price tied to milestones
- Payment schedule: typically 30% upfront, milestones, 20% final
- Change management is critical — all scope changes are COs with price adjustments

**Key clauses:**
- Detailed scope with explicit inclusions and exclusions
- Change Order process with cost and timeline impact
- Milestone-based payment schedule
- Warranty period (30-60 days post-acceptance for defect fixes)
- Acceptance process with deemed acceptance clause

**When to recommend:**
- Client needs budget certainty
- Scope is well-understood (typically after a Discovery phase)
- Compliance or procurement requires fixed pricing
- Project has a clear start and end with defined outcomes

**Pricing guidance:**
- Add 15-25% buffer to effort estimates for fixed-price quotes
- Include assumptions that, if violated, may adjust the price
- Define what constitutes a "defect" (warranty) vs. "enhancement" (change order)

---

## Milestone-Based

**Best for:** Medium-complexity projects where the client wants accountability tied to results but also some flexibility.

**Characteristics:**
- Hybrid between T&M and Fixed-Price
- Project divided into milestones, each with defined deliverables and a price
- Payment triggered by milestone acceptance
- Scope within each milestone is defined; order or timing may flex
- Balanced risk: provider commits to deliverables, client pays on acceptance

**SOW structure:**
- Scope organized into 3-6 milestones (not too many — overhead increases)
- Each milestone: scope, deliverables, acceptance criteria, price, timeline
- Milestones can have dependencies or be parallel
- Payment upon milestone acceptance
- Change management applies per-milestone

**Key clauses:**
- Milestone acceptance process and timeline
- Deemed acceptance after review period
- Milestone re-sequencing process (if priorities shift)
- Inter-milestone dependencies and critical path

**When to recommend:**
- Client wants more accountability than T&M but more flexibility than fixed-price
- Project has natural phase boundaries (discovery, build, deploy)
- Multiple stakeholders need visibility into progress and spend

---

## Discovery + Delivery Pair

**Best for:** Engagements where scope is not yet defined, client needs help understanding what to build before committing to a delivery SOW.

**Characteristics:**
- Two-SOW approach: a short Discovery SOW followed by a Delivery SOW
- Discovery is typically fixed-price (2-6 weeks)
- Delivery SOW is generated as an output of Discovery (can be T&M, fixed, or milestone)
- Reduces risk for both parties: client only commits to Discovery initially
- Discovery deliverables include the Delivery SOW itself

**Discovery SOW structure:**
- Duration: 2-6 weeks (typically 3-4)
- Fixed-price (low commitment, typically $20K-$80K range)
- Deliverables: Architecture document, technical specifications, delivery roadmap, ROM estimate, Delivery SOW draft
- Team: Solution Owner + Tech Lead + 1-2 specialists
- Goal: Answer "What should we build, how, and how much will it cost?"

**Delivery SOW structure:**
- Generated from Discovery outputs
- Engagement model chosen based on Discovery findings
- Scope is well-defined because Discovery answered the hard questions
- Team composition sized based on ROM estimate
- Timeline based on technical assessment, not guesses

**Key clauses (Discovery SOW):**
- Discovery is a standalone engagement — no obligation to proceed to Delivery
- Discovery deliverables include: architecture doc, technical specs, ROM estimate, draft Delivery SOW
- Delivery SOW pricing is an estimate at Discovery start, refined as a deliverable
- Client retains all Discovery deliverables regardless of Delivery decision

**When to recommend:**
- Client has a vision but not a detailed technical plan
- Scope is complex or has significant unknowns
- Client needs to build internal buy-in before committing to a large engagement
- Multiple technical approaches are possible and need evaluation
- Budget for Delivery is not yet approved

---

## Engagement Model Selection Guide

Use this decision tree to recommend an engagement model:

```
Is the scope well-defined with specific deliverables?
├── YES: Is the client budget-constrained or compliance-driven?
│   ├── YES → Fixed-Price
│   └── NO: Does the project have natural phase boundaries?
│       ├── YES → Milestone-Based
│       └── NO → T&M with defined engagement window
└── NO: Does the client know what they want to build?
    ├── YES (approximately): Is the engagement > 6 months?
    │   ├── YES → T&M (scope will evolve)
    │   └── NO → Milestone-Based (scope per phase)
    └── NO → Discovery + Delivery (define scope first)
```

**Conversion patterns:**
- T&M to Fixed-Price: Client requests budget certainty after initial sprints → generate CO with fixed scope and price
- Fixed-Price to T&M: Scope changes exceed 20% → recommend switching to T&M for remaining work
- Flat-rate to Delivery-based: Client requests per-deliverable pricing → restructure as milestone-based with per-milestone pricing
