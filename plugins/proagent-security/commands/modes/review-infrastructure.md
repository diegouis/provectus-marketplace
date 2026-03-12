# Review: Infrastructure Security

- Overly permissive security groups or firewall rules (0.0.0.0/0 ingress)
- Default VPC or security group usage
- Missing encryption at rest for databases and storage
- IAM policies granting `*` permissions
- Missing logging and monitoring for infrastructure changes
- Publicly accessible resources that should be private (S3 buckets, databases)
- Missing network ACLs and VPC flow logs
