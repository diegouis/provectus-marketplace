---
description: >
  Overview of all HR capabilities: job descriptions, interviews, onboarding,
  performance reviews, compensation analysis, employee development, CV validation,
  and full candidate lifecycle evaluation.
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# proagent-hr Hub

Welcome to the Provectus HR plugin. This hub provides access to all human resources and talent management capabilities.

## Available Commands

### /proagent-hr-run
Execute HR operations. Accepts a mode argument:

- **draft-job-description** - Draft a comprehensive job description for a role. Analyzes role requirements, team context, and market positioning to produce a structured description with responsibilities, qualifications, compensation range, and growth trajectory.
- **plan-interview** - Design a structured interview process for a role. Creates interview stages, generates question banks, builds evaluation scorecards, and coordinates scheduling across panel members.
- **create-onboarding** - Create a 30/60/90-day onboarding plan for a new hire. Generates day-one checklists, milestone schedules, buddy assignments, training plans, and welcome communications.
- **performance-review** - Facilitate a performance review cycle. Generates review templates, collects and synthesizes feedback, drafts constructive narratives, and prepares calibration materials.
- **compensation-analysis** - Analyze compensation for a role or team. Researches market benchmarks, maps internal pay bands, identifies equity gaps, and models total compensation packages.
- **validate-cvs** - Validate candidate CVs against a job description at scale. Uses a multi-agent pipeline: parses CVs from Google Drive, strips PII for blind review, scores skills/experience/integrity in parallel, aggregates into ranked comparison matrices, and generates hiring recommendations after recruiter approval.
- **generate-prescreening** - Generate prescreening questionnaires and internal scoring rubrics for candidates advancing from CV screening. Targets CV gaps with tailored questions and produces recruiter-only rubrics with behavioral anchors.
- **score-prescreening** - Score candidate prescreening responses against internal rubrics. Tracks gap resolution, flags CV inconsistencies, produces comparison matrix with advance/hold/decline recommendations after recruiter approval.
- **evaluate-hr-interview** - Evaluate HR interview outcomes with mandatory bias scanning. Detects protected characteristic references, unanchored culture fit language, and demographic-correlated adjectives before scoring communication, motivation, collaboration, problem solving, and culture alignment.
- **evaluate-technical-interview** - Evaluate technical interview outcomes with bias scanning for pedigree, style, familiarity, and speed bias. Maps JD requirement coverage and flags untested requirements as interview gaps. Scores technical depth, problem solving, code quality, system design, and communication.
- **synthesize-final-recommendation** - Synthesize all stage scorecards into final hire/reject recommendations. Applies configurable stage weights, performs cross-stage consistency analysis and legal defensibility checks. Produces Hire—Strong/Standard/Conditional, Hold, or Reject decisions with onboarding flags or candidate communication guidance.
- **generate-resume** - Generate a tailored, ATS-optimized resume for a specific job description.
- **analyze-growth** - Analyze developer coding patterns and generate a personalized growth report with curated learning resources.

### /proagent-hr-review
Review and assess HR processes. Accepts a mode argument:

- **review job descriptions** - Audit existing job descriptions for completeness, bias-free language, legal compliance, and alignment with current role requirements.
- **interview process** - Evaluate the interview workflow for a role, assessing stage coverage, question quality, scorecard design, and candidate experience.
- **onboarding plans** - Review onboarding plan completeness, milestone coverage, and new hire readiness.
- **team composition** - Analyze team structure, skills distribution, growth trajectories, and succession planning needs.
- **cv-screening** - Audit a completed CV screening batch for scoring consistency, bias detection, coverage completeness, and compliance with blind review protocol.
- **prescreening-quality** - Audit prescreening questionnaires for legal compliance, scoring consistency, and effectiveness at targeting CV gaps.
- **interview-evaluation-audit** - Audit HR and technical interview evaluations for bias scan completeness, inter-rater reliability, coverage gaps, and process compliance.
- **final-recommendation-audit** - Audit final hiring recommendations for legal defensibility, disparate impact patterns, consistent criteria application, and appropriate candidate communication.
- **compliance-audit** - Audit GDPR compliance, employment contracts, and data protection across all HR processes.

## Quick Start

### Hiring Workflow
1. Run `/proagent-hr-run draft-job-description` to create a job description for an open role
2. Run `/proagent-hr-run plan-interview` to design the interview process for that role
3. Run `/proagent-hr-run validate-cvs` to screen candidate CVs against the JD at scale
4. Run `/proagent-hr-review cv-screening` to audit the screening for bias and consistency
5. Run `/proagent-hr-run generate-prescreening` to create prescreening questionnaires for advancing candidates
6. Run `/proagent-hr-run score-prescreening` after candidates respond, to score and compare
7. Run `/proagent-hr-run evaluate-hr-interview` after HR interviews are conducted
8. Run `/proagent-hr-run evaluate-technical-interview` after technical interviews are conducted
9. Run `/proagent-hr-run synthesize-final-recommendation` to produce final hire/reject decisions
10. Run `/proagent-hr-run create-onboarding` after a hire is confirmed

### People Operations Workflow
1. Run `/proagent-hr-run performance-review` to initiate a review cycle
2. Run `/proagent-hr-run compensation-analysis` to benchmark compensation
3. Run `/proagent-hr-review team composition` for a strategic team assessment

## Candidate Evaluation Pipeline

The full candidate lifecycle orchestrates 12 specialized agents across 6 stages:

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
[STAGE 5] evaluate-technical-interview → Coverage Check + Technical Evaluation Scorecards
              │
        ⏸ Coverage Gap Gate + Technical Reviewer Gate
              │
[STAGE 6] synthesize-final-recommendation → Final Hire/Reject Decision
              │
        ⏸ Hiring Manager Gate
              │
        Gmail / Slack / ATS (offers + notifications)
```

Key features: blind review protocol throughout, mandatory bias scans before evaluation, configurable stage weights, legal defensibility checks, crash-safe session state, and mandatory human gates at every stage transition.

## Configuration

This plugin integrates with:
- **Google Drive** for reading CV PDFs, job descriptions, and interview notes
- **Google Sheets** for writing comparison matrices, evaluation summaries, and pipeline tracking
- **Google Docs** for collaborative HR document creation and editing
- **Gmail** for interview scheduling, candidate outreach, offer/decline communications, and internal announcements
- **Slack** for hiring pipeline updates, screening notifications, gate approvals, and team alerts
- **Google Calendar** for interview scheduling, onboarding milestones, and review cycle deadlines
- **Rube/Composio** for BambooHR employee records and ATS integrations (Greenhouse, Lever)

See `.mcp.json` for MCP server configuration and `hooks/hooks.json` for document formatting validation, bias-free screening enforcement, and prescreening legality checks.
