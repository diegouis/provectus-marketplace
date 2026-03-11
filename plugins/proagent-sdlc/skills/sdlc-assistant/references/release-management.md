# Release Management

## Release Workflow

Combines changelog generation, semantic versioning with conventional commits, and verification workflows for acceptance criteria.

**Release workflow:**
1. Verify all acceptance criteria are met
2. Generate changelog from conventional commits since last release
3. Determine version bump (major/minor/patch) from commit types
4. Update version in project manifests
5. Create release branch or tag
6. Run release readiness checks (tests pass, no blocking issues, docs current)
7. Create PR or release draft

**Verification process:**
- Identify target specification
- Confirm all tasks are complete
- Verify each acceptance criterion against implementation
- Mark spec as Completed
- Review product context docs for needed updates

## Changelog Generation

Automated changelog generation follows the pattern from awesome-claude-skills (`changelog-generator/SKILL.md`):

1. Parse conventional commits since last release tag
2. Group by type: Features, Bug Fixes, Performance, Breaking Changes, Documentation, Chores
3. Include commit hash, scope, and description
4. Highlight breaking changes at the top with migration notes
5. Output as CHANGELOG.md entry with release date and version
