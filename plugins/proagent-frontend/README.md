# proagent-frontend

Provectus Frontend Engineering plugin for Claude Code. Comprehensive toolkit for building modern web interfaces with component architecture, design systems, accessibility compliance, and performance optimization.

## Overview

proagent-frontend provides a complete frontend engineering toolkit that integrates with Claude Code to scaffold components, build UI features, manage design systems, audit accessibility, and optimize performance. It supports React, Vue, and Angular projects with Tailwind CSS, TypeScript, and Vite build systems. Quality gates enforce WCAG 2.1 AA compliance, performance budgets, and design system adherence through automated hooks.

## Installation

### Claude Code (CLI)

1. Copy the `proagent-frontend/` directory into your project's `.claude/plugins/` directory:
   ```bash
   cp -r proagent-frontend/ your-project/.claude/plugins/proagent-frontend/
   ```
2. Copy MCP server configuration to your project root:
   ```bash
   cp proagent-frontend/.mcp.json your-project/.mcp.json
   ```
3. Configure MCP credentials in your environment:
   - Set `GITHUB_PERSONAL_ACCESS_TOKEN` for GitHub integration
   - Set `GITLAB_PERSONAL_ACCESS_TOKEN` and `GITLAB_API_URL` for GitLab integration
4. Install Playwright for visual testing: `npm install -D @playwright/test`
5. Install accessibility tooling: `npm install -D @axe-core/cli`

### Claude Desktop

1. Open Claude Desktop Settings > Plugins
2. Add the plugin directory path pointing to `proagent-frontend/`
3. Configure MCP servers in Claude Desktop's MCP settings:
   - Add Playwright MCP: `npx @playwright/mcp@latest --isolated`
   - Add GitHub MCP: `npx -y @modelcontextprotocol/server-github` with `GITHUB_PERSONAL_ACCESS_TOKEN`
   - Add GitLab MCP: `npx -y @modelcontextprotocol/server-gitlab` with `GITLAB_PERSONAL_ACCESS_TOKEN`
4. Restart Claude Desktop to load the plugin

## Commands

| Command | Description |
|---------|-------------|
| `/proagent-frontend-hub` | View all available commands and quick start guide |
| `/proagent-frontend-run scaffold-component` | Generate a UI component with TypeScript types, tests, and accessibility |
| `/proagent-frontend-run build-ui` | Build a complete UI feature from a description or spec |
| `/proagent-frontend-run design-system` | Initialize or extend a token-based design system |
| `/proagent-frontend-run accessibility-audit` | Run WCAG 2.1 AA audit with structured results and remediation |
| `/proagent-frontend-run optimize-performance` | Analyze Core Web Vitals and generate optimization plan |
| `/proagent-frontend-review components` | Audit component quality, reusability, and patterns |
| `/proagent-frontend-review accessibility` | Deep WCAG review with keyboard and screen reader testing |
| `/proagent-frontend-review performance` | Bundle analysis, rendering audit, asset optimization |
| `/proagent-frontend-review design consistency` | Design token and component pattern adherence review |

## Quality Gates

The plugin includes automated quality gates via `hooks/hooks.json`:

- **Pre-commit**: Blocks commits that fail TypeScript compilation, ESLint checks, or accessibility linting rules (jsx-a11y, vuejs-accessibility)
- **Post-build**: Warns when axe-core detects WCAG violations or Lighthouse accessibility score drops below 90
- **Pre-merge**: Requires component tests to pass, zero critical accessibility violations, bundle size within budget (200KB JS gzipped), and visual regression test pass

## Supported Technologies

### Frameworks
- React 18/19 (functional components, hooks, Suspense)
- Vue 3 (Composition API, script setup)
- Angular 17+ (standalone components, signals)

### Styling
- Tailwind CSS 3/4 with custom design tokens
- CSS Modules, styled-components, CSS-in-JS
- CSS custom properties for runtime theming

### Build Tools
- Vite 5/6/7 with HMR, code splitting, and asset optimization
- PostCSS with Tailwind CSS, autoprefixer, CSS nesting
- TypeScript strict mode with path aliases

### Testing
- Vitest / Jest for unit and integration testing
- Testing Library (React, Vue, Angular) for component testing
- Playwright for E2E, visual regression, and accessibility testing
- axe-core for automated WCAG compliance testing

### Design System
- Token-based architecture (colors, typography, spacing, shadows)
- Theme management with light/dark/auto mode support
- Component library: Avatar, Badge, Button, Card, Input, Toggle
- Pre-built themes: modern-minimalist, midnight-galaxy

### Accessibility
- WCAG 2.1 AA compliance auditing
- axe-core automated checks
- Keyboard navigation and focus management testing
- Screen reader compatibility validation
- Color contrast analysis

### Performance
- Core Web Vitals monitoring (LCP, FID/INP, CLS)
- Bundle size analysis and budgeting
- Code splitting and lazy loading
- Image optimization (WebP/AVIF, responsive, lazy loading)
- Service worker caching strategies

## Architecture

The plugin is built around these components:

- **SKILL.md**: Defines the frontend assistant's core competencies across component design, design systems, accessibility, responsive design, performance optimization, web artifacts, and frontend tooling
- **Commands**: Three command files (Hub, Run, Review) that provide the user-facing interface for all frontend operations
- **Agent**: A frontend specialist subagent with expertise in React/Vue/Angular, design systems, WCAG compliance, and performance engineering
- **Hooks**: Automated quality gates that enforce TypeScript compilation, accessibility standards, and performance budgets at commit, build, and merge time
- **MCP Config**: Integration with Playwright for visual testing, GitHub for PR workflows, and GitLab for merge request gates

## Source Attribution

This plugin synthesizes patterns and practices from the following Provectus repositories:

- **Auto-Claude**: Design system architecture with React 19, Vite 7, Tailwind CSS 4, component library (Avatar, Badge, Button, Card), theme constants, useTheme hook, pre-commit configuration
- **awesome-claude-skills**: Artifacts builder (React/Tailwind/shadcn), brand guidelines, canvas design, theme factory
- **casdk-harness**: TypeScript expert and React expert agent configurations
- **claude-ui**: React 18/Vite application architecture, component patterns (ArtifactPanel, CommandPalette, SettingsModal, ModelSelector), ThemeContext (light/dark/auto), AuthContext, service worker, PWA manifest
- **proagent**: Frontend engineer role definition, component design skills, state management strategies, responsive design implementation
- **proagent-repo GUI**: Frontend validation workflow configuration
- **skills**: Algorithmic art (JavaScript Canvas), canvas design with bundled fonts, frontend design, theme factory with 10 presets (modern-minimalist, midnight-galaxy), web artifacts builder, Slack GIF creator
- **agents**: WCAG accessibility audit patterns, TDD workflow plugins

## License

MIT
