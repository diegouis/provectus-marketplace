# Mode: Bootstrap

Check and install all prerequisites for using provrag.

## Workflow

### 1. Read the reference

Read `skills/provrag-developer/references/cli-reference.md` for the full bootstrap details.

### 2. Check each prerequisite

Run these checks in parallel where possible:

```bash
# Check each tool
which git && git --version
which docker && docker --version && docker info > /dev/null 2>&1
which mise && mise --version
python3 --version 2>&1 | grep -q '3.13'
which uv && uv --version
which task && task --version
which aws && aws --version
which pulumi && pulumi version
which glab && glab --version
```

### 3. Check AWS SSO

```bash
aws sts get-caller-identity --profile provectus-demos 2>&1
```

If expired or not configured:
```bash
aws sso login --profile provectus-demos
```

### 4. Check GitLab authentication

```bash
glab auth status --hostname gitlab.provectus.com 2>&1
```

### 5. Check Docker daemon

```bash
docker info > /dev/null 2>&1
```

If Docker is installed but daemon not running, tell the user to start Docker Desktop.

### 6. Report status

Present a summary table:

| Tool | Status | Action |
|------|--------|--------|
| git | OK / Missing | Install instructions |
| Docker | OK / Not running | Start Docker Desktop |
| mise | OK / Missing | `curl https://mise.run \| sh` |
| Python 3.13 | OK / Missing | `mise install python@3.13` |
| uv | OK / Missing | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| go-task | OK / Missing | `brew install go-task` |
| AWS CLI | OK / Missing | `brew install awscli` |
| AWS SSO | OK / Expired | `aws sso login --profile provectus-demos` |
| Pulumi | OK / Missing | `curl -fsSL https://get.pulumi.com \| sh` |
| glab | OK / Missing | `brew install glab` |
| glab auth | OK / Not authenticated | `glab auth login --hostname gitlab.provectus.com` |

### 7. Alternative: Run bootstrap script

If the user has the provrag repository cloned, offer to run the interactive bootstrap script:

```bash
bash ~/Documents/GitLab/provrag/scripts/bootstrap.sh
```

This handles installation interactively with prompts.

### 8. Final check

If all prerequisites pass, report ready for `provrag init`.

If issues remain, list them clearly with installation commands.
