# proagent-hr

Provectus HR plugin for Claude Code. Comprehensive human resources and talent management for the full employee lifecycle, including CV validation at scale with multi-agent orchestration and end-to-end candidate evaluation through prescreening, interview evaluation, and final recommendation synthesis.

## Overview

proagent-hr provides a complete HR toolkit that integrates with Claude Code to automate job description drafting, interview planning, onboarding coordination, performance reviews, compensation analysis, employee development tracking, **CV validation against job profiles at scale**, **prescreening questionnaire design and scoring**, **HR and technical interview evaluation with bias detection**, **cross-stage synthesis for hire/reject decisions**, **GDPR compliance auditing**, **employment contract generation**, **tailored resume generation**, and **developer growth analysis**. It enforces document quality through formatting validation, inclusive language checks, PII protection, bias-free screening hooks, prescreening legality checks, evaluation bias detection, GDPR data handling compliance, and employment contract validation. Integrates assets from 3 source repos: `provectus-marketplace`, `agents`, and `awesome-claude-skills`.

## Installation

1. Copy the `proagent-hr/` directory into your project's `.claude/plugins/` directory
2. Configure MCP servers in `.mcp.json` with your credentials:
   - Set `SLACK_BOT_TOKEN` and `SLACK_TEAM_ID` for Slack integration
   - Set `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REFRESH_TOKEN` for Google Drive and Sheets integration
   - Set `GITHUB_PERSONAL_ACCESS_TOKEN` for GitHub integration
3. Ensure your Google OAuth credentials have scopes for Drive and Sheets access

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-hr-hub` | View all available commands and quick start guide |
| `/proagent-hr-run draft-job-description` | Draft a job description with inclusive language and compensation range |
| `/proagent-hr-run plan-interview` | Design structured interview process with scorecards |
| `/proagent-hr-run create-onboarding` | Create 30/60/90-day onboarding plan |
| `/proagent-hr-run performance-review` | Facilitate review cycle with feedback synthesis |
| `/proagent-hr-run compensation-analysis` | Analyze compensation against market benchmarks |
| `/proagent-hr-run validate-cvs` | Validate CVs against a JD with multi-agent scoring and blind review |
| `/proagent-hr-run generate-prescreening` | Generate prescreening questionnaires targeting CV gaps with scoring rubrics |
| `/proagent-hr-run score-prescreening` | Score prescreening responses, track gap resolution, advance/hold/decline |
| `/proagent-hr-run evaluate-hr-interview` | Evaluate HR interviews with bias scanning and behavioral dimension scoring |
| `/proagent-hr-run evaluate-technical-interview` | Evaluate technical interviews with bias scanning and JD coverage mapping |
| `/proagent-hr-run synthesize-final-recommendation` | Synthesize all stages into final hire/reject decisions with legal defensibility |
| `/proagent-hr-run generate-resume` | Generate a tailored, ATS-optimized resume for a specific job description |
| `/proagent-hr-run analyze-growth` | Analyze developer coding patterns and generate a personalized growth report |
| `/proagent-hr-review review job descriptions` | Audit job descriptions for quality and compliance |
| `/proagent-hr-review interview process` | Evaluate interview workflow and candidate experience |
| `/proagent-hr-review onboarding plans` | Review onboarding completeness and effectiveness |
| `/proagent-hr-review team composition` | Analyze team structure and succession planning |
| `/proagent-hr-review cv-screening` | Audit CV screening batch for consistency and bias |
| `/proagent-hr-review prescreening-quality` | Audit prescreening for legality, scoring consistency, and effectiveness |
| `/proagent-hr-review interview-evaluation-audit` | Audit evaluations for bias scans, inter-rater reliability, and coverage |
| `/proagent-hr-review final-recommendation-audit` | Audit recommendations for legal defensibility and disparate impact |
| `/proagent-hr-review compliance-audit` | Audit GDPR compliance, employment contracts, and data protection |

## Candidate Evaluation Pipeline

The full candidate lifecycle runs a multi-agent orchestration pipeline across 6 stages:

```
[STAGE 1] validate-cvs (6 agents)
              │
        ⏸ Recruiter Gate
              │
[STAGE 2] generate-prescreening → score-prescreening
              │
        ⏸ Recruiter Gate
              │
[STAGE 3] plan-interview (HR + Technical kits)
              │
        (interviews conducted by humans)
              │
[STAGE 4] evaluate-hr-interview → Bias Scan + HR Evaluation
              │
        ⏸ Bias Review Gate + HR Reviewer Gate
              │
[STAGE 5] evaluate-technical-interview → Coverage Check + Technical Evaluation
              │
        ⏸ Coverage Gap Gate + Technical Reviewer Gate
              │
[STAGE 6] synthesize-final-recommendation → Hire/Reject Decision
              │
        ⏸ Hiring Manager Gate
              │
        Gmail / Slack / ATS (offers + notifications)
```

### Scoring Weights

| Stage | Default Weight | Signal Type |
|-------|---------------|-------------|
| CV Screening | 15% | Document-based |
| Prescreening | 10% | Written responses |
| HR Interview | 30% | Live behavioral assessment |
| Technical Interview | 45% | Live technical assessment |

Weights are configurable per run. If a stage is skipped, its weight is redistributed proportionally.

### Key Features
- **Blind Review**: PII stripped before scoring, candidates identified by number only through all stages
- **Mandatory Bias Scanning**: Interviewer notes scanned for bias BEFORE evaluation scoring begins
- **Coverage Mapping**: Untested JD requirements flagged as interview gaps, not candidate deficiencies
- **Legal Defensibility**: Checklist must pass before any final recommendation is issued
- **Configurable Weights**: Stage weights adjustable per pipeline, auto-redistribute when stages skipped
- **Tiered Ranking**: Candidates sorted into Tier 1 (Strong), 2 (Good), 3 (Partial), 4 (No Match)
- **Final Decisions**: Hire—Strong, Hire—Standard, Hire—Conditional, Hold, Reject
- **Crash Recovery**: Session state persisted at each stage for resumable processing
- **Human Gates**: Mandatory recruiter/reviewer confirmation at every stage transition

### Agents

| Agent | Model | Role |
|-------|-------|------|
| `cv-parser` | Sonnet | Extract structured data from CV PDFs, separate PII |
| `cv-skills-matcher` | Sonnet | Score skill match against JD requirements |
| `cv-experience-validator` | Sonnet | Validate work history timeline and relevance |
| `cv-red-flag-detector` | Opus | Detect factual inconsistencies (bias-free) |
| `cv-scoring-aggregator` | Sonnet | Combine scores into composite rankings |
| `cv-recommendation-generator` | Opus | Produce shortlists and advancement rationale |
| `prescreening-question-generator` | Sonnet | Generate tailored questionnaires and scoring rubrics |
| `prescreening-response-scorer` | Sonnet | Score responses, track gap resolution |
| `hr-interview-evaluator` | Opus | Bias scan + HR behavioral dimension scoring |
| `technical-interview-evaluator` | Opus | Bias scan + coverage mapping + technical scoring |
| `cross-stage-synthesizer` | Opus | Weighted cross-stage synthesis, legal defensibility, final decisions |

## Document Quality Gates

The plugin includes automated document validation via `hooks/hooks.json`:

- **Job Description Structure**: Warns when required sections are missing (role summary, responsibilities, qualifications, compensation, EEO statement)
- **Inclusive Language**: Flags biased terms (rockstar, ninja, gendered language) and recommends alternatives
- **PII Protection**: Blocks commits containing social security numbers, raw salary figures, or personal addresses
- **Onboarding Completeness**: Validates all onboarding phases are covered (day one through 90-day review)
- **Review Template Validation**: Ensures performance reviews include strengths, development areas, and development plans
- **Bias-Free Screening**: Warns when CV screening outputs reference protected characteristics
- **Blind Review Enforcement**: Verifies no PII in scoring rationale for CV screening artifacts
- **GDPR Compliance**: Validates HR data handling follows consent management, data subject rights, retention policies, and breach notification (from `agents/plugins/hr-legal-compliance/skills/gdpr-data-handling/SKILL.md`)
- **Employment Contract Compliance**: Ensures offer letters and employment agreements include required legal sections (from `agents/plugins/hr-legal-compliance/skills/employment-contract-templates/SKILL.md`)
- **Prescreening Legality**: Blocks prescreening questionnaires containing prohibited questions (age, DOB, marital status, children, religion, nationality, citizenship, disability, health)
- **Evaluation Bias Detection**: Warns when evaluation files contain bias indicators (accent, appearance, pedigree)
- **Evaluation Blind Review**: Warns when evaluation or recommendation files may contain candidate names
- **Pipeline Session State**: Confirms updates to `candidate_pipeline_session.json`

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides, CV PDFs |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| Google Sheets | `@anthropic/mcp-server-google-sheets` | Comparison matrices, batch reports |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming — renders canvases directly in chat via natural language |
| Rube | `rube.app/mcp` | SaaS automation gateway (BambooHR, ATS systems, etc.) |

## Architecture

The plugin is built around these components:

- **Skills**: Three skill files — `hr-assistant` for core HR operations (including GDPR compliance, employment contracts, resume generation, and developer growth analysis), `cv-validation` for resume screening at scale, and `interview-evaluation` for prescreening through final recommendation synthesis
- **Commands**: Three command files (Hub, Run, Review) providing the user-facing interface for all HR operations including the full candidate lifecycle
- **Agents**: Twelve agents — one generalist HR specialist, six CV validation agents, and five interview evaluation agents forming an end-to-end orchestration pipeline
- **Hooks**: Document quality gates enforcing formatting, inclusive language, PII protection, bias-free screening, prescreening legality, evaluation bias detection, GDPR compliance, and employment contract validation
- **MCP Config**: Integration with Slack, Google Drive, Google Sheets, Google Workspace, GitHub, Excalidraw, and Rube for end-to-end workflow automation
- **External Skills (4)**: Integrated from `agents` repo (GDPR data handling, employment contract templates) and `awesome-claude-skills` repo (developer growth analysis, tailored resume generator)

## Source Repos

| Repo | Assets | Key Contributions |
|------|--------|-------------------|
| `provectus-marketplace` | 18 | Core plugin, CV validation pipeline, interview evaluation pipeline, all agents |
| `agents` | 4 | GDPR data handling, employment contract templates, legal advisor, HR pro agents |
| `awesome-claude-skills` | 3 | Developer growth analysis, tailored resume generator |

## License

MIT
