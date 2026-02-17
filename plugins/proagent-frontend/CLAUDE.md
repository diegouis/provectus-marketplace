# proagent-frontend

This is the Provectus Frontend Engineering plugin for Claude Code. It provides comprehensive capabilities for building modern web interfaces with React, Vue, Angular, Tailwind CSS, design systems, accessibility compliance, and performance optimization.

## Plugin Structure

```
proagent-frontend/
  .claude-plugin/plugin.json          - Plugin metadata and configuration
  skills/frontend-assistant/SKILL.md  - Core skill: component design, design systems, accessibility, responsive design, performance
  commands/
    proagent-frontend-hub.md           - Plugin hub with command overview and quick start
    proagent-frontend-run.md           - Execute: scaffold-component, build-ui, design-system, accessibility-audit, optimize-performance
    proagent-frontend-review.md        - Review: components, accessibility, performance, design consistency
  agents/frontend-specialist.md        - Frontend specialist subagent for UI engineering
  hooks/hooks.json                     - Pre-commit validation, post-build accessibility, pre-merge UI gates
  mcp.json                             - MCP server configs: Playwright, GitHub, GitLab
```

## Commands

- `/proagent-frontend-hub` - View all available frontend commands and quick start guide
- `/proagent-frontend-run scaffold-component` - Generate a UI component with types, tests, and accessibility
- `/proagent-frontend-run build-ui` - Build a complete UI feature from a description
- `/proagent-frontend-run design-system` - Initialize or extend a design system with tokens and components
- `/proagent-frontend-run accessibility-audit` - Run WCAG 2.1 AA accessibility audit with remediation
- `/proagent-frontend-run optimize-performance` - Analyze Core Web Vitals and optimize bundle/rendering
- `/proagent-frontend-review components` - Audit component quality, reusability, and patterns
- `/proagent-frontend-review accessibility` - Deep WCAG compliance review with keyboard and screen reader testing
- `/proagent-frontend-review performance` - Bundle analysis, rendering audit, and asset optimization
- `/proagent-frontend-review design consistency` - Design token and component pattern adherence check

## Quality Gates

The hooks configuration enforces:
1. **Pre-commit**: TypeScript type checking, ESLint with framework plugins, accessibility linting on staged files
2. **Post-build**: axe-core WCAG audit and Lighthouse accessibility scoring on built output
3. **Pre-merge**: Component tests, accessibility gate (zero critical violations), bundle size budget, visual regression

## MCP Integrations

- **Playwright**: Cross-browser UI testing, visual regression, responsive layout validation, accessibility auditing of rendered pages
- **GitHub**: Component library PRs with visual diffs, design system versioning, frontend CI/CD
- **GitLab**: Merge request UI gates, pipeline monitoring, component package publishing

## Conventions

- All components use TypeScript strict mode with comprehensive prop interfaces
- Styling uses Tailwind CSS utility classes with design tokens for theme values
- Accessibility is validated against WCAG 2.1 AA with axe-core in CI pipelines
- Performance budgets: LCP < 2.5s, FID < 100ms, CLS < 0.1, initial JS < 200KB gzipped
- Components follow atomic design: atoms > molecules > organisms > templates > pages
- Theme management supports light/dark/auto modes with system preference detection
- Tests use Testing Library with accessible queries (getByRole, getByLabelText)
