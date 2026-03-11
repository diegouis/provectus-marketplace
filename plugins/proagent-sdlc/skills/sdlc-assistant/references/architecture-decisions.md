# Architecture Decisions, ADRs, and C4 Diagrams

## Architecture Decisions

Follows the AWOS collaborative architecture pattern: read product definition and roadmap, then work through architectural areas section-by-section with the user, proposing technologies with alternatives and justifications. Produces a structured `architecture.md` covering stack, databases, infrastructure, and integration points.

**Key steps:**
- Check prerequisites: product definition and roadmap must exist
- Detect mode: creation vs. update
- Interactive design: propose areas, suggest technologies with alternatives, clarify and confirm
- Finalize and save to `context/product/architecture.md`
- Review subagent coverage against chosen technologies

## Architecture Decision Records (ADRs)

Generates ADRs following the pattern from agents repo (`plugins/documentation-generation/skills/architecture-decision-records/SKILL.md`). Each ADR captures a single architectural decision with full context.

**ADR structure:**
- Title: short descriptive name
- Status: proposed, accepted, deprecated, superseded
- Context: what forces are at play, what is the problem
- Decision: what was decided and why
- Consequences: what becomes easier, what becomes harder
- Alternatives considered: with trade-off analysis

## C4 Architecture Diagrams

Generates C4 model documentation following the pattern from agents repo (`plugins/c4-architecture/agents/c4-context.md`).

**C4 levels:**
- Context: system boundaries, external actors, and integrations
- Container: applications, data stores, and communication protocols
- Component: internal modules, services, and their responsibilities
- Code: class/module level detail (optional, for critical paths only)

Output as structured markdown with Excalidraw or Mermaid diagram descriptions.
