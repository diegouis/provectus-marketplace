# proagent-hr

This is the Provectus HR plugin for Claude Code. It provides comprehensive human resources and talent management capabilities for the full employee lifecycle, including CV validation at scale with multi-agent orchestration.

## Plugin Structure

```
proagent-hr/
  .claude-plugin/plugin.json   - Plugin metadata and configuration
  skills/
    hr-assistant/SKILL.md      - Core HR skill: hiring, interviews, onboarding, reviews, compensation, development
    cv-validation/SKILL.md     - CV validation skill: parsing, scoring, ranking, blind review, batch processing
  commands/
    proagent-hr-hub.md          - Plugin hub with command overview and quick start
    proagent-hr-run.md          - Execute HR ops: draft-job-description, plan-interview, create-onboarding, performance-review, compensation-analysis, validate-cvs
    proagent-hr-review.md       - Review quality: job descriptions, interview process, onboarding plans, team composition, cv-screening
  agents/
    hr-specialist.md            - HR specialist subagent for people operations and talent management
    cv-parser.md                - CV document parser: extracts structured data, separates PII for blind review
    cv-skills-matcher.md        - Skills scorer: matches candidate skills against JD requirements
    cv-experience-validator.md  - Experience validator: timeline, progression, domain relevance
    cv-red-flag-detector.md     - Integrity analyst: detects factual inconsistencies (bias-free)
    cv-scoring-aggregator.md    - Score aggregator: combines parallel results into composite scores and comparison matrices
    cv-recommendation-generator.md - Recommendation generator: produces shortlists and advancement rationale
  hooks/hooks.json              - Document formatting validation, inclusive language checks, PII protection, bias-free screening enforcement
  .mcp.json                      - MCP server configs: Slack, Google Drive, Google Workspace, Google Sheets, GitHub, Rube
```

## Commands

- `/proagent-hr-hub` - View all available HR commands and quick start guide
- `/proagent-hr-run draft-job-description` - Draft a role-specific job description with inclusive language and market-aligned compensation
- `/proagent-hr-run plan-interview` - Design a structured interview process with question banks, scorecards, and scheduling
- `/proagent-hr-run create-onboarding` - Create a 30/60/90-day onboarding plan with checklists and milestone scheduling
- `/proagent-hr-run performance-review` - Facilitate a performance review cycle with templates, feedback synthesis, and calibration
- `/proagent-hr-run compensation-analysis` - Analyze compensation against market benchmarks with equity auditing and scenario modeling
- `/proagent-hr-run validate-cvs` - Validate candidate CVs against a job description using multi-agent orchestration with blind review, scoring, and ranked shortlisting
- `/proagent-hr-review review job descriptions` - Audit job descriptions for completeness, bias, and compliance
- `/proagent-hr-review interview process` - Evaluate interview workflow coverage, candidate experience, and question quality
- `/proagent-hr-review onboarding plans` - Review onboarding plan completeness and effectiveness
- `/proagent-hr-review team composition` - Analyze team structure, skills distribution, and succession planning
- `/proagent-hr-review cv-screening` - Audit a completed CV screening batch for scoring consistency, bias, and coverage

## CV Validation Pipeline

The `validate-cvs` mode uses a multi-agent orchestration pipeline:

```
Google Drive (JDs + CV PDFs)
        │
  [1] Extract JD Requirements → STOP for recruiter confirmation
        │
  [2] Parse CVs (cv-parser) → anonymized profiles + PII envelopes
        │
  [3] Parallel Fan-Out:
        ├─ cv-skills-matcher (score skills)
        ├─ cv-experience-validator (validate history)
        └─ cv-red-flag-detector (check integrity)
        │
  [4] Fan-In: cv-scoring-aggregator → comparison matrix + tiers
        │
  [5] STOP for recruiter review
        │
  [6] cv-recommendation-generator → shortlist + next steps
        │
  Google Sheets / Slack / Gmail (results)
```

### Blind Review Protocol
- PII is stripped by the parser and stored in a separate identity envelope
- All analysis uses anonymized candidate IDs (Candidate #001, #002, etc.)
- Names are reunited with scores only in the final recommendation output
- No analysis agent may reference or infer protected characteristics

### Session State
The pipeline maintains `cv_validation_session.json` for crash-safe resume of interrupted batches.

## Document Quality Gates

The hooks configuration enforces:
1. **Job Description Structure**: Validates required sections (role summary, responsibilities, qualifications, compensation, EEO statement)
2. **Inclusive Language**: Scans for biased or exclusionary terms and recommends alternatives
3. **PII Protection**: Blocks commits containing personally identifiable information (SSNs, salary figures, personal addresses)
4. **Onboarding Completeness**: Validates onboarding plans include all phases (day one through 90-day review)
5. **Review Template Validation**: Ensures performance review documents contain balanced feedback sections
6. **Bias-Free Screening**: Warns when CV screening outputs reference protected characteristics (age, gender, ethnicity, race, disability, religion)
7. **Blind Review Enforcement**: Verifies no PII appears in scoring rationale for CV screening artifacts

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
