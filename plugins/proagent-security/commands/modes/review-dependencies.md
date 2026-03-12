# Review: Dependency Vulnerabilities

Check for these issues:

- Known CVEs in direct dependencies (check against NVD, GitHub Advisory Database)
- Outdated dependencies with available security patches
- Yanked or deprecated packages still in use
- Dependency confusion risk (private package names that could be squatted)
- Overly permissive version ranges that could pull malicious updates
- Missing lock files (package-lock.json, Pipfile.lock, go.sum)
- Unmaintained dependencies (no updates in 12+ months with open security issues)
