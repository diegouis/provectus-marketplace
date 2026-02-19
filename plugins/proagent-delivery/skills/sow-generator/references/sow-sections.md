# SOW Section Writing Guidance

Section-by-section conventions for the standard Provectus SOW structure. Based on analysis of 5 real signed/draft SOWs (Natera #28, Natera #30, GANT #3, Johnson Lambert, Fincredibilizer #2).

---

## 1. Purpose

**What it does:** Legal boilerplate establishing the SOW, parties, effective date, and MSA reference.

**Standard language (copy and customize):**
> This Statement of Work ("SOW") is dated as of [DATE] ("Effective Date") by and between Provectus IT, Inc. ("Provectus" or "Vendor") and [CLIENT LEGAL NAME] ("Customer" or "[SHORT NAME]"). The purpose of this SOW is to describe the services that Provectus will provide to the Customer under the terms and conditions of the Master Services Agreement ("MSA") between the parties, dated [MSA DATE].

**Conventions:**
- Always include the SOW number: "Statement of Work #[N]"
- Use legal entity names with abbreviations defined in parentheses
- Reference the MSA date — this is a legal requirement

---

## 2. Organization

**What it does:** Client company description — who they are, what they do, why it matters.

**Real example (Natera):**
> Natera, Inc. is a clinical genetic testing company specializing in non-invasive, cell-free DNA (cfDNA) testing technology, focusing on women's health, cancer, and organ health. Natera's proprietary technology combines novel molecular biology techniques with a suite of bioinformatics software that allows detection down to a single molecule in a tube of blood.

**Real example (GANT):**
> Gant Travel is a digitally driven, data-focused corporate travel management company that delivers end-to-end solutions for business travel, meetings, and expense optimization. With a strong focus on technology and user experience, Gant leverages data insights to simplify travel management and enhance traveler satisfaction.

**Conventions:**
- 1-2 paragraphs
- Include industry, core business, and technology context relevant to the engagement
- May include "Business Drivers & Key Challenges" sub-section for complex engagements (see GANT example)
- Tone: factual, not promotional

---

## 3. Project Overview

**What it does:** High-level summary of what Provectus will do and why.

**Real example (Natera #30):**
> Provectus will partner with Natera's Shopfloor Engineering and AI teams to advance the development and operationalization of prioritized GenAI initiatives aligned to lab productivity, automation, and data unification. This engagement is structured as a capacity-based, agile delivery model that enables Provectus to flexibly support a dynamic backlog of use cases.

**Real example (Fincredibilizer):**
> The Fincredibilizer MVP establishes a production-ready platform that transforms portfolio management into a scalable, data-driven growth engine. By integrating structured, unstructured, and public data sources, it builds rich client profiles and continuously identifies high-impact opportunities across finance and operations.

**Conventions:**
- 2-3 paragraphs
- First paragraph: what Provectus will do
- Second paragraph: business objectives and strategic alignment
- Third paragraph (optional): engagement structure and approach
- Reference specific technology domains (GenAI, ML, data platform, etc.)

---

## 4. Project Scope

**What it does:** The contractual boundary — exactly what is and isn't included.

**Sub-sections (standard pattern):**

### 4.1 Methodology
Standard opening: "Provectus will collaborate closely with [Client] and follow the methodology and/or practices of the existing team."

### 4.2 Scope of Work
Organized as **numbered areas of focus** (T&M) or **detailed use cases** (Fixed-Price).

**T&M pattern (Natera #28 — lean):**
```
Potential Areas of Focus:
1. Ingestion Expansion — Add Women's Health, Organ Health, and expanded xCures/Kno2 pipelines.
2. New Use Cases — Support ClinVerify Billing, Appeals evidence retrieval, and downstream workflows.
3. Retrieval Enhancements — Enable delta-by-timepoint document retrieval and date-range queries.
4. Scalability & Operations — Scale throughput for post-launch load and improve maintenance efficiency.
```

**Fixed-Price pattern (GANT — detailed):**
```
In-Scope Activities:
1. MLP Phase 1 - Booking (Flight, Hotel, Auto Search)
   - Identity-Aware Sessions: The system assumes a User ID is passed from the TalkDesk login context.
   - Permission Logic: The ID is validated to differentiate between Primary Traveler and Traveler Arranger.
   - Search Flow: The agent calls GANT APIs in sequence...
   - Hotel Sub-flow: A 5-API sequence will be implemented:
     1. City search for baseline pricing
     2. Geo-location filtering
     3. Hotel selection for live pricing
     4. Content retrieval for descriptions and imagery
     5. Session preparation for checkout
```

### Out of Scope
Always include. Real example (GANT):
```
- Actual booking creation and email confirmations
- Payment Processing: All checkout/refunds happen in the GANT Portal
- TSA Integration: Due to high complexity and low immediate value
- User Authentication: Assumed to be handled prior to the chat session
- Multi-city trips booking
- Group booking
```

**Specificity Do/Don't:**

| Don't | Do |
|---|---|
| "Build the backend" | "Implement REST API with 12 endpoints for user management with JWT authentication" |
| "Set up infrastructure" | "Provision AWS environments (Dev, STG, PROD) including AgentCore Runtime, DynamoDB, and Secrets Manager" |
| "AI integration" | "Implement Model Context Protocol (MCP) tools for flight and hotel searches directly with GANT APIs" |
| "Add monitoring" | "Expand visibility into operational bottlenecks, aging samples, and equipment performance" |

---

## 5. Estimated Durations & Team

**What it does:** Timeline, sprint structure, and team composition.

**Standard opening:**
> This project phase will be timeboxed to [DURATION] ([N] [2-week sprints]). The project will start on [START DATE] and end on [END DATE].

**Team table (standard Provectus format):**

| Role | Allocation | Responsibility |
|------|------------|----------------|
| Solution Architect (100%) | Full-time | Designing and overseeing technical architecture, developing solution designs, ensuring alignment between business requirements and technical implementations |
| Solution Owner (10%) | Part-time | Primary interface between client and team, prioritizing requirements, managing expectations, facilitating decision-making |

**Conventions:**
- Allocation as percentage in the role name: "Solution Architect (100%)"
- Responsibility column: multi-sentence description of what this role does
- Always include Solution Owner (SO) — typically 10-25%
- May include delivery model narrative explaining why the team is structured this way
- For AWS-funded engagements, may include TCO calculation sub-section

---

## 6. Payment and Fee Schedule

**What it does:** Commercial terms — pricing, invoicing, termination.

**T&M opening pattern:**
> Time & Materials. Provectus estimates that [Client]'s total payment under this Statement of Work will be $[AMOUNT] unless specified through a change order and following the prescribed [Client] change order process.

**Fixed-price opening pattern:**
> Fixed Fee. [Client] total payment under this Statement of Work will be $[AMOUNT] unless specified through a change order and following the prescribed change order process.

**Cost table (real example — Natera):**

| Description | Duration (Sprints) | Cost per Sprint | Estimated Total Cost |
|---|---|---|---|
| AI Pod | 6 | $16,560 | $99,360 |
| | | **Total Cost** | **$99,360** |

**Invoice schedule (real example — Natera):**

| Invoice Date | Description | Cost |
|---|---|---|
| 2/1/2026 | Services rendered in January | $16,560 |
| 3/1/2026 | Services rendered in February | $33,120 |
| 4/1/2026 | Services rendered in March | $33,120 |
| 5/1/2026 | Services rendered in April | $16,560 |

**Termination clause (standard):**
> If the Customer wishes to terminate this SOW without cause, the Customer must provide the Vendor with thirty (30) days' written notice (email is acceptable). Notwithstanding the above, Customer will be responsible for the prorated fee for the remaining term from the date of the termination notice until the termination date.

---

## 7. Project Assumptions

**What it does:** Conditions that must hold true. This is the longest section and contains both operational assumptions and legal clauses.

**Standard assumptions (present in all 5 sample SOWs — include by default):**

**Client responsibilities:**
- Provide access to SMEs and resources required for project work
- Provide access to cloud infrastructure, datasets, and tools
- Review and sign-off deliverables in a timely manner
- Align incentives of employees and vendors to cooperate with Provectus
- Provide appropriate system access for reviewing configurations
- Provide timely access to technical information and environments

**Provectus limitations:**
- Not responsible for products not provided by or tasks not performed by Provectus consultants
- Not responsible for third-party software/hardware bugs, incompatibilities, or defects
- Not responsible for delays, errors, or omissions caused by other parties

**Operational:**
- Normal business hours (8:00 am to 5:00 pm local time), Mon-Fri, except holidays
- Schedule estimates represent commercially reasonable technical judgment
- Work commences on mutually agreeable date after fully executed SOW
- May use subcontractors where appropriate

**Acceptance and scope:**
- Deliverables deemed accepted upon delivery unless otherwise noted in writing
- Only tasks in this SOW will be undertaken
- Customer signs project completion form upon completion

**Termination:**
- Customer may terminate with prior notice for non-performance
- All fees and expenses to date of termination will be invoiced

**Client-specific additions (varies by engagement):**
- Data residency requirements (Natera: "data will not be moved outside the US")
- IP/compliance clauses (Natera: patient re-identification prohibition, AI data ownership)
- Security clearance coordination
- Referenceability clause (Johnson Lambert)
- Completion/success criteria (Fincredibilizer, Johnson Lambert)

---

## 8. Signatures and Dates

Standard two-column layout: VENDOR (Provectus IT, Inc.) and CUSTOMER ([Client]).

Fields: Signature, Printed Name, Title, Date.

---

## Optional Sections

Some SOWs include additional sections based on engagement complexity:

| Section | When to Include | Example |
|---|---|---|
| Completion/Success Criteria | Fixed-price MVPs | Fincredibilizer: "The MVP will be deemed successful if..." |
| Solution Architecture | Complex technical engagements | Fincredibilizer: architecture diagram + TCO |
| Referenceability | When marketing permission is negotiated | Johnson Lambert |
| Target State Architecture | When scope is Phase 1 of a larger vision | GANT: future capabilities designed but not built |
| AWS TCO | AWS-funded engagements | Natera #30 |
