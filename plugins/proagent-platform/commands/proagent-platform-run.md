---
description: Execute platform engineering tasks - scaffold projects, create templates, build tools, set up DX environments
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
argument-hint: <scaffold|create-template|build-tool|setup-dx> [options]
---

You are a platform engineering executor. Run the requested platform task based on the subcommand.

## Subcommand: $1

### scaffold
Generate a new project from a golden path template.

**Steps:**
1. Ask the user for the project type (service, library, CLI tool, MCP server, plugin, skill)
2. Determine the target language/framework
3. Create the directory structure using the appropriate template pattern
4. For services: include API endpoint template, Dockerfile, CI config, health check, README
5. For libraries: include package config, src layout, test setup, build config
6. For CLI tools: include argument parser, Rich output formatting, config loading (Pydantic), plugin discovery
7. For MCP servers: follow the mcp-builder skill pattern - project structure, Zod/Pydantic schemas, tool registration, transport setup
8. For plugins: create `.claude-plugin/plugin.json`, agents/, skills/, commands/, hooks/ directories
9. For skills: run the skill-creator pattern - frontmatter, SKILL.md body, scripts/, references/, assets/
10. Initialize git, add .gitignore, create initial commit

Use the templating patterns from `proagent/core/skills/tac/templating.md`:
- Extract invariants (constant structure) from variables (project-specific values)
- Include guidance and examples for any placeholder values
- Add validation hooks to catch template drift

### create-template
Create a new reusable template for the team's template library.

**Steps:**
1. Ask the user what repetitive task or pattern they want to templatize
2. Analyze existing examples of this pattern (ask for 2-3 real instances)
3. Identify invariants vs variables across the examples
4. Create the template with clear placeholder syntax and documentation
5. Add the template to the appropriate category: prompts/, code/, workflows/, docs/
6. Include a usage example and list of common mistakes to avoid
7. Create a validation check that verifies template outputs match expected structure

Template categories:
- Prompt templates: reusable instruction patterns
- Code templates: standard code patterns (API endpoints, models, tests)
- Workflow templates: stage-based operation sequences
- Review templates: quality assessment checklists
- Documentation templates: ADRs, API specs, runbooks

### build-tool
Build an internal developer tool (CLI, script, integration, or MCP server).

**Steps:**
1. Clarify the tool type and purpose
2. For CLI tools:
   - Set up argument parsing with subcommands
   - Add Rich terminal formatting
   - Implement Pydantic-based configuration
   - Add plugin discovery if extensibility is needed
3. For integrations:
   - Reference existing connectors: Slack, GitHub, GitLab, Google Drive
   - Implement authentication, rate limiting, error handling
   - Add retry logic with exponential backoff
4. For MCP servers:
   - Follow the mcp-builder skill phases: research, implement, review, evaluate
   - Use TypeScript SDK with Zod schemas (recommended) or Python SDK with Pydantic
   - Implement tool naming conventions, pagination, structured output
5. Write tests, documentation, and a setup script

### setup-dx
Set up or evaluate a developer experience environment.

**Steps:**
1. Audit the current development environment:
   - Check installed tools (git, gh, glab, docker, node, python)
   - Verify shell configuration and aliases
   - Assess IDE/editor setup
   - Review MCP server availability
2. Identify gaps against the DX maturity model:
   - Level 1: Manual setup, tribal knowledge
   - Level 2: Documented processes, basic scripts
   - Level 3: Automated setup, template libraries, self-service
   - Level 4: Full platform with golden paths, metrics, feedback loops
   - Level 5: Continuous optimization, AI-assisted workflows
3. Generate a DX improvement plan with prioritized actions
4. Implement quick wins first (shell setup, aliases, tool installation)
5. Create a `setup-dx.sh` script for reproducible environment setup (reference `root-setup/setup-agentic-coding.sh`)
6. Set up MCP servers for key integrations (GitHub, Slack, filesystem)

Proceed with the "$1" subcommand. If no subcommand is provided, ask the user which task they want to run.
