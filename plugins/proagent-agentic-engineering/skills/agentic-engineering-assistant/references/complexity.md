# Complexity Assessment

Before generating artifacts, assess the complexity of the request. This determines the depth of every artifact you produce.

## Simple (1 artifact, minimal sections)

**Indicators:** Single clear task, no chaining, no external dependencies, fits in one file.
**Examples:** "a hook that blocks rm -rf", "a command that runs tests and reports results"

**Artifact depth:**
- Frontmatter: all fields
- Body: Variables, Workflow (3-5 steps), Error Handling (Gate Guard only), Report
- Skip: Instructions section (rules are obvious), Expertise section, Contracts

## Medium (2-3 artifacts, standard sections)

**Indicators:** Multi-step task, some chaining, clear data flow, moderate domain knowledge needed.
**Examples:** "a scout-then-plan pipeline", "an agent that reviews code with a validation hook"

**Artifact depth:**
- Frontmatter: all fields
- Body: Variables, Instructions, Workflow (5-10 steps), Error Handling (Gate Guard + Step Fallback), Report
- Include: Inter-Artifact Contracts for each connection
- Skip: Expertise section unless domain-specific

## Complex (full pipeline or expert trio, all sections)

**Indicators:** Multi-artifact orchestration, deep domain expertise needed, self-improvement desired, agent teams.
**Examples:** "a self-improving documentation system", "an agent team for full-stack development"

**Artifact depth:**
- Frontmatter: all fields with careful model/tool selection
- Body: ALL sections -- Variables, Instructions, Expertise, Workflow (10+ steps), Error Handling (all patterns), Report
- Include: Inter-Artifact Contracts, coordinator command, Design Decisions documented in specs/
- Include: Expertise sections for domain knowledge, Critical First Step for agents
- Consider: Expert System trio (plan/build/improve) if the domain benefits from learning
