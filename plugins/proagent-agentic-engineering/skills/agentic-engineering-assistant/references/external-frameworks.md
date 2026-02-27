# External Framework Reference Cards

> These cards describe external frameworks referenced by this plugin. For each framework, we list what it does, when to use it, and where to find deep documentation.
>
> **Important:** This plugin does NOT contain the implementation code for these frameworks. Install them separately for full functionality.

---

## ralph-orchestrator
- **Language:** Rust
- **What it does:** Event-loop-driven autonomous coding with explore-plan-code-commit cycle and multi-backend LLM support (Claude, Kiro, Gemini, Codex)
- **When to use:** Rust projects or when you need multi-backend LLM orchestration with configurable presets
- **Key concepts:** Event loop engine, YAML presets (e.g., `presets/feature.yml`), backend adapters
- **Context confidence:** 40% -- we know the architecture but not implementation details
- **For deep knowledge:** Consult the framework's own documentation and source code

---

## casdk-harness
- **Language:** Python
- **What it does:** Claude SDK native harness with AgentSession, autonomous mode, and plugin lifecycle management (discovery, namespacing, hot-reload)
- **When to use:** Python projects needing Claude SDK integration with plugin ecosystem
- **Key concepts:** AgentSession, autonomous mode, plugin discovery, bundled plugins (context-engineering, research-team)
- **Context confidence:** 40% -- we know class names and purposes but not constructor parameters or MCP integration mechanics
- **For deep knowledge:** Consult the framework's own documentation and source code

---

## Auto-Claude
- **Language:** Python
- **What it does:** Multi-agent coding framework with tool registry for dynamic capabilities and Graphiti knowledge graph integration for persistent context
- **When to use:** Projects needing persistent knowledge graph context across sessions
- **Key concepts:** Agent pipeline, tool registry, Graphiti knowledge graph integration
- **Context confidence:** 20% -- minimal implementation details available
- **For deep knowledge:** Consult the framework's own documentation and source code

---

## gastown
- **Language:** Go
- **What it does:** Multi-agent orchestration CLI with molecule-based workflow composition and declarative orchestration formulas
- **When to use:** Go projects needing declarative, molecule-based multi-agent workflows
- **Key concepts:** CLI entry point, "molecule" concept, TOML formulas (`.beads/formulas/`)
- **Context confidence:** 20% -- only high-level architecture known
- **For deep knowledge:** Consult the framework's own documentation and source code

---

## AWOS (Architecture-Workflow-Output-Specification)
- **Language:** Python (Claude Code plugin)
- **What it does:** 4-command pipeline for spec-driven development: `/architecture` -> `/spec` -> `/implement` -> `/verify`
- **When to use:** When you need structured spec-driven development with confirmation gates between stages
- **Key concepts:** Session persistence (JSON state), file-based step detection, configurable confirmation gates (`AWOS_SPEC_REFINEMENT`)
- **Context confidence:** 50% -- pipeline stages documented but actual command implementations not present
- **For deep knowledge:** Install the AWOS plugin separately for full command implementations

---

## ProAgent ZTE Trust Ladder
- **Language:** Python (ProAgent core)
- **What it does:** 5-level progressive autonomy framework controlling what agents can do without human approval
- **Levels:**
  1. **Observer** -- read-only, no modifications
  2. **Assistant** -- suggests changes, human approves
  3. **Collaborator** -- makes changes with confirmation gates
  4. **Delegator** -- autonomous within defined scope
  5. **Autonomous** -- full autonomy with audit trail
- **When to use:** When you need progressive trust escalation for agent systems
- **Context confidence:** 30% -- level names and descriptions known but measurement criteria and CLI enforcement not documented
- **For deep knowledge:** Consult the ProAgent ZTE module source code
