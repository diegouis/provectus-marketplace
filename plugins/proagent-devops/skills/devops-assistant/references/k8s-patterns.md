## Kubernetes Orchestration

### Application Deployment Pattern

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
spec:
  replicas: 3
  revisionHistoryLimit: 5
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: myapp
    spec:
      serviceAccountName: myapp
      securityContext:
        runAsNonRoot: true
        runAsUser: 1001
      containers:
      - name: myapp
        image: myregistry.io/myapp:1.0.0
        ports:
        - containerPort: 3000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: myapp-secrets
              key: database-url
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /health
            port: 3000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 3000
          initialDelaySeconds: 10
          periodSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: myapp
  namespace: production
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 3000
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: myapp
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
```

### GitOps with ArgoCD

- Store all Kubernetes manifests in a Git repository as the single source of truth
- Use ArgoCD Application CRDs to define sync policies and health checks
- Implement environment promotion via pull requests (dev -> staging -> production)
- Enable auto-sync with self-healing for drift detection and remediation
- Use Kustomize overlays or Helm value files for environment-specific configuration

### Helm Chart Scaffolding

Reference: `agents/plugins/kubernetes-operations/skills/helm-chart-scaffolding/SKILL.md`

When creating new Helm charts:

1. **Initialize the chart structure:**
   ```bash
   helm create <chart-name>
   ```
2. **Standard chart layout:**
   ```
   chart-name/
     Chart.yaml          # Chart metadata and dependencies
     values.yaml         # Default configuration values
     values-staging.yaml # Staging overrides
     values-prod.yaml    # Production overrides
     templates/
       deployment.yaml
       service.yaml
       ingress.yaml
       hpa.yaml
       serviceaccount.yaml
       configmap.yaml
       secrets.yaml
       _helpers.tpl       # Template helpers and named templates
     tests/
       test-connection.yaml
   ```
3. **Best practices:**
   - Maintain a standardized chart structure with Chart.yaml, values.yaml, and templates/
   - Use `.helmignore` to exclude unnecessary files from chart packages
   - Validate charts with `helm lint` and `helm template` before deployment
   - Implement chart testing with `helm test` hooks
   - Version charts semantically and publish to a chart repository
   - Use named templates in `_helpers.tpl` for reusable label and selector blocks
   - Parameterize image tags, replica counts, resource limits, and ingress hosts via values.yaml
