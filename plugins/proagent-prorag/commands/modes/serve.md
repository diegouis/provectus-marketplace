# Mode: Serve

Test the RAG query API. The API is already running in AWS -- `task connect` tunnels it to localhost.

## Workflow

### 1. Verify tunnels are active

```bash
provrag list 2>&1
```

If this fails (connection refused, timeout), reconnect:
```bash
task disconnect && task connect
```

### 2. Verify the API is reachable

```bash
curl -s --max-time 5 http://localhost:8080/{slug}/health 2>&1
```

If the health check fails, the tunnel to port 8080 may be down. Disconnect and reconnect.

### 3. Verify index has data

```bash
provrag list
```

If the target index is empty or missing, suggest running ingestion first.

### 4. Query the API

```bash
curl -X POST http://localhost:8080/{slug}/query \
  -H 'Content-Type: application/json' \
  -d '{"query": "your question here", "top_k": 5}'
```

### 5. Observability

If Phoenix is running (tunneled via `task connect`):
- Open Phoenix UI: `http://localhost:6006`
- View traces for each query (embedding, retrieval, generation spans)

If Prefect is running (tunneled via `task connect`):
- Open Prefect UI: `http://localhost:4200`
- View flow runs for each query execution

### 6. Report

Tell the user:
- API URL and endpoints (`http://localhost:8080/{slug}/query`)
- Sample query and response
- Where to view traces (Phoenix at :6006)
