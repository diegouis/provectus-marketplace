## GitOps Workflow Patterns

Reference: `agents/plugins/kubernetes-operations/skills/gitops-workflow/SKILL.md`

### ArgoCD Application Pattern

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: myapp
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/k8s-manifests.git
    targetRevision: main
    path: environments/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
```

### Environment Promotion Flow

1. Developer merges feature branch into `main` in the application repo
2. CI pipeline builds and pushes container image, updates image tag in the GitOps manifests repo
3. ArgoCD detects the manifest change and syncs to the staging environment
4. After validation, promote to production via pull request updating `environments/production/` values
5. ArgoCD syncs production after PR merge with automatic self-healing enabled
