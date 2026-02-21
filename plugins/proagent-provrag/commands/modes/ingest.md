# Mode: Ingest

Run the ingestion pipeline to load, process, and index documents.

## Workflow

### 1. Verify environment

Ensure AWS SSM tunnels are active:

**For AWS environment:**
```bash
# Ensure SSO is active
aws sts get-caller-identity --profile provectus-demos
# Start tunnels if needed
task connect
```

After connecting, **verify tunnels are healthy** before proceeding:
```bash
provrag list 2>&1
```
If this fails (connection refused, timeout), disconnect and reconnect:
```bash
task disconnect && task connect
```
Then re-verify. See the `operate` mode's connect section for full troubleshooting.

### 2. Verify documents exist

Check documents in S3:
```bash
aws s3 ls s3://{bucket}/ --profile provectus-demos
```

If no documents exist, guide the user to upload:
```bash
aws s3 cp ./documents/ s3://{bucket}/docs/ --recursive --profile provectus-demos
```

### 3. Run ingestion

**IMPORTANT**: Ingestion can take several minutes depending on document count and pipeline complexity. Always run it in the background to avoid timeout killing the process.

Use the Bash tool with `run_in_background: true`:

```bash
set -a && source .env && set +a && provrag ingest --index {index} --pipeline {package}.ingestion:ingest_pipeline 2>&1
```

Or with prefix filter:
```bash
set -a && source .env && set +a && provrag ingest --index {index} --prefix "pdfs/" --pipeline {package}.ingestion:ingest_pipeline 2>&1
```

Or using Taskfile:
```bash
task ingest 2>&1
```

After launching, use `TaskOutput` with `block: false` to check progress periodically. Wait for the process to complete before verifying results.

### 4. Verify results

Once ingestion finishes:

```bash
provrag list
```

This shows all OpenSearch indices with their document counts.

### 5. Report

Tell the user:
- Number of documents loaded
- Number of chunks indexed
- Index name for use with `provrag serve`
- Any errors encountered
