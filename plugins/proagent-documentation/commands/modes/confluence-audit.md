# Audit Confluence Pages

**Input**: Confluence space key or page URL
**Output**: Audit report with page health status

## Steps

1. **Enumerate pages** — list all pages in the target space or under parent
2. **Check staleness** — identify pages not updated in 90+ days
3. **Validate links** — check internal Confluence links and external URLs
4. **Detect orphans** — find pages not linked from any parent or index
5. **Check labels** — ensure consistent labeling across pages
6. **Identify duplicates** — find pages with similar titles or overlapping content
7. **Report findings** — produce audit report with remediation suggestions

## Health Status

- **Healthy**: Updated within 90 days, all links valid, properly labeled
- **Stale**: Not updated in 90-180 days, may contain outdated information
- **Critical**: Not updated in 180+ days, broken links, or orphaned
