# Review: CI/CD Pipeline Security

- Secrets hardcoded in pipeline configuration
- GitHub Actions using unpinned action versions (`@latest` instead of SHA)
- Missing `permissions` restrictions on workflow jobs
- No security scanning step (CodeQL, Bandit, Trivy, npm audit)
- Overly broad IAM permissions for deployment credentials
- Missing deployment gates and approval requirements for production
- Pull request pipelines executing untrusted code with elevated permissions
- Missing branch protection rules on main/production branches
