## Business Analytics

### KPI Dashboard Design

When designing KPI dashboards, follow these principles (detailed in `agents/plugins/business-analytics/skills/kpi-dashboard-design/SKILL.md` — load only when working on dashboard tasks):

1. **Define metric hierarchy** - Separate leading indicators (pipeline velocity, conversion rates) from lagging indicators (revenue, churn)
2. **Choose the right visualization** - Line charts for trends, bar charts for comparisons, scorecards for KPIs, heatmaps for correlations
3. **Design for the audience** - Executive dashboards show high-level summaries; operational dashboards show drill-down detail
4. **Set alerting thresholds** - Define green/yellow/red ranges for each KPI based on business targets
5. **Include time comparisons** - Show period-over-period (WoW, MoM, YoY) changes alongside absolute values

### Data Storytelling

When presenting data insights, follow these patterns (detailed in `agents/plugins/business-analytics/skills/data-storytelling/SKILL.md` — load only when working on storytelling tasks):

1. **Context** - Why does this analysis matter? What question are we answering?
2. **Key finding** - Lead with the most important insight, supported by data
3. **Supporting evidence** - Show trends, comparisons, and statistical significance
4. **Implications** - What should the audience do differently based on this data?
5. **Next steps** - Recommend concrete actions with expected impact

## Bioinformatics Data Pipelines

### Nextflow Pipeline Development

For genomics and life-sciences pipelines (detailed in `provectus-marketplace/testing/knowledge-work-plugins/bio-research/skills/nextflow-development/SKILL.md` — do NOT load unless the user is working on Nextflow pipelines):

- Use Nextflow DSL2 for modular, reusable bioinformatics workflows
- Define processes with input/output channels for parallel execution
- Configure resource requirements (cpus, memory, time) per process
- Use containers (Docker/Singularity) for reproducible environments
- Implement resume capability for fault-tolerant long-running pipelines

### Instrument Data to Allotrope Conversion

For lab instrument data standardization (detailed in `provectus-marketplace/testing/knowledge-work-plugins/bio-research/skills/instrument-data-to-allotrope/SKILL.md` — do NOT load unless the user is working on Allotrope conversion):

- Convert vendor-specific instrument output to Allotrope Simple Model (ASM) format
- Map instrument metadata fields to Allotrope ontology terms
- Validate converted data against ASM JSON schemas
- Support common instrument types (plate readers, chromatography, spectroscopy)

## Analytics Infrastructure

Reference scripts in `proagent-repo/infrastructure/analytics/` for internal analytics patterns (do NOT load unless the user is working on analytics infrastructure):

- **tracker.py** - Usage event tracking with structured event schema, batched writes, and async submission
- **reporter.py** - KPI report generation with scheduled delivery, aggregation windows, and Slack integration
- **queries.py** - Reusable SQL query library for analytics aggregations, funnel analysis, and cohort retention

## Excel Spreadsheet Operations

Reference `skills/skills/xlsx/SKILL.md` for Excel file handling (do NOT load unless the user is working on spreadsheets):

- Read and parse .xlsx files with multi-sheet support
- Write structured data to Excel with formatting, formulas, and named ranges
- Transform CSV/database exports into formatted Excel reports
- Handle large spreadsheets with streaming reads for memory efficiency
