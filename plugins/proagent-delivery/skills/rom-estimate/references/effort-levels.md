# Effort Level Reference Guide

Detailed sizing guide with complexity signals and domain-specific examples.

## XS — Extra Small (0.5-1 day)

**Complexity:** Trivial. Single config change, one file, no business logic.

| Signal | Example |
|--------|---------|
| Config change | Add environment variable, update .env |
| Access provisioning | Grant IAM role, add user to group |
| Single utility | Helper function, format converter |
| Documentation | Update README, add API doc entry |
| Library install | Add npm package, pip install |

**Red flags (should be S or higher):**
- Requires testing beyond a quick manual check
- Touches more than 2 files
- Needs code review from a specialist

---

## S — Small (1-3 days)

**Complexity:** Well-understood pattern. Single responsibility. Known solution.

| Signal | Example |
|--------|---------|
| CRUD endpoint | GET/POST/PUT/DELETE for one resource |
| Basic UI | Simple form, list view, modal dialog |
| Auth setup | Configure OAuth provider, JWT middleware |
| Data model | Single table/collection schema |
| Monitoring | Log group, basic alarm, metric filter |
| Notification | Slack webhook, email template |

**Red flags (should be M or higher):**
- Multiple resources or relationships
- Custom validation logic
- Retry/error handling needed
- Pagination or search

---

## M — Medium (3-8 days)

**Complexity:** Multiple components. Business logic. Error handling. Integration.

| Signal | Example |
|--------|---------|
| Complex endpoint | Multi-step business logic, validation, error handling |
| Workflow | Multi-step form wizard, approval flow |
| Webhook handler | Receive, validate, retry, idempotency |
| Search | Full-text search, filters, pagination |
| Business rules | Validation engine, scoring criteria |
| Dashboard | Data aggregation, charts, filters |
| Data connector | Single-source ETL with quality checks |
| Test suite | Unit + integration tests for a module |

**Red flags (should be L or higher):**
- Touches 3+ services
- Requires transaction safety
- Performance-critical path
- Compliance implications

---

## L — Large (8-15 days)

**Complexity:** Multi-service. System-level concern. Significant testing.

| Signal | Example |
|--------|---------|
| Complex integration | GDS, payment gateway, multi-API orchestration |
| CI/CD pipeline | Multi-stage, feature flags, rollback strategy |
| IaC | Terraform modules for full environment |
| RBAC system | Permission model + middleware + admin UI |
| Data pipeline | Multi-source ETL with quality + lineage |
| Matching engine | Scoring algorithms, tuning interface |
| Onboarding wizard | Multi-step with validation, privacy, data checks |
| E2E test suite | Cross-service tests, security tests, perf tests |

**Red flags (should be XL):**
- Novel technology with no team experience
- Cross-account or cross-region scope
- AI/ML model training or fine-tuning
- Multiple XL-level subsystems combined

---

## XL — Extra Large (15-20+ days)

**Complexity:** Architecture-level. Novel technology. High uncertainty.

| Signal | Example |
|--------|---------|
| AI agent | LangGraph state machine, multi-tool orchestration |
| Evaluation framework | Metrics pipeline, datasets, baselines, A/B |
| Decision engine | Multi-use-case trees, manual tuning, R/P/E |
| RAG system | Embeddings, vector store, metadata extraction, semantic search |
| Text-to-SQL | Natural language query pipeline with scoring |
| Cloud migration | Cross-account move, data migration, validation |
| Prompt management | Registry, versioning, guardrails, logging |
| ML lifecycle | Experiment tracking, back-testing, model registry |
| Data platform | Multi-source centralization, quality, lineage, compliance |

**When to go beyond 20 days:**
- Multiple XL concerns combined (e.g., RAG + agent + evaluation)
- Regulatory audit requirements (SOC 2 certification process)
- Multi-region deployment from scratch

---

## Duration Calibration

| Level | Opt | Pess | P50 | Typical range |
|-------|-----|------|-----|---------------|
| XS | 0.5 | 1 | 0.75 | Half day to one day |
| S | 1 | 3 | 2 | One to three days |
| M | 3 | 8 | 5.5 | Three days to a week+ |
| L | 8 | 15 | 11.5 | One to three weeks |
| XL | 15 | 20+ | 17.5+ | Three to four+ weeks |

**Adjust within range based on:**
- Team familiarity with the technology
- Clarity of requirements (vague → push toward pessimistic)
- External dependencies (API specs TBD → push toward pessimistic)
- Compliance requirements (regulated → push toward pessimistic)
- Reuse potential (existing patterns → push toward optimistic)
