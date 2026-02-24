### 8. Prompt Engineering and Context Engineering

Design effective prompts and manage context for optimal agent performance.

**Agentic Development Workflow (ADW)**:
- Structured workflow for agent-assisted development
- Phases: Explore, Plan, Code, Commit
- Progressive context building

**Trust Ladder** (ProAgent ZTE -- `proagent-repo core/zte/trust_ladder.py`):
- Progressive agent autonomy model with 5 levels
- Levels: Observer -> Assistant -> Collaborator -> Delegator -> Autonomous
- Increase trust as agent demonstrates competence
- Each level unlocks additional tool permissions and reduces confirmation gates
- Gastown escalation system provides complementary trust management for multi-agent teams

**Core Four TAC Principles**:
- Task framing, autonomy calibration, context management, review cadence

**Prompt-Driven Development**:
- Treat prompts as first-class engineering artifacts
- Version control, review, and iterate on prompts
- Evaluate prompt effectiveness with structured criteria

**Session Handoff**:
- Context preservation between sessions
- State serialization and recovery
- Checkpoint management
- Setup-ralph skill (`taches-cc-resources skills/setup-ralph/SKILL.md`) for bootstrapping loop context

**Thinking Model Commands** (taches-cc-resources):
- First-principles reasoning (`commands/consider/first-principles.md`) for structured decomposition before implementation
- Apply mental models to agent design decisions, architecture tradeoffs, and debugging strategies
- Use structured thinking before committing to orchestration patterns or agent architectures

### 9. Agent Evaluation

Test and evaluate agent system effectiveness.

**Evaluation Approaches**:
- Conversational evaluation framework
- Task-based assessment with clear success criteria
- Multi-dimensional scoring (accuracy, completeness, efficiency)

**MCP Server Evaluations**:
- Create 10 evaluation questions per MCP server
- Requirements: independent, read-only, complex, realistic, verifiable, stable
- XML output format with `<qa_pair>` elements

**Verification Before Completion**:
- Evidence-based verification before declaring success
- Run tests, check outputs, validate against requirements
- Never rely on assumptions about what was done
