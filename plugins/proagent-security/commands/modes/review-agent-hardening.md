# Review: Agent Hardening

Review autonomous agent security posture (reference: `casdk-harness/src/harness/security.py`, `casdk-harness/docs/HARDENING.md`):

- Agent sandbox configuration (filesystem, network, process restrictions)
- Trust level assignment and escalation policies (`proagent-repo/core/skills/tac/trust-ladder.md`)
- Permission boundaries preventing privilege escalation
- Audit logging coverage for agent actions
- Resource limits (CPU, memory, execution time) to prevent abuse
- Session isolation between concurrent agent tasks
