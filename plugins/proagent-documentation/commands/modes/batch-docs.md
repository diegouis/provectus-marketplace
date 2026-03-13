# Batch Process Multiple Repositories

**Input**: List of repository URLs or organization/group name
**Output**: Documentation index and individual repo docs

## Steps

1. **Enumerate repos** — list repos from org/group or parse input list
2. **Run analysis** — analyze each repo (parallel where possible)
3. **Generate docs** — produce selected doc types for each repo
4. **Build index** — create a master index page linking all repo docs
5. **Publish index** — optionally publish to Confluence as a documentation hub
6. **Report results** — summary table of repos processed, docs generated, pages published

## Options

- `--org <github-org|gitlab-group>` — process all repos in organization
- `--repos <url1,url2,...>` — comma-separated repo URLs
- `--type <readme|architecture|all>` — doc type to generate for each repo
- `--confluence-space <SPACE_KEY>` — publish all docs to this Confluence space
