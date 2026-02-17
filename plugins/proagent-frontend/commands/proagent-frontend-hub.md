---
description: >
  Overview of all frontend engineering capabilities: component scaffolding, UI building,
  design systems, accessibility auditing, performance optimization, and code review.
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# proagent-frontend Hub

Welcome to the Provectus Frontend Engineering plugin. This hub provides access to all frontend development, design system, and UI optimization capabilities.

## Available Commands

### /proagent-frontend-run
Execute frontend engineering operations. Accepts a mode argument:

- **scaffold-component** - Generate a new UI component with TypeScript types, tests, accessibility attributes, and Storybook stories. Follows atomic design principles and the project's existing component patterns. Supports React, Vue, and Angular output.
- **build-ui** - Build a complete UI feature from a description or specification. Analyzes requirements, creates component hierarchy, implements responsive layouts, applies theming, and validates accessibility. Produces production-ready code with Tailwind CSS and framework best practices.
- **design-system** - Initialize or extend a design system with token-based architecture. Creates foundational components (Button, Card, Input, Badge, Avatar, Toggle), defines color palettes and typography scales, configures theme management (light/dark/auto), and generates documentation.
- **accessibility-audit** - Run a comprehensive WCAG 2.1 AA accessibility audit on components or pages. Checks color contrast, keyboard navigation, ARIA attributes, semantic HTML, screen reader compatibility, and focus management. Returns structured results with remediation guidance.
- **optimize-performance** - Analyze and optimize frontend performance. Measures Core Web Vitals (LCP, FID, CLS), identifies bundle size bottlenecks, recommends code splitting strategies, optimizes image loading, and configures caching. Returns actionable improvement plan with expected impact.

### /proagent-frontend-review
Review and assess frontend quality. Accepts a mode argument:

- **review components** - Audit UI components for reusability, prop design, composition patterns, TypeScript correctness, and adherence to the project's design system. Identifies anti-patterns, accessibility gaps, and improvement opportunities.
- **accessibility** - Deep accessibility review against WCAG 2.1 AA standards. Tests keyboard navigation flows, screen reader announcements, color contrast ratios, focus indicators, and ARIA usage patterns. Reports violations with criterion references and fix examples.
- **performance** - Frontend performance review covering bundle analysis, render optimization, asset loading, caching strategy, and Core Web Vitals. Identifies bottlenecks and recommends prioritized optimizations.
- **design consistency** - Review UI elements against the project's design system tokens and patterns. Checks color usage, typography scale adherence, spacing consistency, component variant usage, and responsive breakpoint implementation.

## Quick Start

1. Run `/proagent-frontend-run scaffold-component` to generate a new component with tests and accessibility
2. Run `/proagent-frontend-run build-ui` to build a complete UI feature from a description
3. Run `/proagent-frontend-run accessibility-audit` to check WCAG compliance
4. Run `/proagent-frontend-review components` to audit existing component quality
5. Run `/proagent-frontend-run design-system` to initialize or extend your design system

## Configuration

This plugin integrates with:
- **Playwright MCP** for visual regression testing and cross-browser UI validation
- **GitHub/GitLab** for component library CI/CD, PR previews, and design system versioning
- **axe-core** for automated accessibility testing in CI pipelines
- **Lighthouse** for performance auditing and Core Web Vitals monitoring

See `.mcp.json` for MCP server configuration and `hooks/hooks.json` for automated quality gates.
