# Mode: Operate

Run lifecycle operations: status, list, clean, connect, disconnect.

## Read the CLI reference first

Read `skills/provrag-developer/references/cli-reference.md` for full command details.

## Operations

### status

Check the project lifecycle stage:

```bash
provrag status
```

Stages: `unknown` -> `scaffolded` -> `configured` -> `repo_created` -> `infra_previewed` -> `infra_deployed` -> `app_built` -> `app_deployed` -> `live`

### list

List all OpenSearch indices:

```bash
provrag list
```

### clean

Delete an OpenSearch index:

```bash
provrag clean --index {name} --yes
```

**Warning**: This permanently deletes all data in the index. Confirm with the user before running.

### connect

Start SSM tunnels to AWS services via the bastion host:

```bash
task connect
```

This establishes port forwarding:
| Local Port | AWS Service |
|------------|-------------|
| `:9200` | OpenSearch VPC endpoint (port 443) |
| `:4200` | Prefect Server via ALB |
| `:6006` | Phoenix via ALB |
| `:8080` | Deployed API via ALB (at `/{slug}/`) |

**Prerequisites before connecting:**
1. AWS SSO session must be active:
   ```bash
   aws sso login --profile provectus-demos
   ```
2. `OPENSEARCH_ENDPOINT` must be set in `.env`
3. Bastion host must be running

**IMPORTANT: Tunnel health monitoring.**

SSM tunnels through the bastion are fragile and can drop silently. After running `task connect`, **proactively verify connectivity** by hitting each endpoint:

```bash
# OpenSearch -- use provrag list (fastest check)
provrag list 2>&1

# API health endpoint
curl -s --max-time 5 http://localhost:8080/{slug}/health 2>&1

# Prefect
curl -s --max-time 5 http://localhost:4200/api/health 2>&1

# Phoenix
curl -s --max-time 5 http://localhost:6006 2>&1 | head -5
```

Run these checks **immediately after connecting** and **before any operation that uses AWS services** (ingest, serve, list, clean).

**If any check fails** (connection refused, timeout, SSL error, empty response):

1. Disconnect all tunnels:
   ```bash
   task disconnect
   ```
2. Verify SSO session is still active:
   ```bash
   aws sts get-caller-identity --profile provectus-demos 2>&1
   ```
   If expired, re-login: `aws sso login --profile provectus-demos`
3. Reconnect:
   ```bash
   task connect
   ```
4. Re-verify all endpoints using the checks above
5. If tunnels fail again after 2 attempts, check:
   - Is the bastion host running? `aws ec2 describe-instances --filters "Name=tag:Name,Values=provrag-bastion-bastion" "Name=instance-state-name,Values=running" --query 'Reservations[0].Instances[0].InstanceId' --output text --profile provectus-demos --region us-east-2`
   - Is `OPENSEARCH_ENDPOINT` correct in `.env`?
   - Are there network/VPN issues?

**Be proactive**: Do not wait for a user to report a broken tunnel. If you run any command that fails with connection errors, immediately trigger the disconnect/reconnect cycle above.

### disconnect

Kill all active SSM tunnel sessions:

```bash
task disconnect
```

Verify tunnels are stopped:
```bash
ps aux | grep 'aws ssm start-session' | grep -v grep || echo "No active tunnels"
```
