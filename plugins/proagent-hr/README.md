# proagent-hr

Provectus HR plugin for Claude Code. Comprehensive human resources and talent management for the full employee lifecycle, including CV validation at scale with multi-agent orchestration.

## Overview

proagent-hr provides a complete HR toolkit that integrates with Claude Code to automate job description drafting, interview planning, onboarding coordination, performance reviews, compensation analysis, employee development tracking, and **CV validation against job profiles at scale**. It enforces document quality through formatting validation, inclusive language checks, PII protection, and bias-free screening hooks.

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
| `/proagent-hr-review review job descriptions` | Audit job descriptions for quality and compliance |
| `/proagent-hr-review interview process` | Evaluate interview workflow and candidate experience |
| `/proagent-hr-review onboarding plans` | Review onboarding completeness and effectiveness |
| `/proagent-hr-review team composition` | Analyze team structure and succession planning |
| `/proagent-hr-review cv-screening` | Audit CV screening batch for consistency and bias |

## CV Validation Pipeline

The `validate-cvs` command runs a multi-agent orchestration pipeline:

```
Google Drive (JDs + CV PDFs)
        │
  [1] Extract JD requirements → STOP for recruiter confirmation
        │
  [2] Parse CVs → anonymized profiles (blind review)
        │
  [3] Parallel analysis:
        ├─ Skills matching
        ├─ Experience validation
        └─ Red flag detection
        │
  [4] Aggregate scores → comparison matrix + tier ranking
        │
  [5] STOP for recruiter review
        │
  [6] Generate recommendations → shortlist + next steps
```

### Key Features
- **Blind Review**: PII stripped before scoring, candidates identified by number only
- **Configurable Weights**: Default 35/35/15/15 (Skills/Experience/Education/Certifications), adjustable per run
- **Tiered Ranking**: Candidates sorted into Tier 1 (Strong), 2 (Good), 3 (Partial), 4 (No Match)
- **Bias-Free Screening**: Hooks warn on protected characteristic references, employment gaps never penalized
- **Crash Recovery**: Session state persisted after each candidate for resumable batch processing
- **Recruiter Gates**: Human confirmation required before final recommendations

### Agents

| Agent | Model | Role |
|-------|-------|------|
| `cv-parser` | Sonnet | Extract structured data from CV PDFs, separate PII |
| `cv-skills-matcher` | Sonnet | Score skill match against JD requirements |
| `cv-experience-validator` | Sonnet | Validate work history timeline and relevance |
| `cv-red-flag-detector` | Opus | Detect factual inconsistencies (bias-free) |
| `cv-scoring-aggregator` | Sonnet | Combine scores into composite rankings |
| `cv-recommendation-generator` | Opus | Produce shortlists and advancement rationale |

## Document Quality Gates

The plugin includes automated document validation via `hooks/hooks.json`:

- **Job Description Structure**: Warns when required sections are missing (role summary, responsibilities, qualifications, compensation, EEO statement)
- **Inclusive Language**: Flags biased terms (rockstar, ninja, gendered language) and recommends alternatives
- **PII Protection**: Blocks commits containing social security numbers, raw salary figures, or personal addresses
- **Onboarding Completeness**: Validates all onboarding phases are covered (day one through 90-day review)
- **Review Template Validation**: Ensures performance reviews include strengths, development areas, and development plans
- **Bias-Free Screening**: Warns when CV screening outputs reference protected characteristics
- **Blind Review Enforcement**: Verifies no PII in scoring rationale for CV screening artifacts

### MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides, CV PDFs |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| Google Sheets | `@anthropic/mcp-server-google-sheets` | Comparison matrices, batch reports |
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Rube | `rube.app/mcp` | SaaS automation gateway (BambooHR, ATS systems, etc.) |

## Architecture

The plugin is built around these components:

- **Skills**: Two skill files — `hr-assistant` for core HR operations and `cv-validation` for resume screening at scale
- **Commands**: Three command files (Hub, Run, Review) providing the user-facing interface for all HR operations including CV validation
- **Agents**: Seven agents — one generalist HR specialist and six specialized CV validation agents forming an orchestration pipeline
- **Hooks**: Document quality gates enforcing formatting, inclusive language, PII protection, and bias-free screening
- **MCP Config**: Integration with Slack, Google Drive, Google Sheets, Google Workspace, GitHub, and Rube for end-to-end workflow automation

## Source Attribution

This plugin synthesizes patterns and practices from the following Provectus repositories:

- **proagent**: Human resources role definition, onboarding coordination skills, interview process management, performance review facilitation
- **awesome-claude-skills**: Developer growth analysis for personalized growth reports, meeting insights analyzer for behavioral pattern detection, tailored resume generator for job description alignment
- **skills**: Internal communications skill for newsletters, FAQs, and company-wide updates
- **agents**: HR professional agent for policy documentation and compliance workflows
- **specs**: Business role implementations covering project-manager, human-resources, and technical-writer within the Provectus Unified Agent Framework (PUAF)

## License

MIT
