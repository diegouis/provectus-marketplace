# Mode: Architecture Interview

Conduct a structured 4-phase interview to capture all RAG architecture decisions before scaffolding. Produces a `.provrag-spec.json` consumed by init, customize-ingestion, and customize-rag modes.

## Quick-Start Path

If the user says "just defaults", "use defaults", or "quick start":
1. Generate `.provrag-spec.json` with all defaults (see Phase defaults below)
2. Present a single summary table of all decisions
3. Ask: "Confirm these defaults or tell me what to change?"
4. On confirmation, write the spec and route to execution

## Pre-Fill Path

Parse the user's original request for known decisions before starting. Fill what you can, interview only the gaps. Examples:
- "legal PDFs" → `purpose: "legal document search"`, `file_types: ["pdf"]`
- "hybrid search with reranking" → `search_type: "hybrid"`, `reranker: "cross-encoder-ms-marco"`
- "multilingual" → `language: "multilingual"`
- "production on AWS" → `environment: "aws"`

Present pre-filled values as confirmed and skip those questions.

---

## Phase 1 — Project & Data Layer

Collect these decisions. Present defaults so the user can confirm or override:

| Decision | Options | Default |
|----------|---------|---------|
| **Project name** | free text (required) | — |
| **Purpose** | free text | "RAG application" |
| **Document sources** | `s3` / `local` / `urls` / `database` | `s3` |
| **File types** | `text` / `pdf` / `mixed` / `code` / `html` | `text` |
| **Document language** | `english` / `multilingual` | `english` |
| **Data volume** | `small` (<1K docs) / `medium` (1K–100K) / `large` (100K+) | `small` |
| **Update pattern** | `one-time` / `periodic-full` / `incremental` | `one-time` |
| **Metadata to extract** | free text (what fields to index alongside content) | `"source, title"` |

### After Phase 1

Present a summary table of Phase 1 decisions, then ask:
> "Phase 1 complete. Confirm these choices or tell me what to revise."

Only proceed to Phase 2 after confirmation.

---

## Phase 2 — Chunking & Embedding

| Decision | Options | Default |
|----------|---------|---------|
| **Chunking strategy** | `recursive-character` / `sentence` / `markdown-aware` / `token-aware` | `recursive-character` |
| **Chunk size** | integer (tokens/chars) | `512` |
| **Chunk overlap** | integer | `50` |
| **Embedding provider** | `bedrock-titan-v2` (1024d) / `openai-text-embedding-3-small` (1536d) | derived from environment |
| **Environment** | `local` (OpenAI + MinIO) / `aws` (Bedrock + S3) | `local` |

Auto-derivation rules:
- If `environment: "aws"` → default embedding = `bedrock-titan-v2`, dimension = `1024`
- If `environment: "local"` → default embedding = `openai-text-embedding-3-small`, dimension = `1536`

### After Phase 2

Present summary table, then ask for confirmation before proceeding.

---

## Phase 3 — Retrieval & Search

| Decision | Options | Default |
|----------|---------|---------|
| **Search type** | `dense` (k-NN only) / `hybrid` (BM25 + k-NN) | `dense` |
| **Top-k** | integer | `10` |
| **BM25 weight** | float 0–1 (only if hybrid) | `0.3` |
| **k-NN weight** | float 0–1 (only if hybrid) | `0.7` |
| **Reranker** | `none` / `cross-encoder-ms-marco` / `cross-encoder-bge` | `none` |
| **Rerank top-k** | integer (only if reranker set) | `5` |
| **Index engine** | `faiss` / `nmslib` / `lucene` | `faiss` |

Mark index engine as **advanced** — offer to skip: "Index engine defaults to FAISS. Want to change it? (most users skip this)"

### Conditional questions

- Only ask BM25/k-NN weights if `search_type: "hybrid"`
- Only ask rerank top-k if reranker is not `none`

### After Phase 3

Present summary table, then ask for confirmation.

---

## Phase 4 — Generation & Operations

| Decision | Options | Default |
|----------|---------|---------|
| **System prompt** | free text (domain persona + constraints) | `"You are a helpful assistant. Answer questions based only on the provided context."` |
| **Source citations** | `yes` / `no` | `no` |
| **LLM model** | `claude-3-sonnet` / `claude-3-haiku` / `gpt-4` | derived from environment |
| **Temperature** | float 0–1 | `0.1` |
| **Tracing** | `phoenix` / `none` | `phoenix` |

Auto-derivation:
- If `environment: "aws"` → default LLM = `claude-3-sonnet`
- If `environment: "local"` → default LLM = `gpt-4`

### After Phase 4

Present a **full summary** across all 4 phases, then ask:
> "Architecture complete. Confirm to generate the spec, or tell me what to revise."

---

## Generate .provrag-spec.json

After final confirmation, write `.provrag-spec.json` to the current working directory using the Write tool:

```json
{
  "version": "1.0",
  "project": {
    "name": "<project-name>",
    "slug": "<project-slug>",
    "purpose": "<purpose>",
    "description": "RAG application built with ProRAG"
  },
  "data": {
    "sources": "<s3|local|urls|database>",
    "file_types": ["<text|pdf|mixed|code|html>"],
    "language": "<english|multilingual>",
    "volume": "<small|medium|large>",
    "update_pattern": "<one-time|periodic-full|incremental>",
    "metadata_fields": ["<field1>", "<field2>"]
  },
  "chunking": {
    "strategy": "<recursive-character|sentence|markdown-aware|token-aware>",
    "chunk_size": 512,
    "chunk_overlap": 50
  },
  "embedding": {
    "provider": "<bedrock-titan-v2|openai-text-embedding-3-small>",
    "dimension": 1024,
    "environment": "<local|aws>"
  },
  "retrieval": {
    "search_type": "<dense|hybrid>",
    "top_k": 10,
    "bm25_weight": 0.3,
    "knn_weight": 0.7,
    "reranker": "<none|cross-encoder-ms-marco|cross-encoder-bge>",
    "rerank_top_k": 5,
    "index_engine": "<faiss|nmslib|lucene>"
  },
  "generation": {
    "system_prompt": "<prompt text>",
    "source_citations": false,
    "llm_model": "<claude-3-sonnet|claude-3-haiku|gpt-4>",
    "temperature": 0.1,
    "tracing": "<phoenix|none>"
  }
}
```

Derive `slug` from `name` using lowercase + hyphens (e.g., "Acme Legal RAG" → "acme-legal-rag").

Omit conditional fields that don't apply (e.g., `bm25_weight`/`knn_weight` if `search_type: "dense"`, `rerank_top_k` if `reranker: "none"`).

## After Spec Generation

Report the spec file location, then route to execution:

1. Invoke Skill: `proagent-provrag-run` args: `init` — the init mode will read the spec and pre-fill parameters
2. After init completes, suggest next steps based on the spec:
   - If `file_types` includes `pdf` → "Run `/proagent-provrag-run customize-ingestion` to add PDF support"
   - If `search_type: "hybrid"` or `reranker` is set → "Run `/proagent-provrag-run customize-rag` to configure retrieval"
   - If `system_prompt` is custom → "Run `/proagent-provrag-run customize-rag` to apply your system prompt"
