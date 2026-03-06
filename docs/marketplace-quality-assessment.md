# Provectus Marketplace: Plugin Quality & Maturity Assessment

**Date**: 2026-02-20 (revised 2026-03-06)
**Repository**: `provectus-marketplace`
**Scope**: 18 Claude Code plugins (16 practice-specific + 1 router + 1 setup) intended for non-technical Cowork users
**Source**: 867 cataloged assets across 16 Provectus repositories

---

## Summary

The marketplace has **excellent scaffolding** -- consistent architecture, naming, security, documentation templates across all 18 plugins. But the content ranges from battle-tested to first-draft, and no plugins are production-ready for the stated audience (non-technical Cowork users) without hardening.

> **2026-03-06 revision notes:** Since the original assessment, SKILL.md files were restructured (PR #28) to follow the <80-line router pattern, agent definitions were deduplicated (PR #27), context guards were added (PR #26), hook jq guards were fixed (PR #25), CI validation was added (PR #36), a release pipeline with Slack notifications was added (PR #39), HR gained a full candidate lifecycle pipeline (PR #32), and proagent-ae was bumped to v1.0.0 (PR #33). Updated data points are marked with [updated] below.

| Dimension | Rating |
|-----------|--------|
| Architecture & consistency | Excellent |
| Naming conventions | Excellent |
| Hook safety | Excellent |
| Tool restrictions | Very Good |
| Security hygiene | Strong |
| Design guidelines | Excellent |
| Content depth (varies) | Mixed |
| Non-technical user readiness | Not Ready |
| External reference integrity | 200+ broken refs |

---

## Critical Issues

### Issue 1: 200+ Broken External References

Every SKILL.md and agent file references external Provectus repos that don't exist in this marketplace. Users installing plugins see references to inaccessible files.

| External Repo | Broken Refs | Affected Plugins |
|---------------|:-----------:|------------------|
| `agents/plugins/*` | 45+ | devops, backend, security, qa, ml-ai, data, sdlc, platform, hr |
| `casdk-harness/*` | 15+ | devops, backend, data, security, ml-ai, qa |
| `proagent-repo/*` | 12+ | sdlc, qa, security, ml-ai, data, agentic-eng |
| `taches-cc-resources/*` | 10+ | ml-ai, backend, qa, frontend, agentic-eng |
| `awesome-claude-skills/*` | 15+ | ml-ai, frontend, finance, hr, qa, platform |
| `ralph-orchestrator/*` | 8+ | sdlc, ml-ai, qa, backend |
| `Auto-Claude/*` | 8+ | devops, security, ml-ai, backend, frontend |
| Others (awos, claude-ui, gastown, superpowers, planning-with-files, awesome-claude-code) | 15+ | Various |

**Only 4 plugins have zero broken refs:** documentation, router, aws-ai, sales.

**Worst offenders by plugin:**
- proagent-devops: 18 broken refs
- proagent-backend: 17 broken refs
- proagent-security: 15 broken refs
- proagent-qa: 14 broken refs
- proagent-ml-ai: 12 broken refs

### Issue 2: Not Ready for Non-Technical Users

Plugins assume domain expertise and technical setup that non-technical Cowork users won't have.

| Plugin | Jargon | MCP Deps | Error Handling | Guardrails | Fitness |
|--------|:------:|:--------:|:--------------:|:----------:|:-------:|
| **security** | CRITICAL | CRITICAL | CRITICAL | CRITICAL | **Fails** |
| **hr** | CRITICAL | HIGH | MEDIUM | CRITICAL | Not Ready |
| **delivery** | MED-HIGH | HIGH | HIGH | CRITICAL | Not Ready |
| **finance** | MED-HIGH | MEDIUM | MEDIUM | HIGH | Not Ready |
| **documentation** | MEDIUM | MEDIUM | MED-HIGH | MEDIUM | Borderline |
| **sales** | MEDIUM | LOW | MEDIUM | MEDIUM | Borderline |
| **router** | LOW | N/A | MEDIUM | MEDIUM | Ready |

**Key failures:**

1. **Security plugin requires 7 CLI tools** (bandit, trivy, semgrep, govulncheck, pip-audit, gh, glab) that non-technical users cannot install. No fallback workflow exists.

2. **No graceful MCP degradation anywhere.** If Slack/Drive/Jira/Confluence aren't configured, plugins fail silently rather than explaining what the user needs to set up.

3. **High-stakes operations lack approval gates.** SOW generation can overwrite client docs. CV screening makes hiring recommendations without audit trails. Finance analysis reveals salary data without access controls. Confluence publishing pushes directly without review.

4. **Domain jargon throughout.** HR plugin uses GDPR legal terminology without glossary. Finance uses accounting acronyms (COGS, DSO, NRR, ARR) unexplained. Security is entirely engineer-facing despite claiming compliance officer audience.

5. **No example outputs anywhere.** Non-technical users have no way to preview what a sprint plan, SOW, CV screening report, or security audit looks like before running the command.

### Issue 3: marketplace.json Data Drift

[updated] `statistics.total_skills` (20) and `statistics.total_agents` (25) now match actual file counts. Remaining drift:
- `proagent-delivery` lists `skills: 1`, actually has 2 SKILL.md files (delivery-assistant + rom-estimate)
- `proagent-hr` lists `skills: 2`, actually has 3 SKILL.md files (hr-assistant + cv-validation + interview-evaluation)

### Issue 4: Agent Descriptions Missing `<example>` Blocks

[updated] 6 of 31 agent files (19%) now include `<example>` blocks: agentic-engineering-specialist, delivery-specialist, sow-context-extractor, finance-specialist, platform-specialist, and sdlc-specialist. The remaining 25 agents still lack them, reducing Claude's ability to route tasks correctly.

---

## Plugin-by-Plugin Maturity

### Tier 1 -- Substantive Content, Real Value

These plugins contain tested, specific patterns beyond Claude's default knowledge. **But they still have the broken-refs and user-readiness issues above.**

| Plugin | SKILL Lines | Unique Content | Battle-Tested? | Notes |
|--------|:-----------:|:--------------:|:--------------:|-------|
| **data** | 49 [updated] | ~80% | Yes | dbt medallion architecture, PG tuning values, Airflow DAGs. Content moved to references/ |
| **backend** | 39 [updated] | ~70% | Yes | N+1 benchmarks, JWT lifecycle, Redis patterns, PostgreSQL. Content moved to references/ |
| **devops** | 43 [updated] | ~75% | Yes | Production YAML/HCL, K8s resource calculations. Content moved to references/ |
| **ml-ai** | 37 [updated] | ~75% | Yes | Hyperparameter ranges, training pipelines, RAG architecture. Content moved to references/ |
| **agentic-eng** | 72 [updated] | ~85% | Yes | Multi-agent orchestration, autonomous loops. v1.0.0, workflow factory added |
| **delivery** | 45 + rom-estimate 286 [updated] | ~75% | **Most tested** | SOW references 5 real signed SOWs. ROM uses real team structures. v0.4.0 |

### Tier 2 -- Useful Frameworks, Not Automation

These add methodology and templates but don't execute workflows. ~50-60% of content is knowledge Claude already has.

| Plugin | SKILL Lines | Unique Content | Notes |
|--------|:-----------:|:--------------:|-------|
| **sdlc** | 392 | ~60% | Named process frameworks (ProAgent 5-stage, PITER). Organizational value. Still exceeds 80-line guideline. |
| **security** | 37 [updated] | ~55% | Excellent knowledge base. NOT an automated scanner. CLI tool dependencies. Content moved to references/ |
| **documentation** | 231 | ~65% | Confluence Storage Format is genuinely hard content. Multi-agent pipeline unproven. Still exceeds 80-line guideline. |
| **sales** | 39 [updated] | ~55% | Good templates. Lead scoring model. No research automation. Content moved to references/ |
| **frontend** | 281 | ~50% | Design system guide. Accessibility checklist. Not a component generator. Still exceeds 80-line guideline. |
| **finance** | 406 | ~50% | Revenue forecasting methodology. No calculation engine. Still exceeds 80-line guideline. |

### Tier 3 -- First Drafts / Needs Significant Work

| Plugin | SKILL Lines | Unique Content | Notes |
|--------|:-----------:|:--------------:|-------|
| **qa** | 233 | ~40% | Mostly generic testing advice Claude already knows. Still exceeds 80-line guideline. |
| **platform** | 257 | ~45% | Vague "golden paths" without concrete implementations. Still exceeds 80-line guideline. |
| **hr** | 203 + cv-validation 152 + interview-evaluation 206 [updated] | ~55% | CV orchestration expanded to 7 agents with full candidate lifecycle pipeline (PR #32). v0.4.0. Prescreening, evaluation, and hire/reject stages added. Still exceeds 80-line guideline. |
| **router** | 130 | ~10% | Routing table. Does its job. No domain knowledge. |

---

## Prioritized Fix List

### P0 -- Blocks Production Use

#### 1. Resolve 200+ broken external references
**All plugins except documentation, router, aws-ai, sales.**
Convert external repo paths to one of:
- Inline summaries (describe what the asset does in 1-2 sentences)
- Remove the reference if it's not essential
- Bundle critical referenced assets into a `references/` directory within each plugin

#### 2. Add MCP graceful degradation to all plugins
**All 15 practice plugins.**
Each command and skill must handle the case where MCP servers aren't configured:
- Check for MCP availability before starting workflows
- Provide user-friendly error messages ("Slack integration is not configured. To set it up, see...")
- Offer fallback workflows that work without MCP (manual data input instead of Slack/Drive)

#### 3. Add approval gates for high-stakes operations
- **delivery**: Review gate before overwriting SOW files
- **hr**: Audit trail for CV screening decisions; GDPR compliance disclaimers
- **finance**: Warning before exposing compensation data
- **documentation**: Review gate before Confluence publishing (like delivery's Approve/Edit/Redo pattern)
- **security**: Disclaimer that plugin output is self-assessment, not certified audit

### P1 -- Non-Technical User Readiness

#### 4. Add example outputs to every hub command
Each `/proagent-{practice}-hub` should include a sample output (what a sprint plan, SOW, CV screening report, security audit, etc. looks like) so users know what to expect.

#### 5. Simplify security plugin for non-engineers
Either:
- (a) Create a "compliance mode" that uses GitHub/GitLab native security scanning (no CLI tools) and produces human-readable compliance reports
- (b) Re-label the plugin as "engineers only" and remove compliance officer positioning

#### 6. Add glossaries to domain-specific plugins
- **hr**: Define GDPR, DSAR, PII, blind review, PIP
- **finance**: Define COGS, DSO, NRR, ARR, CAC, LTV, FinOps
- **security**: Define SAST, DAST, OWASP, STRIDE, CVSS
- **delivery**: Define velocity, story points, burndown, RAG status

#### 7. Add `<example>` blocks to remaining agent descriptions
[updated] 6 of 31 agents now have `<example>` blocks (was 2). Still needed in 25 agent files including backend, devops, qa, security, ml-ai, data, frontend, hr (12 agents), documentation (3 agents), connector-setup, and aws-ai specialists.

### P2 -- Content Depth

#### 8. Expand proagent-qa (currently 234 lines -- shortest)
Add: Playwright E2E recipes, pytest fixture patterns, Jest snapshot patterns, CI test parallelization, flaky test handling, real test file templates.

#### 9. Expand proagent-platform (currently 258 lines -- vague)
Add: Actual golden path templates (project scaffolds), service catalog schemas, IDP patterns, concrete CLI tool templates.

#### 10. Test proagent-hr CV pipeline end-to-end
Run 6-agent orchestration with 10-20 synthetic CVs. Document: parser consistency, parallel agent output compatibility, scoring aggregator handling of missing data, token cost per CV.

### P3 -- Data Integrity & Infrastructure

#### 11. Fix marketplace.json component counts
Align `components` counts and `statistics` totals with actual files on disk.

#### 12. Create `.env.example`
Document all 8+ required environment variables with placeholder values and setup instructions.

#### 13. Move audit log from `/tmp/` to user-scoped path
[updated] The `/tmp/proagent-ae-audit.log` reference now only exists in `hooks/legacy/shell-hooks-v0.3.0.json` (archived). Active hooks no longer reference `/tmp/` paths.

#### 14. ~~Add plugin validation script + CI~~ DONE
[updated] Completed in PR #36. `scripts/validate-plugins.sh` + `.github/workflows/validate-plugins.yml` runs on every PR to main. Includes SKILL.md line count audit (warning-only, 80-line threshold) and posts validation summary as a PR comment.

### P4 -- Polish

#### 15. Add `keywords` to all plugin.json files
#### 16. Add MCP fallback docs to all CLAUDE.md files
#### 17. Resolve version alignment
[updated] Version spread has widened: agentic-eng at 1.0.0, delivery/hr at 0.4.0, most at 0.3.0, documentation/router/connector-setup at 0.2.0, aws-ai at 0.2.0.

---

## Overall Verdict

| Category | Count | Maturity | Description |
|----------|:-----:|:--------:|-------------|
| Scaffolding/structure | All 18 | v1.0 | Production-quality architecture, naming, safety |
| Content depth (Tier 1) | 6 | v0.8 | Real patterns, tested workflows. SKILL.md files restructured to router pattern. |
| Content depth (Tier 2) | 6 | v0.5-0.6 | Useful frameworks. Some SKILL.md files still exceed 80-line guideline. |
| Content depth (Tier 3) | 4 | v0.4-0.5 | HR significantly improved (v0.4.0, full lifecycle pipeline). Others still need work. |
| Non-technical user readiness | 0 of 18 | v0.2-0.3 | None are production-ready for non-technical users. |
| External reference integrity | 5 of 18 clean | v0.3 | 200+ broken references across remaining plugins. |
| CI/CD & release pipeline | N/A | v0.9 | [new] Plugin validation on PR, release pipeline with Slack notifications, CODEOWNERS. |

The marketplace is a well-engineered framework with inconsistent content fill. 6 plugins have genuinely substantive domain knowledge. Since the initial assessment, significant progress was made on infrastructure (CI validation, release pipeline, Slack notifications), skill safety (context guards, SKILL.md restructuring, agent deduplication), and the HR plugin (full candidate lifecycle). But the stated goal -- robust, hardened plugins for non-technical Cowork users -- is not yet met. The P0 and P1 items remain the gap between "good engineering prototype" and "production deployment."
