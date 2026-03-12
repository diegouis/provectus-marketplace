# Review: Container Security

- Running as root (missing `USER` directive in Dockerfile)
- Using `latest` tag instead of pinned versions
- SSH private keys or secrets mounted into containers
- Missing `HEALTHCHECK` directive
- Docker socket exposed to containers (privilege escalation risk, CVSS 9.0)
- Missing resource limits (CPU, memory) enabling resource exhaustion
- Plaintext checkpoint or state data without encryption (CVSS 9.1)
- Missing network segmentation between service tiers
- Base images not scanned for vulnerabilities
