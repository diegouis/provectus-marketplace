# Mode: Customize RAG

Modify the RAG query pipeline for specific requirements.

## Workflow

### 1. Load the customization cookbook

Read `skills/provrag-developer/references/customization-cookbook.md` for concrete recipes.

(The core SKILL.md is already loaded by the run dispatcher.)

### 2. Read current implementation

```
Read src/{package}/pipeline.py
Read src/{package}/steps.py
Read src/{package}/app.py
Read tests/test_pipeline.py
Read tests/test_steps.py
```

### 3. If the project has a .venv, read live provrag API

```bash
uv run python -c "import provrag.pipelines.rag; print(provrag.pipelines.rag.__file__)"
uv run python -c "import provrag.retrieval.opensearch_client; print(provrag.retrieval.opensearch_client.__file__)"
```

### 4. Identify the customization

Ask the user what they need. Common options:
- **Cross-encoder reranking** -- Replace naive score-sort with transformer-based reranking
- **Hybrid search** -- Combine BM25 lexical + k-NN semantic search
- **Custom system prompt** -- Domain-specific generation instructions
- **Query expansion** -- LLM-powered query reformulation before retrieval
- **Response formatting** -- Custom answer structure

### 5. Apply the recipe

Follow the corresponding recipe from the customization cookbook:

#### For cross-encoder reranking:
1. Replace `rerank` in `steps.py` with cross-encoder implementation
2. Add `sentence-transformers` dependency
3. Consider module-level model caching for production
4. Update tests with mocked `CrossEncoder`

#### For hybrid search:
1. Add `hybrid_retrieve` and `setup_hybrid_pipeline` steps to `steps.py`
2. Update `pipeline.py` to use `hybrid_retrieve` instead of `dense_retrieve`
3. Update `ingestion.py` to call `setup_hybrid_pipeline` after `create_index`
4. Update tests for new retrieval step

#### For custom system prompt:
1. Define `SYSTEM_PROMPT` constant in `pipeline.py`
2. Pass `system_prompt=SYSTEM_PROMPT` to `generate_answer`

#### For query expansion:
1. Add `expand_query` step to `steps.py`
2. Insert before `embed_query` in the pipeline
3. Consider using expanded query for hybrid text search, original for vector

### 6. Update app.py if needed

If new pipeline parameters were added, ensure `app.py` passes them correctly via `create_app(**pipeline_kwargs)`.

### 7. Code style enforcement

Same rules as ingestion customization:
- `from __future__ import annotations`
- `TYPE_CHECKING` guards
- `@step` with `name` and `span_kind`
- `cast("str", ...)` for pipeline return
- No unnecessary comments

### 8. Verify

```bash
task check
```

Fix any lint, type, or test issues.
