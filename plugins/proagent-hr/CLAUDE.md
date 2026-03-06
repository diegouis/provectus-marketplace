# proagent-hr

This is the Provectus HR plugin for Claude Code. It provides comprehensive human resources and talent management capabilities for the full employee lifecycle, including CV validation at scale with multi-agent orchestration and end-to-end candidate evaluation through prescreening, interview evaluation, and final recommendation synthesis.

## Plugin Structure

```
proagent-hr/
  .claude-plugin/plugin.json   - Plugin metadata and configuration
  skills/
    hr-assistant/SKILL.md      - Core HR skill: hiring, interviews, onboarding, reviews, compensation, development
    cv-validation/SKILL.md     - CV validation skill: parsing, scoring, ranking, blind review, batch processing
    interview-evaluation/SKILL.md - Interview evaluation skill: prescreening, HR eval, technical eval, cross-stage synthesis
  commands/
    proagent-hr-hub.md          - Plugin hub with command overview and quick start
    proagent-hr-run.md          - Execute HR ops: draft-job-description, plan-interview, create-onboarding, performance-review, compensation-analysis, validate-cvs, generate-prescreening, score-prescreening, evaluate-hr-interview, evaluate-technical-interview, synthesize-final-recommendation, generate-resume, analyze-growth
    proagent-hr-review.md       - Review quality: job descriptions, interview process, onboarding plans, team composition, cv-screening, prescreening-quality, interview-evaluation-audit, final-recommendation-audit, compliance-audit
  agents/
    hr-specialist.md            - HR specialist subagent for people operations and talent management
    cv-parser.md                - CV document parser: extracts structured data, separates PII for blind review
    cv-skills-matcher.md        - Skills scorer: matches candidate skills against JD requirements
    cv-experience-validator.md  - Experience validator: timeline, progression, domain relevance
    cv-red-flag-detector.md     - Integrity analyst: detects factual inconsistencies (bias-free)
    cv-scoring-aggregator.md    - Score aggregator: combines parallel results into composite scores and comparison matrices
    cv-recommendation-generator.md - Recommendation generator: produces shortlists and advancement rationale
    prescreening-question-generator.md - Prescreening designer: generates tailored questionnaires and scoring rubrics from CV gaps
    prescreening-response-scorer.md - Prescreening scorer: evaluates candidate responses, tracks gap resolution
    hr-interview-evaluator.md   - HR evaluator: bias scan + behavioral dimension scoring for HR interviews
    technical-interview-evaluator.md - Technical evaluator: bias scan + coverage mapping + technical dimension scoring
    cross-stage-synthesizer.md  - Final synthesizer: weighted cross-stage scoring, legal defensibility, hire/reject decisions
  hooks/hooks.json              - Document formatting validation, inclusive language checks, PII protection, bias-free screening enforcement, prescreening legality, evaluation bias detection
  .mcp.json                      - MCP server configs: Slack, Google Drive, Google Workspace, Google Sheets, GitHub, Rube
```

## External Skill References

The following skills from external repos are integrated into this plugin's workflows:

| Skill | Source Repo | Path | Usage |
|-------|-------------|------|-------|
| GDPR Data Handling | `agents` | `plugins/hr-legal-compliance/skills/gdpr-data-handling/SKILL.md` | Compliance reviews, data subject rights, consent management, breach notification |
| Employment Contract Templates | `agents` | `plugins/hr-legal-compliance/skills/employment-contract-templates/SKILL.md` | Offer letters, employment agreements, employee handbook policies |
| Developer Growth Analysis | `awesome-claude-skills` | `developer-growth-analysis/SKILL.md` | Personalized developer growth reports from chat history, learning resource curation |
| Tailored Resume Generator | `awesome-claude-skills` | `tailored-resume-generator/SKILL.md` | ATS-optimized resume generation tailored to specific job descriptions |

## Commands

- `/proagent-hr-hub` - View all available HR commands and quick start guide
- `/proagent-hr-run draft-job-description` - Draft a role-specific job description with inclusive language and market-aligned compensation
- `/proagent-hr-run plan-interview` - Design a structured interview process with question banks, scorecards, and scheduling
- `/proagent-hr-run create-onboarding` - Create a 30/60/90-day onboarding plan with checklists and milestone scheduling
- `/proagent-hr-run performance-review` - Facilitate a performance review cycle with templates, feedback synthesis, and calibration
- `/proagent-hr-run compensation-analysis` - Analyze compensation against market benchmarks with equity auditing and scenario modeling
- `/proagent-hr-run validate-cvs` - Validate candidate CVs against a job description using multi-agent orchestration with blind review, scoring, and ranked shortlisting
- `/proagent-hr-run generate-prescreening` - Generate prescreening questionnaires targeting CV gaps with internal scoring rubrics for advancing candidates
- `/proagent-hr-run score-prescreening` - Score candidate prescreening responses, track gap resolution, and produce advance/hold/decline recommendations
- `/proagent-hr-run evaluate-hr-interview` - Evaluate HR interviews with mandatory bias scanning before dimension scoring (communication, motivation, collaboration, problem solving, culture alignment)
- `/proagent-hr-run evaluate-technical-interview` - Evaluate technical interviews with bias scanning and JD coverage mapping before dimension scoring (technical depth, problem solving, code quality, system design, communication)
- `/proagent-hr-run synthesize-final-recommendation` - Synthesize all stage scorecards into final hire/reject decisions with configurable weights, cross-stage consistency analysis, and legal defensibility checks
- `/proagent-hr-run generate-resume` - Generate a tailored, ATS-optimized resume for a specific job description using the tailored-resume-generator skill (from `awesome-claude-skills`)
- `/proagent-hr-run analyze-growth` - Analyze a developer's recent coding patterns and generate a personalized growth report with curated learning resources using the developer-growth-analysis skill (from `awesome-claude-skills`)
- `/proagent-hr-review review job descriptions` - Audit job descriptions for completeness, bias, and compliance
- `/proagent-hr-review interview process` - Evaluate interview workflow coverage, candidate experience, and question quality
- `/proagent-hr-review onboarding plans` - Review onboarding plan completeness and effectiveness
- `/proagent-hr-review team composition` - Analyze team structure, skills distribution, and succession planning
- `/proagent-hr-review cv-screening` - Audit a completed CV screening batch for scoring consistency, bias, and coverage
- `/proagent-hr-review prescreening-quality` - Audit prescreening questionnaires for legal compliance, scoring consistency, and gap-targeting effectiveness
- `/proagent-hr-review interview-evaluation-audit` - Audit interview evaluations for bias scan completeness, inter-rater reliability, coverage gaps, and process compliance
- `/proagent-hr-review final-recommendation-audit` - Audit final recommendations for legal defensibility, disparate impact patterns, and consistent criteria application
- `/proagent-hr-review compliance-audit` - Audit HR processes for GDPR compliance, data subject rights handling, and employment contract adherence using the gdpr-data-handling and employment-contract-templates skills (from `agents/hr-legal-compliance`)

## Full Candidate Lifecycle Pipeline

The complete candidate evaluation pipeline spans 6 stages with 12 specialized agents:

```
[STAGE 1] validate-cvs (6 agents) → CV Screening Scorecard
              │
        ⏸ Recruiter Gate
              │
[STAGE 2] generate-prescreening → Questionnaires + Rubrics
              │
        (candidates respond async)
              │
        score-prescreening → Prescreening Scorecards
              │
        ⏸ Recruiter Gate
              │
[STAGE 3] plan-interview → HR + Technical Interview Kits
              │
        (interviews conducted by humans)
              │
[STAGE 4] evaluate-hr-interview → Bias Scan + HR Evaluation Scorecards
              │
        ⏸ Bias Review Gate + HR Reviewer Gate
              │
[STAGE 5] evaluate-technical-interview → Bias Scan + Coverage Check + Technical Evaluation Scorecards
              │
        ⏸ Bias Review Gate + Coverage Gap Gate + Technical Reviewer Gate
              │
[STAGE 6] synthesize-final-recommendation → Final Hire/Reject Decision
              │
        ⏸ Hiring Manager Gate
              │
        Gmail / Slack / ATS (offers + notifications)
```

### Stage Scoring Weights (Default)

| Stage | Weight | Rationale |
|-------|--------|-----------|
| CV Screening | 15% | Document-based, lowest signal fidelity |
| Prescreening | 10% | Written responses, moderate signal |
| HR Interview | 30% | Live behavioral assessment, high signal for soft skills |
| Technical Interview | 45% | Live technical assessment, highest signal for role capability |

Weights are configurable per pipeline run. If a stage is skipped, its weight is redistributed proportionally across remaining stages.

### Blind Review Protocol
- PII is stripped by the parser and stored in a separate identity envelope
- All analysis uses anonymized candidate IDs (Candidate #001, #002, etc.) throughout all stages
- Names are reunited with scores only in the final recommendation output, after hiring manager approval
- No analysis or evaluation agent may reference or infer protected characteristics
- Bias scans run on interviewer notes before evaluation to catch identity leakage

### Session State

The pipeline maintains two session state files for crash-safe resumption:

- **`cv_validation_session.json`**: Tracks CV screening batch progress (parsing, scoring, aggregation, recommendations)
- **`candidate_pipeline_session.json`**: Tracks the full candidate lifecycle from prescreening through final recommendation, including:
  - Per-candidate stage completion status, scores, and file paths
  - Stage weights and any redistribution
  - Recruiter/reviewer gate approvals at each stage
  - Bias flag counts and resolution status
  - Coverage gaps and resolution decisions
  - Pipeline status (in_progress, paused_for_review, completed)

## Document Quality Gates

The hooks configuration enforces:
1. **Job Description Structure**: Validates required sections (role summary, responsibilities, qualifications, compensation, EEO statement)
2. **Inclusive Language**: Scans for biased or exclusionary terms and recommends alternatives
3. **PII Protection**: Blocks commits containing personally identifiable information (SSNs, salary figures, personal addresses)
4. **Onboarding Completeness**: Validates onboarding plans include all phases (day one through 90-day review)
5. **Review Template Validation**: Ensures performance review documents contain balanced feedback sections
6. **Bias-Free Screening**: Warns when CV screening outputs reference protected characteristics (age, gender, ethnicity, race, disability, religion)
7. **Blind Review Enforcement**: Verifies no PII in scoring rationale for CV screening artifacts
8. **GDPR Compliance**: Validates that HR data handling follows GDPR consent management, data subject rights, retention policies, and breach notification procedures (reference: `agents/plugins/hr-legal-compliance/skills/gdpr-data-handling/SKILL.md`)
9. **Employment Contract Compliance**: Ensures offer letters and employment agreements include required legal sections — at-will language, confidentiality, IP assignment, and jurisdiction-specific provisions (reference: `agents/plugins/hr-legal-compliance/skills/employment-contract-templates/SKILL.md`)
10. **Prescreening Legality**: Blocks prescreening questionnaires containing prohibited questions (age, DOB, marital status, children, religion, nationality, citizenship, disability, health, military service, arrest/criminal record, salary history)
11. **Evaluation Bias Detection**: Warns when evaluation files contain bias indicators (accent, appearance, pedigree)
12. **Evaluation Blind Review**: Warns when evaluation or recommendation files may contain candidate names instead of anonymized IDs
13. **Pipeline Session State**: Confirms updates to `candidate_pipeline_session.json`

## MCP Integrations

- **Slack**: Team communication — channels, messages, users, threads via `slack-mcp-server`
- **Google Drive**: File management — Drive files, Docs (Markdown), Sheets (CSV), Slides via `@modelcontextprotocol/server-gdrive`
- **Google Workspace**: Gmail (list, search, send, draft) and Google Calendar (events, scheduling) via `mcp-gsuite`
- **Google Sheets**: Spreadsheet operations — read, write, create sheets for comparison matrices via `@anthropic/mcp-server-google-sheets`
- **GitHub**: Repository management, PRs, issues, Actions via `@modelcontextprotocol/server-github`
- **Excalidraw**: Interactive visual diagramming — renders Excalidraw canvases directly in chat via natural language via `excalidraw/excalidraw-mcp` (remote)
- **Rube (Composio)**: SaaS automation gateway providing access to BambooHR, Google Calendar, Slack, Gmail, and ATS systems (Greenhouse, Lever) via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## Conventions

- All HR documents use professional, inclusive, bias-free language
- Job descriptions include salary transparency and equal opportunity employer statements
- Performance feedback balances recognition with specific, actionable development guidance
- Compensation analysis references market data no older than 6 months
- Onboarding plans are finalized at least 5 business days before the new hire start date
- All personal and compensation data is treated as confidential and protected from version control exposure
- CV screening follows blind review protocol — PII separated from scoring data
- Red flags in CV screening are informational only — never auto-reject candidates
- Scoring weights are declared upfront and applied consistently across all candidates in a batch
- Recruiter confirmation is required before generating final recommendations
- Resume generation follows ATS optimization best practices and uses exact job description keywords
- Developer growth reports are evidence-based, drawn from actual chat history patterns
- Employment contracts and offer letters are reviewed against jurisdiction-specific legal requirements
- GDPR data handling follows consent management, data minimization, and breach notification protocols
- Prescreening questions must comply with employment law — never ask about protected characteristics
- Bias scans must complete BEFORE evaluation scoring — never score first and check for bias after
- Interview coverage gaps are process deficiencies, not candidate deficiencies — never penalize untested areas
- Legal defensibility checklist must pass before any final recommendation is issued
- Final recommendations are processed sequentially per candidate for auditability
- Stage weights are configurable and redistributed proportionally when stages are skipped
