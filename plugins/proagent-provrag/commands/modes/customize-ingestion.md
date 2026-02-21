# Mode: Customize Ingestion

Modify the ingestion pipeline for specific requirements.

## Workflow

### 1. Load the customization cookbook

Read `skills/provrag-developer/references/customization-cookbook.md` for concrete recipes.

(The core SKILL.md is already loaded by the run dispatcher.)

### 2. Read current implementation

```
Read src/{package}/ingestion.py
Read src/{package}/steps.py
Read tests/test_ingestion.py
Read tests/test_steps.py
Read pyproject.toml
```

### 3. If the project has a .venv, read live provrag API

Resolve the installed provrag source paths and read the relevant files:
```bash
uv run python -c "import provrag.pipelines.ingestion; print(provrag.pipelines.ingestion.__file__)"
uv run python -c "import provrag.storage.s3; print(provrag.storage.s3.__file__)"
uv run python -c "import provrag.chunking.text_chunker; print(provrag.chunking.text_chunker.__file__)"
```

### 4. Identify the customization

Ask the user what they need. Common options:
- **PDF ingestion** -- Parse PDF files instead of plain text
- **Custom chunking** -- Sentence-based, markdown-aware, or fixed-size
- **Mixed file types** -- Handle PDFs, TXT, CSV, etc. in one pipeline
- **Metadata enrichment** -- Add extra metadata before chunking
- **Custom preprocessing** -- Domain-specific text cleaning

### 5. Apply the recipe

Follow the corresponding recipe from the customization cookbook:
1. Add new `@step` function(s) to `steps.py`
2. Update `ingestion.py` to use the new step(s)
3. Add required dependencies to `pyproject.toml` with `uv add`
4. Write tests for new steps in `tests/test_steps.py`
5. Update ingestion pipeline tests in `tests/test_ingestion.py`

### 6. Code style enforcement

Verify the implementation follows provrag conventions:
- `from __future__ import annotations` at top
- `TYPE_CHECKING` guards for protocol types
- `@step` decorator with appropriate `name` and `span_kind`
- `model_copy(update={...})` for Pydantic model updates
- No unnecessary comments or docstrings
- Ruff line-length 120

### 7. Verify

```bash
task check
```

This runs lint + typecheck + test. Fix any issues before reporting success.

### 8. Sync dependencies if new ones were added

```bash
uv sync --extra dev
```
