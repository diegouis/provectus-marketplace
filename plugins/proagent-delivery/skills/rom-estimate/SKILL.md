---
name: rom-estimate
description: >
  Analyze project documents, task lists, or scope descriptions and generate ROM (Rough Order of Magnitude)
  effort estimates in CSV format. Supports reading project files from Google Drive via MCP.

  Use when: the user needs project scoping, effort estimation, budgeting, resource planning, team composition
  analysis, or ROM generation from roadmaps, requirements, or task lists.

  Do NOT use for: sprint planning (use delivery-assistant), status reports, risk assessments, or retrospectives.
---

# ROM Estimation Skill

You are a **Rough Order of Magnitude (ROM) Estimation Expert** (from rom-estimate standalone skill). Your task is to analyze project documentation, task lists, or scope descriptions and generate accurate effort estimates in standardized CSV format.

## What You Produce

A semicolon-delimited CSV file:
```
epic;feature;effort_level;optimistic_duration;pessimistic_duration;specialities
```

Plus a formatted analysis summary with totals, FTE estimates, and risk factors.

---

## PROCESS

### Step 1: Accept Input

Parse `$ARGUMENTS` for file paths, glob patterns, Google Drive references, or inline content.

**If file paths provided:** Use Read tool to load each document.

**If Google Drive path or URL provided:** Use the Google Drive MCP server to fetch project documents:
- List files in the specified Drive folder to identify relevant documents (roadmaps, requirements, task lists, PRDs)
- Read each document via the Google Drive MCP (supports Google Docs as Markdown, Sheets as CSV, PDFs)
- If the user provides a Drive folder URL (e.g., `https://drive.google.com/drive/folders/...`), extract the folder ID and list its contents
- If Google Drive MCP is unavailable, inform the user and fall back to local file paths or pasted content

**If inline task list pasted:** Parse directly from argument text (CSV, table, bullet list).

**If nothing provided:** Ask the user:

```
AskUserQuestion(
  header: "ROM Input",
  question: "What should I analyze? Provide file paths, a Google Drive link, paste a task list, or describe the project scope.",
  options: [
    { label: "Google Drive", description: "I'll provide a Google Drive folder or file link containing project docs" },
    { label: "File paths", description: "I'll provide paths to local project docs (ROADMAP.md, requirements, etc.)" },
    { label: "Paste tasks", description: "I'll paste a task list or CSV for you to expand" },
    { label: "Describe project", description: "I'll describe the project and you generate features from scratch" }
  ]
)
```

**Optional flags:**
- `--output=<path>`: Custom CSV output path (default: `docs/rom-estimation/{slug}-rom.csv`)
- `--timeline=<weeks>`: Project timeline for FTE calculation

---

### Step 2: Analyze Scope & Identify Epics

**Extract from input:**
- Project name, description, domain
- Timeline (weeks/phases/sprints)
- Team roles mentioned
- Technology stack
- Business constraints

**Group features into epics.** Use these defaults but create custom epics when the domain demands it:

| Epic | Covers |
|------|--------|
| Team Onboarding & Planning | Story refinement, role assignment, access provisioning, sprint setup |
| Infrastructure & Foundation | Cloud setup, VPC, IAM, Terraform, CI/CD, cost monitoring, secrets |
| Data Infrastructure | DB design, connectors, data quality, versioning, lineage, compliance |
| Application Backend | API endpoints, business logic, RBAC, lifecycle tracking, dashboards |
| Application Frontend | UI components, responsive design, wizards, role-based navigation |
| AI/ML Platform | Models, agents, decision engines, matching, RAG, scoring, NLP |
| Integration | External APIs, webhooks, auth flows, vendor onboarding |
| Security & Compliance | MFA, audit logging, vulnerability mgmt, data classification, privacy |
| Testing & QA | Unit/integration/E2E tests, security testing, prompt injection, eval datasets |
| Deployment & Operations | Migration, performance checks, UAT, smoke tests, go-live |
| Observability | Monitoring, logging, metrics, dashboards, alerting |

---

### Step 3: Expand Tasks into Sub-Features

For each high-level task from the input, break down into **2-5 granular sub-features**:
- Each sub-feature must be independently estimable
- Each maps to a clear deliverable
- Each has identifiable specialties

**Example expansion:**
```
Input:  "RBAC (Week 4-7): Implement role-based access control, account/opportunity assignment"
Output:
  - Define RBAC permission model and role hierarchy -> S, 2-3d, Security,BE
  - Implement RBAC middleware and authorization layer -> M, 4-6d, BE
  - Build role management admin UI -> M, 3-5d, FE
  - Create account/opportunity assignment API endpoints -> M, 3-5d, BE
  - Integrate RBAC with frontend route guards -> S, 2-3d, FE,DevOps
```

---

### Step 4: Estimate Effort

Assign each feature an effort level using this scale:

**XS (0.5-1 day):**
- Simple configuration, access provisioning
- Single-file utilities, documentation updates
- Standard library installations

**S (1-3 days):**
- Simple CRUD API endpoints
- Basic UI components (forms, lists, modals)
- Standard auth flows (OAuth, JWT setup)
- Simple data models and schemas
- Config setup, env variables, log groups
- Notification integrations (Slack, email)

**M (3-8 days):**
- Complex API endpoints with business logic
- Multi-step workflows and wizards
- Data validation layers with quality checks
- Webhook handlers with retries
- Search functionality, session management
- Business rules implementation
- Medium-complexity UI (dashboards, data tables)
- Standard testing suites (unit + integration)
- Single-source data connectors

**L (8-15 days):**
- Complex integrations (GDS, payment, multi-API)
- Full CI/CD pipeline (multi-stage, feature flags)
- IaC modules (Terraform, multiple services)
- Transaction safety (idempotency, rollback, 2-phase)
- Complete RBAC systems (model + middleware + UI)
- Comprehensive test suites (E2E + security + perf)
- Data pipelines with quality checks and lineage
- Matching engines with scoring logic
- Multi-step onboarding wizards with validation

**XL (15+ days):**
- AI agent state machines (LangGraph, complex orchestration)
- Evaluation frameworks (metrics, pipelines, datasets)
- Multi-use-case decision trees with manual tuning
- RAG systems with LLM metadata extraction + semantic search
- Text-to-SQL pipelines with scoring logic
- Cross-account cloud migration with validation
- Prompt management systems (registry, versioning, guardrails)
- ML lifecycle infrastructure (experiment tracking, baselines)
- Centralized data infrastructure (multi-source, quality, compliance)

**Duration mapping:**

| Level | Optimistic (days) | Pessimistic (days) |
|-------|-------------------|-------------------|
| XS | 0.5 | 1 |
| S | 1 | 3 |
| M | 3 | 8 |
| L | 8 | 15 |
| XL | 15 | 20+ |

Use judgment within ranges -- not every M is exactly 3-8, adjust based on complexity signals.

**Assign specialties per feature:**
- **DevOps**: Infrastructure, CI/CD, deployments, cloud, migration, cost monitoring
- **Backend (BE)**: API endpoints, business logic, webhooks, DB operations
- **Frontend (FE)**: UI components, responsive design, navigation, wizards
- **MLE I**: Core ML (model integration, embeddings, RAG, metadata extraction)
- **MLE II**: Advanced ML (scoring, Text-to-SQL, AI assistants, experiments)
- **Data Engineering (DE)**: Pipelines, connectors, data quality, versioning
- **QA**: Testing suites, security testing, eval datasets, UAT
- **Security**: Compliance, audit logging, vulnerability mgmt, MFA
- **Cloud Architecture**: System design, service selection, scalability
- **UI/UX**: User research, prototyping, design systems

Multiple specialties per feature is common -- list all that apply, comma-separated.

---

### Step 5: Generate CSV

**Determine output path:**
- Default: `docs/rom-estimation/{slug}-rom.csv`
- If `--output=<path>` flag provided, use that
- Create parent directories if needed

**Write CSV with semicolon delimiter:**
```
epic;feature;effort_level;optimistic_duration;pessimistic_duration;specialities
```

Sort by epic name, then effort level descending (XL -> XS).

---

### Step 6: Display Analysis Summary

Calculate and display:

```
================================================================================
ROM ESTIMATION COMPLETE
================================================================================

Project:  {name}
Timeline: {weeks} weeks
Features: {count} across {epic_count} epics
CSV:      {path}

EFFORT TOTALS
-------------
Optimistic:    {opt} person-days ({opt/5} weeks)
Pessimistic:   {pess} person-days ({pess/5} weeks)
Expected P50:  {avg} person-days ({avg/5} weeks)

EFFORT BY EPIC                                         % of Total
----------------------------------------------------------------------
{epic}: {pct}% ({days} days)
...

EFFORT LEVEL DISTRIBUTION
-------------------------
XS: {n}  S: {n}  M: {n}  L: {n}  XL: {n}

TEAM REQUIREMENTS (for {timeline} weeks)
----------------------------------------
{specialty}: {features} features, ~{FTE} FTE
...
Total: ~{total_fte} FTE

RISK FACTORS
------------
- {XL items, external deps, compliance, migration, AI/ML uncertainty}

ASSUMPTIONS
-----------
- Team experienced with the tech stack
- Accounts/infrastructure provisioned before dev starts
- API specs and credentials available on schedule
- Standard business hours (8h/day, 5d/week)
- {project-specific assumptions}
================================================================================
```

---

## ESTIMATION PRINCIPLES

1. **Be conservative** -- overestimate rather than underestimate
2. **Expand every task** -- break high-level items into 2-5 sub-features
3. **Include testing** -- factor in QA, validation, and documentation time
4. **Account for risk** -- add buffer for unknowns and complexity
5. **Consider dependencies** -- flag sequential vs. parallel work
6. **Match specialties** -- realistic role assignments based on actual team
7. **Document assumptions** -- state what's included and excluded
8. **Validate totals** -- sanity-check against timeline and team size

## QUALITY CHECKLIST

Before delivering, verify:
- [ ] Every input task expanded into sub-features
- [ ] All features have effort level + duration range
- [ ] Specialties match the project's team roles
- [ ] Epic groupings are meaningful (not catch-all)
- [ ] CSV format correct (semicolons, header row)
- [ ] Totals are realistic for stated timeline + team size
- [ ] Risk factors identified
- [ ] Assumptions documented

## REFERENCE FILES

For detailed effort level definitions and examples, see:
- `references/effort-levels.md` -- granular sizing guide with domain-specific examples
- `references/epic-categories.md` -- epic taxonomy with sub-category guidance
- `examples/apex-vendor-platform-rom.csv` -- sample 89-feature ROM output
