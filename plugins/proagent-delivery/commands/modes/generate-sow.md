# Mode: generate-sow

Generate a delivery-ready Statement of Work (SOW) from client context gathered via Slack channels and Google Drive documents.

**You produce:** A Google Doc with numbered sections following the Provectus SOW template (Purpose, Organization, Project Overview, Project Scope, Estimated Durations & Team, Payment & Fee Schedule, Project Assumptions, Signatures), ready for client review and signature.

**Announce:** "Starting SOW generation workflow. I'll gather client context, conduct a clarification interview, generate the SOW, and output it to Google Drive."

## Arguments

Parse these flags from `$ARGUMENTS`:
- `--channel=<slack-channel-name>` — Slack channel to read for client context
- `--drive=<google-drive-folder-url>` — Google Drive folder with client documents
- `--template=<path-or-drive-url>` — SOW template to use (local or Drive)
- `--type=<discovery|delivery|both>` — SOW type (default: ask during interview)
- `--with-rom` — Generate ROM estimate as appendix
- `--output=<google-drive-folder-url>` — Where to save the output Google Doc

---

## Phase 1: Source Collection

Dispatch the `sow-context-extractor` subagent to gather client context.

**If `--channel` or `--drive` provided:** Dispatch subagent with those parameters via the Task tool (model: sonnet). Read the agent definition from `agents/sow-context-extractor.md` and include it in the subagent prompt along with the channel/drive parameters.

**If neither provided:**
```
AskUserQuestion(
  header: "SOW Sources",
  question: "Where should I gather client context from?",
  options: [
    { label: "Slack + Drive", description: "I'll provide a Slack channel and Google Drive folder" },
    { label: "Drive only", description: "I'll provide a Google Drive folder with project documents" },
    { label: "Slack only", description: "I'll provide a Slack channel name" },
    { label: "Manual input", description: "I'll describe the client context directly" }
  ]
)
```

**Subagent error handling:**
- If subagent returns a partial brief (one source failed) → continue, flag the gap
- If subagent returns an empty brief → switch to manual input mode and collect context via the interview

---

## Phase 2: Context Adequacy Gate

Review the Client Context Brief from the subagent. **Do not proceed to Phase 3 until these minimums are met:**

| Required Field | Minimum | If Missing |
|---|---|---|
| Client name (legal entity) | Must be identified | Ask in Phase 3 first |
| Project name / purpose | Must have a clear statement | Ask in Phase 3 first |
| Stated requirements | At least 3 concrete items | Ask in Phase 3 first |
| Engagement model signals | Any mention | Default: ask in Phase 3 |

Identify gaps and prepare targeted questions for Phase 3.

---

## Phase 3: Clarification Interview

Present synthesized context to the SO and ask targeted questions via `AskUserQuestion`.

**Step 1 — Validate context:** Present the brief summary and ask:
> "Here's what I've gathered. Is this accurate? What should I add or correct?"

**Step 2 — SOW type** (if not provided via `--type`):
```
AskUserQuestion(
  header: "SOW Type",
  question: "What type of SOW should I generate?",
  options: [
    { label: "Delivery", description: "Full delivery with defined scope, timeline, and team" },
    { label: "Discovery", description: "Scoping engagement: requirements, architecture, roadmap (2-6 weeks)" },
    { label: "Both", description: "Discovery SOW + Delivery SOW as a pair" }
  ]
)
```

**Step 3 — Engagement model:**
```
AskUserQuestion(
  header: "Engagement",
  question: "What engagement model should this SOW use?",
  options: [
    { label: "Time & Materials", description: "Billed per sprint at fixed capacity — flexible scope, client controls priorities" },
    { label: "Fixed-Price", description: "Fixed total for defined scope — budget certainty, change orders for additions" },
    { label: "Milestone-Based", description: "Payments tied to deliverable milestones — balanced risk" }
  ]
)
```

**After engagement model is selected:** Read the corresponding reference file:
- T&M → `skills/sow-generator/references/engagement-models/time-and-materials.md`
- Fixed-Price → `skills/sow-generator/references/engagement-models/fixed-price.md`
- Milestone-Based → `skills/sow-generator/references/engagement-models/milestone-based.md`

**Step 4 — Pricing, phases, assumptions, out-of-scope:**
- Pricing structure (flat-rate per sprint/pod vs. role-based rates)
- Phase structure and timeline
- Key assumptions to validate
- Items explicitly out of scope

---

## Phase 4: SOW Draft Generation

**Step 4a — Load template:**
1. If `--template=<path>` flag provided → read that template
2. Else if `skills/sow-generator/templates/` has `.md` files → list and ask user to select
3. Else → read `skills/sow-generator/templates/sow-default.md` as the structural scaffold

**Step 4b — Read section guidance:**
Read `skills/sow-generator/references/sow-sections.md` for section-by-section writing conventions.

**Step 4c — Generate outline first:**
Generate a 1-page outline with section titles and 1-sentence scope per section. Present to the SO:
> "Here's the SOW outline. Does this structure capture the right scope before I write the full draft?"

**Step 4d — Adapt structure to SOW type:**

If the user selected **Discovery** in Phase 3 Step 2, apply these modifications to the standard structure:
- **Section 3 (Project Overview):** Frame as a scoping/assessment engagement. Focus on understanding requirements, evaluating architecture, and producing a roadmap — not building production software.
- **Section 4 (Project Scope):** Scope items are discovery deliverables: requirements document, architecture assessment, technology evaluation, roadmap with ROM estimates, recommended team composition. Use "Discovery Deliverables" instead of "Areas of Focus" or "In-Scope Activities."
- **Section 5 (Estimated Durations & Team):** Typically 2-6 weeks. Smaller team (SA + SO, possibly 1 engineer for technical spikes).
- **Section 6 (Payment):** Usually T&M or fixed-price for a short duration. Lower total cost.
- Add an **optional section** after Section 7: "Next Steps" describing how Discovery outputs feed into a Delivery SOW.

If the user selected **Both**, generate two separate SOW documents: a Discovery SOW first, then a Delivery SOW. The Delivery SOW can reference "pending Discovery outcomes" for scope items that depend on Discovery findings.

**Generate full draft** following the template structure. The standard Provectus SOW has these numbered sections:

1. **Purpose** — Legal boilerplate: effective date, parties, MSA reference
2. **Organization** — Client company description (industry, mission, context)
3. **Project Overview** — What Provectus will do and why (business drivers, objectives)
4. **Project Scope** — Methodology + detailed scope of work (areas of focus, in-scope activities, out-of-scope)
5. **Estimated Durations & Team** — Timeline, sprint structure, team composition table (Role | Allocation | Responsibility)
6. **Payment & Fee Schedule** — Engagement model, cost table, invoice schedule, termination terms
7. **Project Assumptions** — Client responsibilities, Provectus responsibilities, legal/IP/compliance clauses
8. **Signatures & Dates** — Vendor and Customer signature blocks

**Cite-your-work constraint:** Before moving to Phase 5, verify each section by citing one concrete line from your draft:
- Purpose: cite the MSA reference sentence
- Scope: cite the most specific scope item (with quantities or technologies)
- Team: cite the team table with roles and allocations
- Payment: cite the total cost or rate structure
- Assumptions: cite at least 3 client responsibilities

If you cannot cite text for any section, complete that section before proceeding.

---

## Phase 5: Review Gate

Present the full SOW draft and ask:
```
AskUserQuestion(
  header: "SOW Review",
  question: "I've generated the SOW draft. Please review it. What would you like to do?",
  options: [
    { label: "Approve", description: "The SOW is ready — write it to Google Drive" },
    { label: "Edit", description: "I'll provide specific changes to make" },
    { label: "Redo", description: "Start over with different parameters" }
  ]
)
```

- **Edit:** Apply changes, present updated draft, repeat review gate.
- **Redo:** Return to Phase 3.
- **Approve:** Proceed to Phase 6.

**Loop termination:** After 3 rounds of Edit without Approve, present a summary of all changes made and ask: "Continue editing, start fresh from Phase 3, or save the current draft as-is?"

---

## Phase 6: Output

**Primary: Google Drive**
- Use Google Drive MCP to create a new Google Doc
- File name: `[Client Name] - [Project Name] SOW - [Date]`
- If `--output` provided, create in that folder
- Share the Google Drive link with the user

**Fallback: If Google Drive MCP write fails:**
1. Write to local file at `docs/sow/{client-slug}-{date}-sow.md`
2. Output the full SOW as a markdown code block in the conversation
3. Inform the user: "Drive write failed. The SOW has been saved locally and displayed above. You can copy it to Google Drive manually."

**ROM appendix (if `--with-rom`):**
1. Extract the Project Scope (Section 4) text from the generated SOW
2. Dispatch a Task subagent (model: sonnet) with this prompt:
   - Read the skill definition from `skills/rom-estimate/SKILL.md`
   - Use the extracted scope text as the project input
   - Generate the ROM CSV and executive summary following the skill's process
3. When the subagent returns, append the ROM executive summary as a new section in the SOW (after Section 7, before Signatures)
4. Save the ROM CSV as a separate file at `docs/rom-estimation/{client-slug}-rom.csv`
5. If the subagent fails, inform the user: "ROM generation failed. The SOW has been saved without the ROM appendix. You can run `/proagent-delivery:proagent-delivery-run rom-estimate` separately."
