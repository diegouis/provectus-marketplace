# Mode: sow-review

Audit an existing Statement of Work for completeness, quality, and internal consistency against Provectus SOW conventions.

**You produce:** A structured audit report with section-by-section quality scores and actionable recommendations.

**Announce:** "Starting SOW review. I'll assess the document against Provectus quality criteria for completeness, specificity, pricing alignment, and risk coverage."

## Process

### 1. Load the SOW

- If `$ARGUMENTS` includes a file path or Google Drive link, read the SOW from that location
- Otherwise, search for recent SOW files in the project directory or ask the user for the path
- Parse the document into sections

### 2. Section Completeness

Verify all standard Provectus SOW sections are present:

| # | Section | Required | Notes |
|---|---------|----------|-------|
| 1 | Purpose | Yes | Legal boilerplate, MSA reference, effective date |
| 2 | Organization | Yes | Client company description |
| 3 | Project Overview | Yes | What and why |
| 4 | Project Scope | Yes | Methodology + scope of work + out-of-scope |
| 5 | Estimated Durations & Team | Yes | Timeline, sprints, team table |
| 6 | Payment & Fee Schedule | Yes | Cost, invoice schedule, termination |
| 7 | Project Assumptions | Yes | Client/Provectus responsibilities, legal |
| 8 | Signatures & Dates | Yes | Both parties |
| — | Completion/Success Criteria | Optional | Some SOWs include this |
| — | Referenceability | Optional | Marketing permission clause |
| — | Solution Architecture | Optional | For complex technical engagements |

### 3. Scope Specificity

For each scope item:

| Quality | Example | Verdict |
|---|---|---|
| Strong | "Implement 12 REST API endpoints for user management with JWT authentication" | Pass |
| Adequate | "Implement role-based access control with admin UI" | Pass |
| Weak | "Build the backend" | Fail — flag for revision |

Check: action verbs, quantities, technology references, verifiable completion criteria.

### 4. Team & Timeline Realism

- Does team size match scope complexity?
- Are all required specialties covered?
- Is timeline proportional? Heuristic: `(scope person-days) / (team FTEs) <= (calendar days x 0.7)`
- If a ROM estimate is available, cross-check alignment

### 5. Pricing Alignment

- Does pricing model match engagement model (T&M = rate/sprint, Fixed = total + milestones)?
- Does `cost per sprint × sprints = total cost`?
- Is invoice schedule defined with dates and amounts?
- Are termination terms included?
- Are excluded costs stated (cloud, licenses, hardware)?

### 6. Assumptions Review

- Are standard Provectus assumptions present (SME access, timely review, business hours, subcontractors)?
- Are client-specific assumptions included (data residency, compliance, IP ownership)?
- Are consequences stated for assumption violations ("may add time and cost")?

### 7. Output Audit Report

```
## SOW Review: [Client Name] - [Project Name]
Review Date: [Date]
Source: [file path or Drive link]

### Section Completeness
| # | Section | Present | Quality | Notes |
|---|---------|---------|---------|-------|
| 1 | Purpose | Yes/No | Strong/Adequate/Weak | [context] |
| 2 | Organization | Yes/No | Strong/Adequate/Weak | [context] |
| ... | ... | ... | ... | ... |

### Scope Issues
| Scope Item | Issue | Recommendation |
|---|---|---|
| [item] | [too vague / missing quantities] | [specific fix] |

### Timeline & Team Assessment
- Team vs. scope: [Adequate / Under-staffed / Over-staffed]
- Timeline vs. scope: [Realistic / Aggressive / Conservative]
- Specialty gaps: [None / Missing: X, Y]

### Pricing Assessment
- Math check: [Correct / Error in X]
- Terms: [Complete / Missing: X]
- Excluded costs: [Listed / Missing]

### Assumptions Gaps
- Missing standard assumptions: [list]
- Missing client-specific items: [list]

### Recommendations
1. [Most critical fix]
2. [Second priority]
3. [Third priority]

### Overall SOW Quality
**[READY FOR CLIENT / NEEDS REVISION / MAJOR GAPS]**
[2-3 sentence summary]
```
