---
description: >
  Execute frontend engineering operations: scaffold-component, build-ui, design-system,
  accessibility-audit, optimize-performance.
argument-hint: "<mode> [target] [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# proagent-frontend Run

Execute frontend engineering operations based on the specified mode.

## Variables

mode: $1
target: $2 (optional - component name, file path, URL, or description depending on mode)
options: $3 (optional - additional configuration such as framework, style system, or audit scope)

## Instructions

Read the `mode` variable and execute the corresponding workflow below.

---

### Mode: scaffold-component

Generate a new UI component with full project integration.

1. **Analyze Project Context**
   - Detect the frontend framework in use (React, Vue, Angular) from package.json dependencies
   - Identify the styling approach (Tailwind CSS, CSS Modules, styled-components, plain CSS) from config files
   - Locate the existing component directory and naming conventions
   - Check for an existing design system with theme tokens and component patterns
   - Detect test framework (Vitest, Jest, Testing Library) from configuration

2. **Generate Component Structure**
   - Create the component directory following project conventions:
     ```
     ComponentName/
       ComponentName.tsx       - Main component with TypeScript interface
       ComponentName.test.tsx  - Unit and interaction tests
       ComponentName.stories.tsx - Storybook stories (if Storybook is configured)
       index.ts               - Public re-export
     ```
   - Define TypeScript props interface with JSDoc descriptions for each prop
   - Implement variant and size props consistent with existing design system components (derived from Auto-Claude/.design-system/src/components/Button.tsx pattern)
   - Add forwardRef support for DOM element access
   - Include default prop values and prop validation

3. **Apply Accessibility Standards**
   - Add semantic HTML elements (button, nav, dialog, etc.) instead of generic divs
   - Include ARIA attributes: aria-label, aria-describedby, role as appropriate
   - Implement keyboard interaction handlers (onKeyDown for Enter/Space/Escape)
   - Set proper tabIndex and focus management
   - Ensure color contrast compliance in all variants

4. **Generate Tests**
   - Render tests: component mounts without errors, renders expected content
   - Interaction tests: click handlers fire, keyboard navigation works, focus management
   - Accessibility tests: axe-core integration test for zero violations
   - Variant tests: each variant/size combination renders correctly
   - Use Testing Library queries: getByRole, getByLabelText (accessible queries first)

5. **Register Component**
   - Add export to the nearest barrel file (index.ts)
   - If a design system index exists, register the component there
   - Output the component file paths and a usage example

---

### Mode: build-ui

Build a complete UI feature from a description or specification.

1. **Analyze Requirements**
   - If `target` is a description string, extract UI requirements: layout, interactions, data display, navigation
   - If `target` is a spec file path, read and parse acceptance criteria, wireframes, and user flows
   - Identify required components, data models, and API integration points
   - Map requirements to a component hierarchy (page > sections > components)

2. **Design Component Architecture**
   - Decompose the UI into atomic design layers:
     - Atoms: buttons, inputs, labels, icons
     - Molecules: form fields, search bars, menu items
     - Organisms: navigation bars, forms, card grids, modals
     - Templates: page layouts with content slots
   - Define data flow: props drilling vs. context vs. global state
   - Plan responsive behavior for each breakpoint (mobile, tablet, desktop)

3. **Implement Components**
   - Create each component following the scaffold-component workflow
   - Apply Tailwind CSS utility classes for styling (or the project's styling system)
   - Implement responsive layouts with CSS Grid and Flexbox, mobile-first breakpoints
   - Add loading states, error states, and empty states for data-dependent components
   - Wire up event handlers, form validation, and user interactions
   - Connect to API endpoints or mock data as appropriate

4. **Apply Design System**
   - Use existing design tokens for colors, typography, spacing, shadows
   - Apply consistent component variants (primary, secondary, outline, ghost)
   - Implement theme-aware styles using CSS custom properties or Tailwind dark: variant
   - Follow brand guidelines for visual identity (derived from awesome-claude-skills/brand-guidelines)

5. **Validate and Report**
   - Run TypeScript compilation: `npx tsc --noEmit`
   - Execute component tests to verify correctness
   - Run accessibility audit on generated components
   - Output file manifest with component hierarchy diagram
   - Provide usage instructions and integration notes

---

### Mode: design-system

Initialize or extend a design system with token-based architecture.

1. **Assess Current State**
   - Check for existing design system directory, theme tokens, and component library
   - Identify the current tech stack: React version, Tailwind CSS version, build tool
   - Catalog existing components and their prop interfaces
   - Detect inconsistencies in current styling patterns

2. **Define Design Tokens**
   - Create or extend theme constants file with (derived from Auto-Claude/.design-system/src/theme/constants.ts):
     - Color palette: primary, secondary, accent, neutral, semantic (success, warning, error, info)
     - Typography scale: font families (heading, body, mono), sizes (xs through 4xl), weights, line heights
     - Spacing scale: 0, 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24 (in rem units)
     - Shadow system: sm, md, lg, xl for elevation hierarchy
     - Border radius: none, sm, md, lg, full
     - Breakpoints: sm (640px), md (768px), lg (1024px), xl (1280px), 2xl (1536px)

3. **Implement Theme Management**
   - Create a theme provider with React Context (derived from Auto-Claude/.design-system/src/theme/useTheme.ts and claude-ui/src/contexts/ThemeContext.jsx):
     - Support light, dark, and auto (system preference) modes
     - Persist theme selection to localStorage
     - Listen to prefers-color-scheme media query changes
     - Expose useTheme hook for components to consume
   - Generate CSS custom properties from design tokens
   - Configure Tailwind CSS to use custom theme tokens

4. **Build Foundational Components**
   - Generate core component library (derived from Auto-Claude/.design-system/src/components/):
     - **Avatar**: image with fallback initials, sizes (sm, md, lg), status indicator
     - **Badge**: variants (default, success, warning, error), sizes, pill/rounded shapes
     - **Button**: variants (primary, secondary, outline, ghost, destructive), sizes, loading state, icon support
     - **Card**: header/body/footer sections, padding variants, hover effects
     - **Input**: text/email/password/number types, label, helper text, error state, prefix/suffix slots
     - **Toggle**: on/off switch with label, disabled state, size variants
   - Each component gets full TypeScript types, tests, and accessibility attributes

5. **Apply Pre-Built Themes** (optional)
   - Offer theme presets (derived from skills/theme-factory):
     - Modern Minimalist: clean lines, neutral palette, Inter font, generous whitespace
     - Midnight Galaxy: dark palette, accent gradients, space-inspired
     - Custom: user-defined token values
   - Generate preview page showing all components with the selected theme

6. **Output**
   - Design system directory with all token files, components, and theme provider
   - Documentation: token reference, component API docs, usage examples
   - Vite config for the design system preview app (derived from Auto-Claude/.design-system/vite.config.ts)

---

### Mode: accessibility-audit

Run a comprehensive WCAG 2.1 AA accessibility audit.

1. **Scope Discovery**
   - If `target` is a file path, audit that specific component or page
   - If `target` is a URL, use Playwright MCP to load the page and audit the rendered DOM
   - If no target, scan all component files in the project for accessibility issues

2. **Automated Checks** (derived from agents/plugins/accessibility-compliance/skills/wcag-audit-patterns)
   - **Perceivable (WCAG 1.x)**:
     - Images have meaningful alt text (1.1.1 Non-text Content)
     - Video/audio have captions or transcripts (1.2.x Time-based Media)
     - Color contrast meets minimums: 4.5:1 normal text, 3:1 large text (1.4.3 Contrast)
     - Text can be resized to 200% without loss of content (1.4.4 Resize Text)
     - Content does not rely solely on color to convey meaning (1.4.1 Use of Color)
   - **Operable (WCAG 2.x)**:
     - All interactive elements are keyboard accessible (2.1.1 Keyboard)
     - No keyboard traps exist (2.1.2 No Keyboard Trap)
     - Focus order follows logical reading sequence (2.4.3 Focus Order)
     - Focus indicators are visible on all interactive elements (2.4.7 Focus Visible)
     - Skip navigation link is present (2.4.1 Bypass Blocks)
     - Page titles are descriptive (2.4.2 Page Titled)
     - Link purpose is clear from text or context (2.4.4 Link Purpose)
   - **Understandable (WCAG 3.x)**:
     - Page language is declared via lang attribute (3.1.1 Language of Page)
     - Form inputs have associated labels (3.3.2 Labels or Instructions)
     - Error messages identify the field and describe the error (3.3.1 Error Identification)
     - Required fields are programmatically indicated (3.3.2)
   - **Robust (WCAG 4.x)**:
     - Valid HTML structure without parsing errors (4.1.1 Parsing)
     - Custom components have proper ARIA roles and states (4.1.2 Name, Role, Value)
     - Dynamic content changes are announced via aria-live regions (4.1.3 Status Messages)

3. **Manual Check Prompts**
   - Generate a checklist of items requiring human verification:
     - Screen reader announcement accuracy for custom widgets
     - Logical reading order for complex layouts
     - Touch target sizes for mobile (minimum 44x44 CSS pixels)
     - Motion/animation respects prefers-reduced-motion

4. **Report**
   Return results as structured JSON:
   ```json
   {
     "summary": {
       "total_checks": 0,
       "violations": 0,
       "warnings": 0,
       "passes": 0
     },
     "violations": [
       {
         "criterion": "WCAG 2.1 1.4.3",
         "severity": "critical",
         "element": "selector or component name",
         "description": "issue description",
         "remediation": "specific fix instructions with code example"
       }
     ],
     "manual_checks": ["list of items for human review"]
   }
   ```

---

### Mode: optimize-performance

Analyze and optimize frontend performance.

1. **Bundle Analysis**
   - Run `npx vite-bundle-visualizer` or `npx webpack-bundle-analyzer` to map bundle composition
   - Identify the largest dependencies by size
   - Detect duplicate packages in the dependency tree
   - Calculate total bundle size (gzipped and uncompressed)
   - Compare against performance budget (target: < 200KB initial JS gzipped)

2. **Core Web Vitals Assessment**
   - If `target` is a URL, use Playwright MCP to load the page and measure:
     - **LCP** (Largest Contentful Paint): target < 2.5s
     - **FID** (First Input Delay) / **INP** (Interaction to Next Paint): target < 100ms / 200ms
     - **CLS** (Cumulative Layout Shift): target < 0.1
     - **TTFB** (Time to First Byte): target < 800ms
     - **FCP** (First Contentful Paint): target < 1.8s
   - If no URL, analyze source code for performance anti-patterns

3. **Rendering Optimization Analysis**
   - Detect unnecessary re-renders: components missing React.memo, inline object/function props
   - Identify missing useMemo/useCallback for expensive computations
   - Check for proper key usage in list rendering
   - Detect state updates that trigger cascading re-renders
   - Recommend component splitting boundaries for React.lazy/Suspense

4. **Asset Optimization**
   - Audit images: format (WebP/AVIF recommended), sizing, lazy loading below fold
   - Check font loading strategy: font-display, preload, subsetting
   - Verify CSS delivery: critical CSS inlined, non-critical deferred
   - Assess caching headers and service worker strategy (derived from claude-ui/public/service-worker.js)

5. **Generate Optimization Plan**
   Return a prioritized improvement plan:
   ```json
   {
     "current_metrics": {
       "bundle_size_gzip_kb": 0,
       "lcp_ms": 0,
       "fid_ms": 0,
       "cls": 0
     },
     "optimizations": [
       {
         "priority": 1,
         "category": "bundle-size|rendering|assets|caching",
         "description": "what to optimize",
         "implementation": "specific steps with code",
         "expected_impact": "estimated improvement"
       }
     ]
   }
   ```

## Error Handling

- If a command returns a non-zero exit code, capture stderr and report the specific failure
- Timeout long-running operations after 5 minutes
- If TypeScript compilation fails, report errors with file paths and line numbers
- For accessibility audits, always report partial results if the audit cannot complete fully
- For performance analysis, note which metrics could not be measured and why
