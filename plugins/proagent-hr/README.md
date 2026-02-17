# proagent-hr

Provectus HR plugin for Claude Code. Comprehensive human resources and talent management for the full employee lifecycle.

## Overview

proagent-hr provides a complete HR toolkit that integrates with Claude Code to automate job description drafting, interview planning, onboarding coordination, performance reviews, compensation analysis, and employee development tracking. It enforces document quality through formatting validation, inclusive language checks, and PII protection hooks.

## Installation

1. Copy the `proagent-hr/` directory into your project's `.claude/plugins/` directory
2. Configure MCP servers in `.mcp.json` with your credentials:
   - Set `SLACK_BOT_TOKEN` and `SLACK_TEAM_ID` for Slack integration
   - Set `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REFRESH_TOKEN` for Google Drive integration
   - Set `GITHUB_PERSONAL_ACCESS_TOKEN` for GitHub integration
3. Ensure your Google OAuth credentials have scopes for Drive access

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-hr-hub` | View all available commands and quick start guide |
| `/proagent-hr-run draft-job-description` | Draft a job description with inclusive language and compensation range |
| `/proagent-hr-run plan-interview` | Design structured interview process with scorecards |
| `/proagent-hr-run create-onboarding` | Create 30/60/90-day onboarding plan |
| `/proagent-hr-run performance-review` | Facilitate review cycle with feedback synthesis |
| `/proagent-hr-run compensation-analysis` | Analyze compensation against market benchmarks |
| `/proagent-hr-review review job descriptions` | Audit job descriptions for quality and compliance |
| `/proagent-hr-review interview process` | Evaluate interview workflow and candidate experience |
| `/proagent-hr-review onboarding plans` | Review onboarding completeness and effectiveness |
| `/proagent-hr-review team composition` | Analyze team structure and succession planning |

## Document Quality Gates

The plugin includes automated document validation via `hooks/hooks.json`:

- **Job Description Structure**: Warns when required sections are missing (role summary, responsibilities, qualifications, compensation, EEO statement)
- **Inclusive Language**: Flags biased terms (rockstar, ninja, gendered language) and recommends alternatives
- **PII Protection**: Blocks commits containing social security numbers, raw salary figures, or personal addresses
- **Onboarding Completeness**: Validates all onboarding phases are covered (day one through 90-day review)
- **Review Template Validation**: Ensures performance reviews include strengths, development areas, and development plans

## Integrations

### Configured MCP Servers
- **Slack** (`@modelcontextprotocol/server-slack`): Post hiring pipeline updates, new hire introductions, and team announcements
- **Google Drive** (`@modelcontextprotocol/server-google-drive`): Create and collaborate on job descriptions, offer letters, review templates, and policy documents
- **GitHub** (`@modelcontextprotocol/server-github`): Repository access for HR documentation and policy version control

## Architecture

The plugin is built around these components:

- **SKILL.md**: Defines the HR assistant's core competencies across job descriptions, interviews, onboarding, performance reviews, compensation analysis, employee development, internal communications, and meeting behavioral analysis
- **Commands**: Three command files (Hub, Run, Review) that provide the user-facing interface for all HR operations
- **Agent**: An HR specialist subagent with people operations expertise for autonomous HR document creation and process management
- **Hooks**: Document quality gates that enforce formatting standards, inclusive language, and PII protection
- **MCP Config**: Integration with Slack, Google Drive, and GitHub for HR workflow automation

## Source Attribution

This plugin synthesizes patterns and practices from the following Provectus repositories:

- **proagent**: Human resources role definition, onboarding coordination skills, interview process management, performance review facilitation
- **awesome-claude-skills**: Developer growth analysis for personalized growth reports, meeting insights analyzer for behavioral pattern detection, tailored resume generator for job description alignment
- **skills**: Internal communications skill for newsletters, FAQs, and company-wide updates
- **agents**: HR professional agent for policy documentation and compliance workflows
- **specs**: Business role implementations covering project-manager, human-resources, and technical-writer within the Provectus Unified Agent Framework (PUAF)

## License

MIT
