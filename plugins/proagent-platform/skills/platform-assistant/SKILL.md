---
name: platform-assistant
description: >
  Building Developer Platforms & Tooling. Comprehensive guidance for platform engineering:
  developer experience (DX) optimization, service catalogs, golden paths, project scaffolding,
  internal tooling, MCP server development, plugin system architecture, template libraries,
  and CLI tool creation.

  Use when the user needs to:
  (1) Design or build an internal developer platform (IDP),
  (2) Create service catalogs or golden path templates,
  (3) Scaffold new projects, services, or microservices from templates,
  (4) Build internal CLI tools, MCP servers, or plugin systems,
  (5) Evaluate or improve developer experience (DX) across toolchains,
  (6) Create reusable template libraries for teams,
  (7) Design platform-as-product strategies,
  (8) Build skill or agent plugins for Claude Code,
  (9) Set up developer portals or self-service infrastructure.

  Activate when user mentions: platform engineering, developer experience, DX, service catalog,
  golden path, scaffolding, internal tooling, MCP server, plugin system, template library,
  developer portal, self-service, platform team, internal developer platform, IDP, Backstage,
  developer productivity, paved roads, starter kits, project templates, CLI tools, SDK design.
---

# Building Developer Platforms & Tooling

Platform engineering creates self-service capabilities that reduce cognitive load and accelerate delivery. This skill covers the full spectrum: from designing golden paths and service catalogs to building MCP servers and plugin systems.

## Core Capabilities

### 1. Service Catalog & Golden Paths

Design and implement service catalogs that encode organizational best practices into discoverable, self-service templates.

**Key patterns from Provectus assets:**
- Template libraries structured by domain (see `proagent/core/templates/skill-template.md`, `proagent/core/templates/command-template.md`)
- Reusable skill and command patterns (see `skills/skill-creator/SKILL.md` for the meta-skill pattern)
- Progressive disclosure: metadata for discovery, instructions for understanding, details for implementation

**Golden path design principles:**
- Encode best practices as defaults, not documentation
- Make the right thing the easy thing
- Support escape hatches for advanced users
- Version templates independently from consuming projects
- Include validation hooks to catch drift from the golden path

### 2. Project Scaffolding & Templates

Create scaffolding systems that generate production-ready project structures.

**Template architecture:**
- Prompt templates: reusable instruction patterns for common tasks
- Code templates: standard patterns for API endpoints, models, tests, migrations
- Workflow templates: stage-based sequences (plan, implement, validate, deploy)
- Review templates: checklists for consistent quality assessment

**Scaffolding workflow:**
1. Identify repetition across teams and projects
2. Extract invariants (structure, quality criteria, required sections)
3. Parameterize variables (names, configurations, domain-specific values)
4. Add guidance with examples of good fill-ins and common mistakes
5. Iterate based on usage feedback and adoption metrics

### 3. MCP Server Development

Build Model Context Protocol servers that enable LLM-to-service integration (see `skills/mcp-builder/SKILL.md`).

**Recommended stack:**
- TypeScript with MCP SDK for broad compatibility
- Streamable HTTP transport for remote servers, stdio for local
- Zod schemas for input validation, structured output schemas

**Implementation phases:**
1. Deep research: study the target API, plan tool coverage
2. Implementation: project structure, core infrastructure, tool registration
3. Review and test: code quality, MCP Inspector verification
4. Evaluation: create 10 complex, realistic test questions

**Tool design principles:**
- Balance comprehensive API coverage with workflow convenience tools
- Use consistent naming prefixes (e.g., `github_create_issue`, `github_list_repos`)
- Return focused, relevant data with pagination support
- Provide actionable error messages that guide toward solutions

### 4. Plugin System Architecture

Design and implement plugin systems for extensibility.

**Plugin anatomy:**
```
plugin-name/
  .claude-plugin/plugin.json   # Manifest: name, version, agents, skills, commands, hooks, mcp
  agents/*.md                   # Agent definitions with YAML frontmatter
  skills/*/SKILL.md             # Skill definitions with progressive disclosure
  commands/*.md                 # Slash commands with argument handling ($1, $ARGUMENTS)
  hooks/hooks.json              # Lifecycle event handlers (PreToolUse, PostToolUse, Stop)
  .mcp.json                     # MCP server configurations
```

**Plugin lifecycle:**
1. Discovery: scan directories for `.claude-plugin/plugin.json` manifests
2. Loading: parse manifest, resolve paths, load all resource types
3. Namespacing: all resources use `plugin-name:resource-name` format
4. Access: typed accessors for agents, skills, commands, hooks, MCP configs

### 5. Developer Experience (DX) Optimization

Evaluate and improve developer workflows, toolchains, and self-service capabilities.

**DX assessment dimensions:**
- Onboarding time: minutes from clone to first meaningful contribution
- Inner loop speed: edit-build-test-debug cycle time
- Cognitive load: number of tools, contexts, and decisions per task
- Self-service coverage: percentage of common tasks achievable without filing tickets
- Documentation quality: accuracy, discoverability, freshness

**Improvement strategies:**
- Automate repetitive setup with scripts (see `root-setup/setup-agentic-coding.sh`)
- Provide CLI wrappers for complex operations
- Create development containers with pre-configured environments
- Build integration connectors for Slack, GitHub, GitLab, Google Drive
- Implement maturity models to track DX improvements (see `proagent/core/skills/tac/maturity-model.md`)

### 6. Internal CLI & SDK Design

Build internal command-line tools and SDKs that wrap platform capabilities.

**CLI design patterns:**
- Rich formatting for terminal output
- Pydantic-based configuration with environment variable loading
- Command registries with argument substitution
- Plugin discovery and auto-loading

**SDK design principles:**
- Type-safe interfaces with comprehensive validation
- Progressive complexity: simple defaults, advanced overrides
- Consistent error handling with actionable messages
- Auto-discovery of extensions and plugins

## Workflow: Building a New Platform Component

1. **Understand the need**: interview stakeholders, gather concrete usage examples
2. **Survey existing assets**: search for similar patterns in the catalog (127 platform assets across 19 repos)
3. **Design the component**: choose the right abstraction (template, skill, command, MCP server, plugin)
4. **Implement**: follow the appropriate pattern from this skill
5. **Validate**: run template validation, DX feedback checks, and user testing
6. **Ship and iterate**: publish to the service catalog, track adoption, refine based on feedback

## Composio App Automations

This plugin integrates with Composio-powered SaaS automation skills via the Rube MCP server. These skills connect to real external services for end-to-end workflow automation.

### Available Automations

| Skill | Service | Key Capabilities |
|-------|---------|-----------------|
| slack-automation | Slack | Send messages, manage channels, create workflows, user management, file sharing |
| notion-automation | Notion | Create/update pages and databases, manage blocks, search content, template management |
| confluence-automation | Confluence | Create/update pages, manage spaces, search content, attach files, label management |
| google-drive-automation | Google Drive | Create/manage files and folders, sharing permissions, search, export/import formats |

### Usage Pattern

All Composio automations follow a three-step workflow:

1. **Discover tools**: Use `RUBE_SEARCH_TOOLS` with a use case description to find available tools and their schemas
2. **Connect service**: Use `RUBE_MANAGE_CONNECTIONS` to activate the toolkit connection (handles OAuth automatically)
3. **Execute actions**: Use `RUBE_MULTI_EXECUTE_TOOL` with the discovered tool slug and schema-compliant arguments

### Configuration

Add the Rube MCP server to your `.mcp.json`:
```json
"rube": {
  "url": "https://rube.app/mcp"
}
```

## Visual Diagramming with Excalidraw

Use the Excalidraw MCP server to generate interactive diagrams directly in the conversation. Describe what you need in natural language and Excalidraw renders it as an interactive canvas with hand-drawn style.

### When to Use

- Platform topology and service catalog maps
- Golden path and developer workflow diagrams
- Internal tooling architecture and scaffolding template relationships
- Developer portal and DX optimization flows

### Workflow

1. Describe the diagram you need — be specific about components, relationships, and layout
2. Review the rendered interactive diagram in the chat
3. Request refinements by describing what to change (add/remove/rearrange elements)
4. Use fullscreen mode for detailed editing when needed

### Tips for Effective Diagrams

- Name specific components and their connections (e.g., "API Gateway connects to Auth Service and User Service")
- Specify layout direction when it matters (e.g., "left-to-right flow" or "top-down hierarchy")
- Request specific diagram types (architecture diagram, flowchart, sequence diagram, ER diagram)
- Iterate — start with the overall structure, then refine details
