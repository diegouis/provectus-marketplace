# Agent Harden — Harden Agent Deployment

Apply production security hardening for autonomous agent deployments (reference: `casdk-harness/src/harness/security.py`, `casdk-harness/docs/HARDENING.md`).

**Steps:**
1. **Assess current agent configuration:**
   - Check for permission boundaries and sandbox configuration
   - Identify filesystem, network, and process access scope
   - Review trust level assignment and escalation policies
2. **Apply sandboxing controls:**
   - Restrict filesystem access to designated working directories
   - Limit network access to approved endpoints and protocols
   - Set execution time limits and resource caps (CPU, memory)
   - Disable access to secrets and credentials not required for the task
3. **Configure audit logging:**
   - Enable immutable logging of all agent actions
   - Record tool invocations, file modifications, and external API calls
   - Set up alerts for anomalous behavior patterns
4. **Validate hardening:**
   - Test that sandbox restrictions are enforced
   - Verify agent cannot escalate beyond assigned trust level
   - Confirm audit logs capture all security-relevant events
5. **Generate hardening report:**
   - Current vs recommended security posture
   - Applied restrictions and remaining gaps
   - Ongoing monitoring recommendations
