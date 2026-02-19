# SOW Section Writing Guidance

Detailed guidance for each SOW section with Provectus-specific conventions.

---

## 1. Executive Summary

**Purpose:** Give the reader a complete picture in 60 seconds.

**Structure:**
- Paragraph 1: Client context and project purpose. Who is the client? What problem are we solving? Why now?
- Paragraph 2: Engagement overview. What will Provectus deliver? What engagement model? What timeline?

**Conventions:**
- Use the client's legal entity name (e.g., "Acme Corp, Inc." not "Acme")
- State the engagement model explicitly: "This is a Time & Materials engagement..."
- Include the total duration: "...spanning 16 weeks from project kickoff."
- Reference the number of use cases or phases: "...covering 3 use cases across 2 phases."

**Example opening:**
> Acme Corp, Inc. ("Client") engages Provectus ("Provider") to design and implement a cloud-native data platform that consolidates three legacy data sources into a unified analytics layer. This Time & Materials engagement spans 16 weeks and covers three use cases: data ingestion pipeline, real-time dashboarding, and predictive analytics.

**Anti-patterns:**
- Vague openers: "Provectus will help the client with their data needs"
- Missing engagement model
- No timeline reference
- Marketing language instead of factual description

---

## 2. Scope of Work

**Purpose:** Define exactly what Provectus will build/deliver. This is the contractual boundary.

**Structure by use case:**
```
### Use Case 1: [Name]

**Objective:** [One sentence — what business outcome does this use case deliver?]

**Scope items:**
1. [Specific deliverable or activity]
   - Description: [What exactly will be built/done]
   - Deliverable: [Tangible output]
   - Acceptance criteria: [How the client verifies completion]

2. [Next scope item...]
```

**Conventions:**
- Organize by use case, phase, or workstream — never as a flat list
- Each scope item must be independently verifiable
- Use action verbs: "Design," "Implement," "Configure," "Deploy," "Migrate"
- Include quantities where possible: "12 API endpoints," "3 data connectors," "1 admin dashboard"
- Reference technologies: "AWS Lambda," "PostgreSQL," "React," "LangChain"

**Specificity examples:**

| Vague (avoid) | Specific (use) |
|----------------|----------------|
| Build the backend | Implement REST API with 12 endpoints for user management, authentication, and data retrieval |
| Set up infrastructure | Provision AWS infrastructure: VPC, ECS Fargate cluster, RDS PostgreSQL, S3, and CloudFront CDN |
| Create dashboards | Build 4 Grafana dashboards: system health, API latency, error rates, and business KPIs |
| AI integration | Integrate GPT-4 via LangChain for document classification across 5 document types with >90% accuracy target |

---

## 3. Deliverables

**Purpose:** Enumerate every tangible output the client will receive.

**Structure:**
```
| # | Deliverable | Description | Format | Acceptance Criteria | Phase |
|---|-------------|-------------|--------|---------------------|-------|
| D1 | Architecture Design Document | System architecture, data flows, technology stack decisions | Google Doc | Reviewed and approved by client CTO | Phase 1 |
| D2 | Data Ingestion Pipeline | Automated ETL from 3 sources to data lake | Running AWS service | Processes >1M records/day with <5 min latency | Phase 2 |
```

**Conventions:**
- Number deliverables sequentially (D1, D2, D3...)
- Each deliverable maps to one or more scope items
- Format should specify the actual output type: Google Doc, GitHub repo, AWS service, Figma file
- Acceptance criteria are testable, not subjective
- Tie each deliverable to a phase or milestone

**Acceptance criteria patterns:**
- Documents: "Reviewed and approved by [role]"
- Software: "Deployed to [environment], passing [test suite], meeting [performance threshold]"
- Data: "Processing [volume] with [latency/accuracy] meeting [target]"
- Models: "Achieving [metric] >= [threshold] on [evaluation dataset]"

---

## 4. Timeline & Milestones

**Purpose:** Set expectations for when deliverables will be ready.

**Structure:**
```
### Phase 1: Discovery & Architecture (Weeks 1-4)
- **Milestone M1:** Architecture Design Approved (Week 4)
  - Deliverables: D1 (Architecture Document), D2 (Technical Specifications)
  - Acceptance gate: Client CTO sign-off
  - Dependencies: Client provides access to existing systems by Week 1

### Phase 2: Implementation (Weeks 5-12)
- **Milestone M2:** MVP Deployed to Staging (Week 8)
  - Deliverables: D3 (API), D4 (Frontend)
  - Acceptance gate: QA test suite passing, stakeholder demo completed
- **Milestone M3:** Production Release (Week 12)
  - Deliverables: D5 (Production deployment), D6 (Operations runbook)
  - Acceptance gate: Load testing passed, security scan clean
```

**Conventions:**
- Number milestones (M1, M2, M3...) for easy reference
- Each milestone has: date, deliverables, acceptance gate, dependencies
- Include buffer between phases (1 week recommended for handoff and review)
- Flag dependencies clearly: "Client must provide X by Week Y"
- For Discovery SOWs, timeline is typically 2-6 weeks
- For Delivery SOWs, phases rarely exceed 8 weeks (break longer efforts into multiple phases)

---

## 5. Team Composition & Roles

**Purpose:** Define who will work on the project, how much, and what they're responsible for.

**Structure:**
```
### Provectus Team
| Role | Seniority | Allocation | Responsibilities |
|------|-----------|------------|------------------|
| Solution Owner | Senior | 20% (8h/week) | Project governance, client communication, escalation management |
| Tech Lead | Senior | 100% | Architecture decisions, code reviews, technical mentoring |
| Backend Engineer | Mid-Senior | 100% | API development, database design, integration implementation |
| ML Engineer | Senior | 50% | Model development, evaluation, deployment pipeline |
| QA Engineer | Mid | 50% | Test strategy, automated testing, UAT coordination |

### Client Team
| Role | Responsibilities |
|------|------------------|
| Product Owner | Requirements clarification, priority decisions, acceptance sign-off |
| Technical Sponsor | Infrastructure access, security approvals, architecture review |
| Subject Matter Expert | Domain knowledge, data validation, business rule verification |
```

**Conventions:**
- Always include a Solution Owner (SO) role — this is the Provectus project lead
- Allocation in % or hours/week — be explicit
- Client-side roles are just as important — undefined client responsibilities cause delays
- For T&M engagements, allocation may flex; state the expected range
- Include ramp-up and ramp-down periods if applicable

---

## 6. Pricing & Payment Terms

**Purpose:** Define the commercial terms clearly and unambiguously.

**See `references/pricing-guidance.md` for rate card details.**

**Structure for T&M:**
```
### Rate Card
| Role | Monthly Rate | Hourly Rate |
|------|-------------|-------------|
| Solution Owner | $X,XXX | $XXX |
| Senior Engineer | $XX,XXX | $XXX |

### Estimated Investment
- Monthly run rate: $XX,XXX (based on team composition above)
- Estimated total: $XXX,XXX - $XXX,XXX (for XX weeks)
- Actual billing based on hours worked

### Payment Terms
- Invoicing: Monthly, in arrears
- Payment: Net 30 from invoice date
- Currency: USD
```

**Structure for Fixed-Price:**
```
### Project Investment
| Phase | Deliverables | Price |
|-------|-------------|-------|
| Phase 1: Discovery | D1, D2 | $XX,XXX |
| Phase 2: Implementation | D3, D4, D5 | $XXX,XXX |
| **Total** | | **$XXX,XXX** |

### Payment Schedule
| Milestone | Payment | Amount |
|-----------|---------|--------|
| Project kickoff | 30% upfront | $XX,XXX |
| M1: Architecture approved | 20% | $XX,XXX |
| M2: MVP deployed | 30% | $XX,XXX |
| M3: Production release | 20% final | $XX,XXX |

### Payment Terms
- Currency: USD
- Payment: Net 30 from milestone acceptance
```

**Conventions:**
- Always state currency
- For T&M, provide an estimated range (not just a single number)
- For fixed-price, tie payments to milestones with clear acceptance gates
- Include travel and expenses policy: "Travel expenses billed at cost with prior client approval"
- State what is NOT included: "Hardware costs, third-party license fees, and cloud infrastructure costs are the Client's responsibility"

---

## 7. Assumptions & Dependencies

**Purpose:** Document conditions that must be true for the SOW to be valid.

**Categories:**

**Technical assumptions:**
- Cloud accounts and infrastructure provisioned before development starts
- Required API credentials and access provided by [date]
- Development, staging, and production environments available
- Client systems meet specified compatibility requirements

**Client dependencies:**
- Product Owner available for weekly sprint reviews
- Technical Sponsor provides infrastructure access within 5 business days of request
- Business rules and data validation logic provided before Phase 2
- Acceptance testing feedback provided within 5 business days of deliverable submission

**Timeline assumptions:**
- Project starts on [date]
- Team members available as specified in Team Composition
- Standard business hours (8h/day, 5d/week)
- No extended holidays or company shutdowns during the engagement
- Scope changes processed through Change Management (Section 8)

**Conventions:**
- Each assumption should be testable — can you verify it's true or false?
- Client dependencies should have timing ("within X business days")
- Include consequences: "If [dependency] is not met, timeline may shift by [impact]"
- Keep this section separate from scope — assumptions buried in scope text get missed

---

## 8. Change Management Process

**Purpose:** Define how scope changes are handled to prevent uncontrolled scope creep.

**Standard process:**
```
1. **Request:** Either party submits a Change Request (CR) describing the change, reason, and expected impact
2. **Assessment:** Provectus evaluates impact on timeline, budget, resources, and quality within 3 business days
3. **Proposal:** Provectus provides a Change Order (CO) with revised scope, timeline, and cost
4. **Approval:** Both parties sign the Change Order before work begins
5. **Execution:** Approved changes are incorporated into the project plan
```

**Conventions:**
- Define who can submit change requests (named roles, not "anyone")
- Include assessment SLA (typically 3-5 business days)
- State that no changed scope work begins until the CO is signed
- For T&M engagements, clarify that priority changes within the existing scope are normal and don't require COs
- For fixed-price, any scope addition triggers a CO

---

## 9. Acceptance Criteria

**Purpose:** Define how the client formally accepts deliverables.

**Standard process:**
```
1. **Submission:** Provectus delivers the deliverable and notifies the Client
2. **Review period:** Client reviews within [X] business days (typically 5-10)
3. **Feedback:** Client provides written acceptance or specific, actionable feedback
4. **Remediation:** Provectus addresses feedback within [X] business days
5. **Final acceptance:** Client signs off on the deliverable
6. **Deemed acceptance:** If no feedback is provided within the review period, the deliverable is deemed accepted
```

**Conventions:**
- Define review period length (5-10 business days is standard)
- Include deemed acceptance clause — prevents indefinite review cycles
- Feedback must be "specific and actionable" — no vague rejections
- Define warranty/support period post-acceptance (typically 30 days for bug fixes)
- Final acceptance of all deliverables triggers project completion
