# Skill Safety Remediation Plan

Full audit and remediation of all plugins for context explosion risks, following PLUGIN-DESIGN-GUIDELINES.md §2 (Skill Safety).

---

## Completed

### PR #23 — Fix connector-setup skill (merged)
- Rewrote SKILL.md as lightweight router (~60 lines, down from 110)
- Added "ask first, load later" guard
- Hardened hooks.json with jq guard
- Added CONTEXT GUARDs to mode files
- Trimmed agent definition duplication

### PR #24 — Added §2 Skill Safety guidelines (merged)
- Added 6 rules to PLUGIN-DESIGN-GUIDELINES.md under new §2
- Renumbered all subsequent sections (§3–§9)

### PR #25 — Added jq guards to all 17 plugin hooks (merged)
- Added `which jq >/dev/null 2>&1 || exit 0` to all 53 hook commands across 17 plugins
- Fixed `grep -oP` (GNU-only) in proagent-sdlc with portable `sed -nE`
- Critical: 4 blocking safety hooks (ml-ai, hr, aws-ai, documentation) were silently failing without jq

### PR #26 — Removed executable bash blocks from 5 SKILL.md files (merged)
- proagent-documentation (CRITICAL): Removed `find / + source .env`, `git clone` with token, `curl` with credentials
- proagent-data (HIGH): Added lazy-load guards to 7 external SKILL.md path references
- proagent-delivery/rom-estimate (MEDIUM): Added CONTEXT GUARD to reference files section
- proagent-ml-ai (MEDIUM): Converted pip install + export bash block to prose
- proagent-security (MEDIUM): Converted npm audit/trivy bash block to bullet list
- Net: -98 lines of executable code removed

---

### PR #27 — Agent definition bulk trim (pending merge)
- Replaced inline knowledge sections in 17 agent definitions with delegation pointers to SKILL.md
- Pattern: `## Technical Knowledge` → list of `→ skills/*/SKILL.md` pointers + `CLAUDE.md`
- Also removed redundant Identity section and External Skill References table from hr-specialist
- Preserved: frontmatter (including discovery examples), Core Identity, Behavioral Guidelines, Response Format
- Skipped 8 correctly scoped sub-agents (cv-parser, cv-skills-matcher, etc.)

**Results by file (before → after):**

| # | File | Before | After | Saved |
|---|------|--------|-------|-------|
| 1 | confluence-publisher.md | 186 | 37 | -149 |
| 2 | agentic-engineering-specialist.md | 180 | 140 | -40 |
| 3 | aws-ai-specialist.md | 163 | 54 | -109 |
| 4 | delivery-specialist.md | 163 | 43 | -120 |
| 5 | finance-specialist.md | 144 | 42 | -102 |
| 6 | security-specialist.md | 130 | 56 | -74 |
| 7 | hr-specialist.md | 129 | 51 | -78 |
| 8 | platform-specialist.md | 127 | 93 | -34 |
| 9 | data-specialist.md | 125 | 53 | -72 |
| 10 | sales-specialist.md | 122 | 54 | -68 |
| 11 | frontend-specialist.md | 119 | 58 | -61 |
| 12 | backend-specialist.md | 116 | 55 | -61 |
| 13 | ml-ai-specialist.md | 112 | 55 | -57 |
| 14 | sdlc-specialist.md | 111 | 40 | -71 |
| 15 | qa-specialist.md | 102 | 58 | -44 |
| 16 | devops-specialist.md | 95 | 52 | -43 |
| 17 | documentation-specialist.md | 74 | 55 | -19 |
| **Total** | | **2098** | **996** | **-1102** |

Note: agentic-engineering (140) and platform (93) appear higher because their frontmatter contains 5 and 3 discovery `<example>` blocks respectively, which are required for agent discovery and were preserved.

---

## Phase 4: Oversized SKILL.md Restructuring (Optional, Larger Effort)

**Goal:** Restructure the largest knowledge-base SKILL.md files into a router + reference files architecture.

These files are too large but don't have executable bash blocks (those were fixed in PR #26). They're pure knowledge bases that load 800–1200 lines of reference material into context on every invocation. The fix is to split them into a thin SKILL.md router (<80 lines) plus reference files loaded at point-of-need.

### Files to restructure

| # | File | Lines | Proposed Split |
|---|------|-------|----------------|
| 1 | `proagent-backend/skills/backend-assistant/SKILL.md` | 1229 | Router + references/api-patterns.md, references/database-patterns.md, references/auth-patterns.md, references/deployment-patterns.md |
| 2 | `proagent-data/skills/data-assistant/SKILL.md` | 1194 | Router + references/pipeline-patterns.md, references/dbt-patterns.md, references/sql-optimization.md, references/quality-framework.md, references/spark-patterns.md |
| 3 | `proagent-devops/skills/devops-assistant/SKILL.md` | 894 | Router + references/cicd-patterns.md, references/k8s-patterns.md, references/iac-patterns.md, references/monitoring-patterns.md |
| 4 | `proagent-ml-ai/skills/ml-ai-assistant/SKILL.md` | 791 | Router + references/training-patterns.md, references/deployment-patterns.md, references/llm-patterns.md, references/monitoring-patterns.md |
| 5 | `proagent-agentic-engineering/skills/agentic-engineering-assistant/SKILL.md` | 748 | Router + references/component-architecture.md, references/orchestration-patterns.md, references/prompt-engineering.md |
| 6 | `proagent-sales/skills/sales-assistant/SKILL.md` | 613 | Router + references/proposal-patterns.md, references/pricing-patterns.md, references/research-patterns.md |
| 7 | `proagent-security/skills/security-assistant/SKILL.md` | 609 | Router + references/vulnerability-scanning.md, references/compliance-frameworks.md, references/owasp-patterns.md |
| 8 | `proagent-delivery/skills/delivery-assistant/SKILL.md` | 558 | Router + references/sprint-patterns.md, references/reporting-patterns.md, references/stakeholder-patterns.md |

**Approach per file:**
1. Create a thin SKILL.md (<80 lines): frontmatter, description, "when to use", routing table mapping user intent to reference files
2. Move each major section into its own `references/` file
3. Add CONTEXT GUARD notes at each routing point
4. Verify the skill still works by invoking it and requesting each topic

**This phase is optional and can be done incrementally — one plugin at a time.**

---

## Summary of All Phases

| Phase | Status | PRs | Impact |
|-------|--------|-----|--------|
| 1: Fix connector-setup | Done | #23 | Fixed the original crash |
| 2a: Add guidelines | Done | #24 | Codified rules for all future plugins |
| 2b: Fix all hooks | Done | #25 | 53 hook commands hardened, 4 safety gates fixed |
| 2c: Fix SKILL.md bash blocks | Done | #26 | -98 lines of executable code removed |
| 3: Agent definition trim | Done | #27 (pending merge) | 17 files trimmed, -1102 lines of duplicated content |
| 4: SKILL.md restructuring | TODO (optional) | TBD | ~8 files split into router + references |
