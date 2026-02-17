# proagent-hr

This is the Provectus HR plugin for Claude Code. It provides comprehensive human resources and talent management capabilities for the full employee lifecycle.

## Plugin Structure

```
proagent-hr/
  .claude-plugin/plugin.json   - Plugin metadata and configuration
  skills/hr-assistant/SKILL.md - Core HR skill: hiring, interviews, onboarding, reviews, compensation, development
  commands/
    proagent-hr-hub.md          - Plugin hub with command overview and quick start
    proagent-hr-run.md          - Execute HR ops: draft-job-description, plan-interview, create-onboarding, performance-review, compensation-analysis
    proagent-hr-review.md       - Review quality: job descriptions, interview process, onboarding plans, team composition
  agents/hr-specialist.md       - HR specialist subagent for people operations and talent management
  hooks/hooks.json              - Document formatting validation, inclusive language checks, PII protection
  .mcp.json                      - MCP server configs: Slack, Google Drive, GitHub
```

## Commands

- `/proagent-hr-hub` - View all available HR commands and quick start guide
- `/proagent-hr-run draft-job-description` - Draft a role-specific job description with inclusive language and market-aligned compensation
- `/proagent-hr-run plan-interview` - Design a structured interview process with question banks, scorecards, and scheduling
- `/proagent-hr-run create-onboarding` - Create a 30/60/90-day onboarding plan with checklists and milestone scheduling
- `/proagent-hr-run performance-review` - Facilitate a performance review cycle with templates, feedback synthesis, and calibration
- `/proagent-hr-run compensation-analysis` - Analyze compensation against market benchmarks with equity auditing and scenario modeling
- `/proagent-hr-review review job descriptions` - Audit job descriptions for completeness, bias, and compliance
- `/proagent-hr-review interview process` - Evaluate interview workflow coverage, candidate experience, and question quality
- `/proagent-hr-review onboarding plans` - Review onboarding plan completeness and effectiveness
- `/proagent-hr-review team composition` - Analyze team structure, skills distribution, and succession planning

## Document Quality Gates

The hooks configuration enforces:
1. **Job Description Structure**: Validates required sections (role summary, responsibilities, qualifications, compensation, EEO statement)
2. **Inclusive Language**: Scans for biased or exclusionary terms and recommends alternatives
3. **PII Protection**: Blocks commits containing personally identifiable information (SSNs, salary figures, personal addresses)
4. **Onboarding Completeness**: Validates onboarding plans include all phases (day one through 90-day review)
5. **Review Template Validation**: Ensures performance review documents contain balanced feedback sections

## MCP Integrations

- **Slack**: Post hiring pipeline updates, new hire introductions, and team notifications
- **Google Drive**: Create and collaborate on job descriptions, offer letters, performance reviews, and policy documents
- **GitHub**: Repository access for HR documentation and policy version control
- **Rube (Composio)**: SaaS automation gateway providing access to BambooHR, Google Calendar, Slack, and Gmail via `RUBE_SEARCH_TOOLS`, `RUBE_MANAGE_CONNECTIONS`, and `RUBE_MULTI_EXECUTE_TOOL`

## Conventions

- All HR documents use professional, inclusive, bias-free language
- Job descriptions include salary transparency and equal opportunity employer statements
- Performance feedback balances recognition with specific, actionable development guidance
- Compensation analysis references market data no older than 6 months
- Onboarding plans are finalized at least 5 business days before the new hire start date
- All personal and compensation data is treated as confidential and protected from version control exposure
