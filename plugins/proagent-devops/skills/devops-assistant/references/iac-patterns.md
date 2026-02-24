## Terraform Module Library

Reference: `agents/plugins/cloud-infrastructure/skills/terraform-module-library/SKILL.md`

### Module Structure

```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
    README.md
  eks-cluster/
    main.tf
    variables.tf
    outputs.tf
  rds/
    main.tf
    variables.tf
    outputs.tf
  s3-bucket/
    main.tf
    variables.tf
    outputs.tf
```

### Module Usage Pattern

```hcl
module "vpc" {
  source = "./modules/vpc"

  project     = var.project
  environment = var.environment
  cidr_block  = "10.0.0.0/16"
  azs         = ["us-east-1a", "us-east-1b", "us-east-1c"]
}

module "eks" {
  source = "./modules/eks-cluster"

  cluster_name = "${var.project}-${var.environment}"
  vpc_id       = module.vpc.vpc_id
  subnet_ids   = module.vpc.private_subnet_ids
  node_groups = {
    default = {
      instance_types = ["m5.large"]
      min_size       = 2
      max_size       = 10
      desired_size   = 3
    }
  }
}
```

### Module Best Practices

- Pin module versions in `source` using tags or commit SHAs
- Every module must define `variables.tf` with descriptions and validation rules
- Every module must define `outputs.tf` for dependent resources
- Use `terraform-docs` to auto-generate module documentation
- Test modules with `terratest` or `terraform test`

## Cloud Cost Optimization

Reference: `agents/plugins/cloud-infrastructure/skills/cost-optimization/SKILL.md`

### Cost Reduction Strategies

| Strategy | Savings Potential | Complexity |
|----------|------------------|------------|
| Right-sizing instances | 20-40% | Low |
| Reserved Instances / Savings Plans | 30-60% | Medium |
| Spot/Preemptible instances for batch | 60-90% | Medium |
| Auto-scaling with schedule-based policies | 20-30% | Low |
| Storage tiering (S3 Intelligent-Tiering, GCS Nearline) | 30-50% | Low |
| Idle resource cleanup | 10-25% | Low |

### Tagging Standards for Cost Allocation

All resources must include these tags:

```hcl
tags = {
  Project     = var.project
  Environment = var.environment
  Team        = var.team
  CostCenter  = var.cost_center
  ManagedBy   = "terraform"
}
```

### Monitoring Cloud Spend

- Enable AWS Cost Explorer or GCP Billing Reports with daily granularity
- Set budget alerts at 50%, 80%, and 100% of monthly budget
- Review AWS Trusted Advisor or GCP Recommender for optimization suggestions
- Track cost-per-service and cost-per-environment in Grafana dashboards
