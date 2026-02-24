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

### PR #27 — Agent definition bulk trim (merged)
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

### PR #28 — SKILL.md restructuring into router + references (merged)
- Split 8 oversized SKILL.md files (558–1229 lines) into thin routers (<80 lines) plus `references/` directories
- Each router contains: frontmatter, description, "when to use", CONTEXT GUARD, routing table mapping user intent to reference files
- All code examples and content preserved in reference files — zero knowledge loss
- 47 reference files created across 8 plugins

**Results by file (before → after):**

| # | Plugin | Before | Router | Ref Files | Saved from context |
|---|--------|--------|--------|-----------|-------------------|
| 1 | proagent-backend | 1229 | 39 | 8 (1173 lines) | -1190 |
| 2 | proagent-data | 1194 | 49 | 7 (1099 lines) | -1145 |
| 3 | proagent-devops | 894 | 43 | 7 (800 lines) | -851 |
| 4 | proagent-ml-ai | 791 | 37 | 5 (723 lines) | -754 |
| 5 | proagent-agentic-engineering | 748 | 56 | 5 (678 lines) | -692 |
| 6 | proagent-sales | 613 | 39 | 5 (523 lines) | -574 |
| 7 | proagent-security | 609 | 37 | 6 (540 lines) | -572 |
| 8 | proagent-delivery | 558 | 45 | 4 (445 lines) | -513 |
| **Total** | | **6636** | **345** | **47 files (5981 lines)** | **-6291** |

"Saved from context" = lines no longer loaded on every skill invocation (before − router). Reference files are loaded on-demand only when matched by the routing table.

---

## Summary of All Phases

| Phase | Status | PRs | Impact |
|-------|--------|-----|--------|
| 1: Fix connector-setup | Done | #23 | Fixed the original crash |
| 2a: Add guidelines | Done | #24 | Codified rules for all future plugins |
| 2b: Fix all hooks | Done | #25 | 53 hook commands hardened, 4 safety gates fixed |
| 2c: Fix SKILL.md bash blocks | Done | #26 | -98 lines of executable code removed |
| 3: Agent definition trim | Done | #27 | 17 files trimmed, -1102 lines of duplicated content |
| 4: SKILL.md restructuring | Done | #28 | 8 files split into router + references, -6291 lines from default context |
