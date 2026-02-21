# Mode: Init

Scaffold a new provrag project and monitor its setup progress.

## Workflow

### 1. Verify prerequisites

Check that key tools are available:
```bash
which provrag uv task aws glab 2>&1
```

If any are missing, suggest running the `bootstrap` operation first.

### 2. Gather project parameters

Ask the user for these parameters, **always presenting the defaults** so they can just confirm:

- **Project name** (required) -- e.g., "acme-legal-rag"
- **Description** -- default: "RAG application built with provrag"
- **OpenSearch index name** -- default: `{slug}-docs` (derived from project name)
- **Embedding dimension** -- default: `1024` (Titan v2)
- **GitLab group** -- default: `provectus-internals/MLP-COL/ai-accelerators/provrag-projects` (or `--no-gitlab` to skip)
- **Author** -- default: "Provectus"

Present all parameters at once with their defaults so the user only needs to override what they want to change.

### 3. Scaffold the project

```bash
provrag init --name "{name}" --description "{description}" \
  --index {index} --dimension {dimension} \
  --gitlab-group {group}
```

Or with `--no-gitlab` if skipping GitLab:
```bash
provrag init --name "{name}" --description "{description}" \
  --index {index} --dimension {dimension} --no-gitlab
```

### 4. Set up the project

```bash
cd {project-slug}
task ca:login
task setup
```

### 5. Launch status monitor

After scaffolding, launch a background status monitor using the Bash tool with `run_in_background: true`:

```bash
cd {project-slug} && for i in $(seq 1 10); do echo "--- Check $i at $(date) ---"; provrag status 2>&1; echo ""; sleep 30; done
```

This polls `provrag status` every 30 seconds for 5 minutes. Use the TaskOutput tool or Read tool on the output file to check progress.

The stages in order are:
`unknown` -> `scaffolded` -> `configured` -> `repo_created` -> `infra_previewed` -> `infra_deployed` -> `app_built` -> `app_deployed` -> `live`

Check the output periodically and report to the user when:
- The stage reaches `configured` (for `--no-gitlab` projects) or `repo_created` (for GitLab projects)
- An error is detected in the output
- All 10 checks have completed

### 6. Verify project structure

```bash
ls -la {project-slug}/src/{package}/
ls -la {project-slug}/tests/
```

Confirm these files exist:
- `src/{package}/app.py`
- `src/{package}/pipeline.py`
- `src/{package}/ingestion.py`
- `src/{package}/steps.py`
- `tests/test_pipeline.py`
- `tests/test_steps.py`
- `tests/test_ingestion.py`
- `pyproject.toml`
- `Taskfile.yml`
- `.env`

### 7. Run initial checks

```bash
cd {project-slug}
task check
```

### 8. Report next steps

Tell the user:
1. Upload documents to the S3 bucket (`aws s3 cp ./documents/ s3://{bucket}/ --recursive --profile provectus-demos`)
2. Customize pipelines if needed (PDF support, reranking, etc.)
3. Run ingestion: `task ingest` or `provrag ingest`
4. Start server: `task serve` or `provrag serve`
5. For AWS: `task connect` to establish SSM tunnels
