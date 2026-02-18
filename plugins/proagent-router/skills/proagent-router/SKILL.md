---
name: proagent-router
description: Use when the user invokes /proagent to route their request to the appropriate Provectus practice specialist. Detects the domain from the user's input and dispatches to the correct practice plugin for execution.
---

# ProAgent Router

Single entry point for all Provectus practice capabilities. Detects the domain from the user's request and dispatches to the appropriate specialist agent.

## How Routing Works

When the user invokes `/proagent`, follow this process:

### Step 1: Parse the User's Request

Read the user's input after `/proagent` and identify:
- **What** they want to do (build, review, deploy, plan, analyze, etc.)
- **What domain** it falls under (infrastructure, code, data, models, security, etc.)
- **What artifacts** are mentioned (pipelines, APIs, models, tests, reports, etc.)

### Step 2: Match to Practice Domain

Use the routing table below to identify the best-matching practice. Match based on **keywords, artifacts, and intent** — not just exact words.

| Practice | Domain Signals | Example Requests |
|----------|---------------|------------------|
| **agentic-engineering** | Claude Code extensions, MCP servers, multi-agent workflows, prompt engineering, agent systems, plugins, skills | "build an MCP server", "create a Claude plugin", "design a multi-agent workflow" |
| **sdlc** | Architecture, code review, testing strategy, release management, documentation, git workflows, ADRs | "review this PR", "plan the release", "write an ADR", "set up git workflow" |
| **platform** | Developer platforms, service catalogs, golden paths, scaffolding, internal tooling, DX | "create a service template", "build a developer portal", "scaffold a new project" |
| **devops** | CI/CD, Docker, Kubernetes, Terraform, IaC, monitoring, incident response, cloud ops, pipelines | "set up CI/CD", "deploy to k8s", "write Terraform", "configure monitoring" |
| **qa** | Test automation, Playwright, Cypress, regression testing, coverage, E2E, accessibility, WCAG | "write E2E tests", "set up Playwright", "improve test coverage", "accessibility audit" |
| **backend** | APIs, databases, microservices, auth, caching, queues, REST, GraphQL, performance | "build a REST API", "optimize database queries", "add authentication", "set up Redis caching" |
| **frontend** | React, Vue, Angular, design systems, responsive design, CSS, components, UI/UX | "build a React component", "create a design system", "fix responsive layout" |
| **delivery** | Sprint planning, milestones, status reports, risk management, stakeholder comms, estimation, retrospectives | "plan the sprint", "write a status report", "estimate this project", "run a retro" |
| **security** | Vulnerability scanning, compliance, secrets management, threat modeling, OWASP, Zero Trust, pen testing | "scan for vulnerabilities", "threat model this system", "audit secrets management" |
| **data** | ETL/ELT, dbt, Airflow, data warehousing, SQL optimization, data quality, pipelines | "build a data pipeline", "optimize SQL queries", "set up dbt models", "data quality checks" |
| **ml-ai** | Model training, MLOps, experiment tracking, LLM apps, RAG, embeddings, vector stores, inference | "train a model", "build a RAG system", "deploy to SageMaker", "set up MLflow" |
| **aws-ai** | Amazon Bedrock, AgentCore, AWS AI services, CDK for AI, Knowledge Bases, AWS architecture | "build a Bedrock agent", "set up AWS Knowledge Base", "design AI architecture on AWS" |
| **hr** | Hiring, interviews, onboarding, performance reviews, compensation, CV validation, employee development | "screen these CVs", "plan onboarding", "write interview questions", "performance review" |
| **sales** | Proposals, RFPs, competitive analysis, lead research, pipeline management, quotes | "write a proposal", "respond to this RFP", "research this lead", "competitive analysis" |
| **finance** | Budgeting, invoicing, forecasting, P&L analysis, cost optimization, financial reporting | "create a budget", "forecast revenue", "analyze P&L", "optimize cloud costs" |

### Step 3: Handle Ambiguity

**Single domain detected:** Dispatch directly to the specialist.

**Multiple domains detected:** Present the matches and ask the user to confirm:
```
I detected multiple relevant practices for your request:
1. **DevOps** — for the CI/CD pipeline setup
2. **Backend** — for the API deployment configuration

Which practice should I route to? Or should I coordinate across both?
```

**No clear match:** Ask the user to clarify:
```
I couldn't determine the best practice for your request.
Could you tell me more about what you're trying to accomplish?

Available practices: agentic-engineering, sdlc, platform, devops, qa,
backend, frontend, delivery, security, data, ml-ai, aws-ai, hr, sales, finance
```

### Step 4: Dispatch to Specialist

Once the practice is identified, dispatch using the Task tool with the practice's specialist agent:

**Routing map to specialist agents:**

| Practice | Agent Name | Agent Type |
|----------|-----------|------------|
| agentic-engineering | `proagent-agentic-engineering:agentic-engineering-specialist` | Task (subagent_type) |
| sdlc | `proagent-sdlc:sdlc-specialist` | Task (subagent_type) |
| platform | `proagent-platform:platform-specialist` | Task (subagent_type) |
| devops | `proagent-devops:devops-specialist` | Task (subagent_type) |
| qa | `proagent-qa:qa-specialist` | Task (subagent_type) |
| backend | `proagent-backend:backend-specialist` | Task (subagent_type) |
| frontend | `proagent-frontend:frontend-specialist` | Task (subagent_type) |
| delivery | `proagent-delivery:delivery-specialist` | Task (subagent_type) |
| security | `proagent-security:security-specialist` | Task (subagent_type) |
| data | `proagent-data:data-specialist` | Task (subagent_type) |
| ml-ai | `proagent-ml-ai:ml-ai-specialist` | Task (subagent_type) |
| aws-ai | `proagent-aws-ai:aws-ai-specialist` | Task (subagent_type) |
| hr | `proagent-hr:hr-specialist` | Task (subagent_type) |
| sales | `proagent-sales:sales-specialist` | Task (subagent_type) |
| finance | `proagent-finance:finance-specialist` | Task (subagent_type) |

**Dispatch format:**
1. Announce the detected practice: "Routing to **[Practice Name]** specialist..."
2. Use the Task tool to dispatch to the specialist agent with the user's full request as the prompt
3. Return the specialist's response to the user

### Step 5: Cross-Practice Coordination

When a request spans multiple practices (e.g., "deploy an ML model with monitoring"):

1. Identify the **primary** practice (the one doing the main work)
2. Identify **supporting** practices (providing auxiliary capabilities)
3. Dispatch to the primary specialist first
4. If the primary specialist needs support from another domain, dispatch a second agent in parallel
5. Synthesize results from both agents into a coherent response

## Routing Priority Rules

When multiple practices could match, use these tiebreakers:

1. **Specificity wins** — "deploy a Bedrock agent" matches `aws-ai` over `devops` because it's more specific
2. **Artifact type wins** — "review my model training code" matches `ml-ai` (artifact = model) over `sdlc` (action = review)
3. **User history wins** — if the user has been working in a specific domain during the session, prefer that domain for ambiguous requests
4. **Ask when tied** — if two practices are equally valid, ask the user rather than guessing

## Quick Reference for Common Patterns

| User Says... | Route To |
|--------------|----------|
| "help me with..." + technical domain | Match domain from table |
| "review this..." | `sdlc` for code/PR review, domain-specific for artifacts (e.g., `ml-ai` for model review) |
| "deploy..." | `devops` for infra, `ml-ai` for models, `aws-ai` for AWS-specific |
| "test..." | `qa` for test automation, domain-specific for unit tests within that domain |
| "plan..." | `delivery` for project planning, `sdlc` for architecture planning |
| "build..." | Match based on what's being built (API = backend, UI = frontend, pipeline = data/devops) |
| "estimate..." | `delivery` for ROM/project estimation |
| "secure..." / "scan..." | `security` |
| "hire..." / "interview..." | `hr` |
| "proposal..." / "RFP..." | `sales` |
| "budget..." / "invoice..." | `finance` |
