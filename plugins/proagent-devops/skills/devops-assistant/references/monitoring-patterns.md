## Monitoring and Observability

### Prometheus Metrics Collection

Key metrics to track:
- `request_duration_seconds` - Request latency histogram
- `requests_total{status}` - Request counter by status code
- `active_connections` - Current active connections gauge
- `deployment_duration_seconds` - Deployment time histogram
- `deployment_status{environment, result}` - Deployment outcome counter

### Alerting Rules

```yaml
groups:
  - name: application
    rules:
      - alert: HighErrorRate
        expr: rate(requests_total{status=~"5.."}[5m]) / rate(requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected (> 5%)"

      - alert: HighLatency
        expr: histogram_quantile(0.95, rate(request_duration_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "P95 latency above 2 seconds"

      - alert: PodCrashLooping
        expr: rate(kube_pod_container_status_restarts_total[15m]) > 0
        for: 15m
        labels:
          severity: critical
        annotations:
          summary: "Pod {{ $labels.pod }} is crash looping"
```

## Prometheus and Grafana Configuration

### Prometheus Configuration

Reference: `agents/plugins/observability-monitoring/skills/prometheus-configuration/SKILL.md`
Production example: `casdk-harness/config/monitoring/alerting.yml`

Key scrape targets to configure:

```yaml
scrape_configs:
  - job_name: 'application'
    metrics_path: /metrics
    static_configs:
      - targets: ['api:3000']
  - job_name: 'node-exporter'
    static_configs:
      - targets: ['node-exporter:9100']
  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: true
```

### Grafana Dashboard Patterns

Reference: `agents/plugins/observability-monitoring/skills/grafana-dashboards/SKILL.md`

Dashboard organization:

- **Service Overview** - RED metrics (request rate, error rate, duration) per service
- **Infrastructure** - CPU, memory, disk, network per node and container
- **Kubernetes** - Pod status, deployment rollout, HPA scaling events, resource quotas
- **Business Metrics** - Custom application KPIs and SLO burn rate
- **Cost** - Cloud spend by service, environment, and team
