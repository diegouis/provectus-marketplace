# Provectus Marketplace: Plugin Quality & Maturity Assessment

**Date**: 2026-02-20
**Repository**: `provectus-marketplace`
**Scope**: 16 Claude Code plugins (15 practice-specific + 1 router) intended for non-technical Cowork users
**Source**: 867 cataloged assets across 16 Provectus repositories

---

## Summary

The marketplace has **excellent scaffolding** -- consistent architecture, naming, security, documentation templates across all 16 plugins. But the content ranges from battle-tested to first-draft, and no plugins are production-ready for the stated audience (non-technical Cowork users) without hardening.

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

Component counts in `marketplace.json` don't match actual files:
- `proagent-delivery` lists `skills: 1`, actually has 3 SKILL.md files
- `statistics.total_skills` says 18, actual count is 20
- `statistics.total_agents` says 23, actual count is 25

### Issue 4: Agent Descriptions Missing `<example>` Blocks

Only 2 of 15 specialist agents (agentic-engineering, delivery) include `<example>` blocks in their YAML descriptions. The other 13 lack them, reducing Claude's ability to route tasks correctly.

---

## Plugin-by-Plugin Maturity

### Tier 1 -- Substantive Content, Real Value

These plugins contain tested, specific patterns beyond Claude's default knowledge. **But they still have the broken-refs and user-readiness issues above.**

| Plugin | SKILL Lines | Unique Content | Battle-Tested? | Notes |
|--------|:-----------:|:--------------:|:--------------:|-------|
| **data** | 1195 | ~80% | Yes | dbt medallion architecture, PG tuning values, Airflow DAGs |
| **backend** | 1230 | ~70% | Yes | N+1 benchmarks, JWT lifecycle, Redis patterns, PostgreSQL |
| **devops** | 895 | ~75% | Yes | Production YAML/HCL, K8s resource calculations |
| **ml-ai** | 792 | ~75% | Yes | Hyperparameter ranges, training pipelines, RAG architecture |
| **agentic-eng** | 749 | ~85% | Yes | Multi-agent orchestration, autonomous loops (niche audience) |
| **delivery** | 559 + 2 extra | ~75% | **Most tested** | SOW references 5 real signed SOWs. ROM uses real team structures |

### Tier 2 -- Useful Frameworks, Not Automation

These add methodology and templates but don't execute workflows. ~50-60% of content is knowledge Claude already has.

| Plugin | SKILL Lines | Unique Content | Notes |
|--------|:-----------:|:--------------:|-------|
| **sdlc** | 393 | ~60% | Named process frameworks (ProAgent 5-stage, PITER). Organizational value. |
| **security** | 610 | ~55% | Excellent knowledge base. NOT an automated scanner. CLI tool dependencies. |
| **documentation** | 308 | ~65% | Confluence Storage Format is genuinely hard content. Multi-agent pipeline unproven. |
| **sales** | 614 | ~55% | Good templates. Lead scoring model. No research automation. |
| **frontend** | 282 | ~50% | Design system guide. Accessibility checklist. Not a component generator. |
| **finance** | Moderate | ~50% | Revenue forecasting methodology. No calculation engine. |

### Tier 3 -- First Drafts / Needs Significant Work

| Plugin | SKILL Lines | Unique Content | Notes |
|--------|:-----------:|:--------------:|-------|
| **qa** | 234 | ~40% | **Shortest skill.** Mostly generic testing advice Claude already knows. |
| **platform** | 258 | ~45% | Vague "golden paths" without concrete implementations. |
| **hr** | Moderate | ~50% | CV orchestration (6 agents) is well-designed but untested. Individual pieces work; pipeline is unproven. |
| **router** | 128 | ~10% | Routing table. Does its job. No domain knowledge. |

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

#### 7. Add `<example>` blocks to 13 specialist agent descriptions
All `agents/*-specialist.md` files except agentic-engineering and delivery need 2-3 `<example>` blocks with `<commentary>` for proper Claude routing.

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
`plugins/proagent-agentic-engineering/hooks/hooks.json` -- change `/tmp/proagent-ae-audit.log` to `$HOME/.claude/logs/`.

#### 14. Add plugin validation script + CI
`scripts/validate-plugins.py` + `.github/workflows/validate.yml` to catch: missing files, YAML errors, count drift, hook JSON errors, broken references.

### P4 -- Polish

#### 15. Add `keywords` to all plugin.json files
#### 16. Add MCP fallback docs to all CLAUDE.md files
#### 17. Resolve version alignment (documentation/router at 0.2.0 vs others at 0.3.0)

---

## Overall Verdict

| Category | Count | Maturity | Description |
|----------|:-----:|:--------:|-------------|
| Scaffolding/structure | All 16 | v1.0 | Production-quality architecture, naming, safety |
| Content depth (Tier 1) | 6 | v0.8 | Real patterns, tested workflows. Not first drafts. |
| Content depth (Tier 2) | 6 | v0.5-0.6 | Useful frameworks. Second drafts. |
| Content depth (Tier 3) | 4 | v0.3-0.4 | First drafts. Need significant expansion. |
| Non-technical user readiness | 0 of 16 | v0.2-0.3 | None are production-ready for non-technical users. |
| External reference integrity | 3 of 16 clean | v0.3 | 200+ broken references across 13 plugins. |

The marketplace is a well-engineered framework with inconsistent content fill. 6 plugins have genuinely substantive domain knowledge. But the stated goal -- robust, hardened plugins for non-technical Cowork users -- is not yet met. The P0 and P1 items are the gap between "good engineering prototype" and "production deployment."
