# Mode: Add Step

Add a new custom pipeline step.

## Workflow

### 1. Refer to the SKILL.md

The core SKILL.md (already loaded by the run dispatcher) has the `@step` decorator reference.

### 2. Determine step details

Ask the user:
- **Purpose**: What does this step do?
- **Inputs**: What types does it receive? (e.g., `list[Document]`, `list[ScoredChunk]`, `str`)
- **Outputs**: What does it return?
- **Pipeline**: Which pipeline does it belong to? (ingestion or RAG)
- **Position**: Where in the pipeline should it run?

### 3. Choose span_kind

| Span Kind | Use for |
|-----------|---------|
| `CHAIN` | General transformation, filtering, formatting |
| `EMBEDDING` | Embedding operations |
| `RETRIEVER` | Search and retrieval operations |
| `LLM` | Language model calls |

### 4. Write the step

Add to `src/{package}/steps.py`:

```python
@step(name="{step-name}", span_kind="{span_kind}")
def my_step(input_data: InputType, param: str = "default") -> OutputType:
    ...
    return result
```

Rules:
- `from __future__ import annotations` at file top
- `TYPE_CHECKING` guard for provrag type imports
- `model_copy(update={...})` for Pydantic model updates, never mutate
- Single responsibility
- No side effects outside the step's domain

### 5. Insert into pipeline

Edit the pipeline file to call the new step at the correct position. Import from `{package}.steps`.

### 6. Write tests

Add to `tests/test_steps.py`:

```python
class TestMyStep:
    def test_basic_case(self) -> None:
        result = my_step.fn(input_data=..., param="test")
        assert result == ...

    def test_empty_input(self) -> None:
        result = my_step.fn(input_data=[], param="test")
        assert result == []
```

Use `.fn()` to bypass Prefect wrapper. Mock external dependencies.

### 7. Add dependencies

If the step needs external libraries:
```bash
uv add {library}
uv sync --extra dev
```

### 8. Verify

```bash
task check
```
