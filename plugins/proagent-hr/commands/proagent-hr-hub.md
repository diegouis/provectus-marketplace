---
description: >
  Overview of all HR capabilities: job descriptions, interviews, onboarding,
  performance reviews, compensation analysis, employee development, and CV validation.
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

### /proagent-hr-review
Review and assess HR processes. Accepts a mode argument:

- **review job descriptions** - Audit existing job descriptions for completeness, bias-free language, legal compliance, and alignment with current role requirements.
- **interview process** - Evaluate the interview workflow for a role, assessing stage coverage, question quality, scorecard design, and candidate experience.
- **onboarding plans** - Review onboarding plan completeness, milestone coverage, and new hire readiness.
- **team composition** - Analyze team structure, skills distribution, growth trajectories, and succession planning needs.
- **cv-screening** - Audit a completed CV screening batch for scoring consistency, bias detection, coverage completeness, and compliance with blind review protocol.

## Quick Start

### Hiring Workflow
1. Run `/proagent-hr-run draft-job-description` to create a job description for an open role
2. Run `/proagent-hr-run plan-interview` to design the interview process for that role
3. Run `/proagent-hr-run validate-cvs` to screen candidate CVs against the JD at scale
4. Run `/proagent-hr-review cv-screening` to audit the screening for bias and consistency
5. Run `/proagent-hr-run create-onboarding` after a hire is confirmed

### People Operations Workflow
1. Run `/proagent-hr-run performance-review` to initiate a review cycle
2. Run `/proagent-hr-run compensation-analysis` to benchmark compensation
3. Run `/proagent-hr-review team composition` for a strategic team assessment

## CV Validation Pipeline

The `validate-cvs` command orchestrates 6 specialized agents:

```
[cv-parser] → Parse CVs, strip PII
      │
      ├─ [cv-skills-matcher]        ─┐
      ├─ [cv-experience-validator]   ├─ Parallel analysis
      └─ [cv-red-flag-detector]     ─┘
              │
      [cv-scoring-aggregator] → Comparison matrix
              │
      ⏸ Recruiter reviews scores
              │
      [cv-recommendation-generator] → Shortlist
```

Key features: blind review protocol, configurable scoring weights, tiered ranking, crash-safe batch processing, and mandatory recruiter confirmation gates.

## Configuration

This plugin integrates with:
- **Google Drive** for reading CV PDFs and job descriptions
- **Google Sheets** for writing comparison matrices and batch reports
- **Google Docs** for collaborative HR document creation and editing
- **Gmail** for interview scheduling, candidate outreach, and internal announcements
- **Slack** for hiring pipeline updates, screening notifications, and team alerts
- **Google Calendar** for interview scheduling, onboarding milestones, and review cycle deadlines
- **Rube/Composio** for BambooHR employee records and ATS integrations

See `.mcp.json` for MCP server configuration and `hooks/hooks.json` for document formatting validation and bias-free screening enforcement.
