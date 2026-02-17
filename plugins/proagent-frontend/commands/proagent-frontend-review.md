# proagent-frontend Review

Review and assess frontend code quality, accessibility, performance, and design system adherence.

## Variables

mode: $1 (one of: "components", "accessibility", "performance", "design consistency")
target: $2 (optional - specific file, directory, component, or URL to review)

## Instructions

Read the `mode` variable and execute the corresponding review workflow below.

---

### Mode: review components

Audit UI components for quality, reusability, and best practices.

1. **Discover Components**
   - Locate all component files in the project (*.tsx, *.jsx, *.vue, *.component.ts)
   - If `target` is provided, scope the review to that specific file or directory
   - Identify the framework (React, Vue, Angular) and styling approach in use
   - Detect design system components vs. application-specific components

2. **Analyze Component Quality**
   - **Props Design**: Check for well-typed interfaces, consistent naming (onAction for handlers, isState for booleans), sensible defaults, and JSDoc documentation
   - **Composition Patterns**: Verify proper use of children/slots, compound component patterns, render props, and custom hooks for shared logic
   - **Separation of Concerns**: Flag components mixing business logic with presentation. Container components should handle data; presentation components should handle rendering
   - **State Management**: Check for state lifted to the appropriate level, avoid prop drilling deeper than 3 levels, proper use of context for shared state (derived from proagent/roles/frontend-engineer/skills/state-management.md)
   - **Error Handling**: Verify error boundaries for component trees, fallback UI for loading/error states, graceful degradation
   - **Component Size**: Flag components exceeding 300 lines; recommend splitting into sub-components
   - Anti-patterns to detect:
     - Inline function definitions in JSX props causing unnecessary re-renders
     - Direct DOM manipulation instead of declarative rendering
     - Hardcoded colors/sizes instead of design token references
     - Missing key props on list items
     - Using index as key for dynamic lists
     - Prop type any or missing TypeScript types

3. **Evaluate Reusability**
   - Check if components are framework-agnostic where possible (logic in hooks, rendering in components)
   - Verify components accept customization through props, not internal conditionals
   - Assess composability: can the component be used in different contexts without modification?
   - Check for proper re-export through barrel files (index.ts)

4. **Report**
   Provide a structured review:
   - Component health score (1-10) based on type safety, accessibility, reusability, and test coverage
   - List of issues with severity (critical, warning, suggestion) and affected file paths
   - Specific code examples showing the current pattern and recommended improvement
   - Highlighted components that serve as good examples to follow

---

### Mode: accessibility

Deep accessibility review against WCAG 2.1 AA standards.

1. **Scope Assessment**
   - If `target` is a URL, use Playwright MCP to load the page and navigate through the UI
   - If `target` is a file path, analyze the component source code for accessibility patterns
   - If no target, audit all component files and page templates

2. **Keyboard Navigation Testing**
   - Trace tab order through all interactive elements and verify logical sequence
   - Check that all custom interactive elements (dropdowns, modals, tabs, accordions) support full keyboard operation
   - Verify Enter activates buttons/links, Space toggles checkboxes/switches, Escape closes modals/popups
   - Test arrow key navigation in menus, tabs, and radio groups
   - Verify focus trapping in modals and dialogs (focus should not escape)
   - Check that focus returns to the trigger element when modals/popups close
   - Verify skip navigation link is present and functional (derived from claude-ui/src/components/CommandPalette.jsx keyboard handling)

3. **Screen Reader Compatibility**
   - Verify all images have descriptive alt text (not "image", not empty for decorative images used with role="presentation")
   - Check heading hierarchy: single h1, no skipped levels (h1 > h2 > h3, not h1 > h3)
   - Verify landmark regions: main, nav, header, footer, aside are used correctly
   - Check that dynamic content updates use aria-live regions (polite for non-urgent, assertive for urgent)
   - Verify form inputs have associated labels (htmlFor/id or wrapping label element)
   - Check that error messages are programmatically associated with their inputs via aria-describedby
   - Verify custom widgets have proper ARIA roles: dialog, tab, tabpanel, menu, menuitem, combobox, listbox

4. **Visual Accessibility**
   - Test all text/background color combinations for WCAG AA contrast (4.5:1 normal, 3:1 large)
   - Verify focus indicators are visible and have sufficient contrast (3:1 against adjacent colors)
   - Check that information is not conveyed by color alone (icons, patterns, or text labels accompany color)
   - Verify content is readable at 200% zoom without horizontal scrolling
   - Check that animations respect prefers-reduced-motion media query

5. **Report**
   Provide an accessibility assessment:
   - Overall compliance rating: Compliant, Partially Compliant, Non-Compliant
   - Violations grouped by WCAG principle (Perceivable, Operable, Understandable, Robust)
   - Each violation includes: WCAG criterion, severity, affected element, description, and code fix
   - Manual testing checklist for items requiring human verification
   - Estimated remediation effort per violation category

---

### Mode: performance

Frontend performance review with actionable optimization recommendations.

1. **Build Analysis**
   - Analyze the build configuration (Vite, webpack, or framework-specific)
   - Measure output bundle sizes (entry chunks, vendor chunks, async chunks)
   - Detect tree-shaking effectiveness: unused exports, side-effect-free packages
   - Check for duplicate dependencies in the bundle
   - Verify source maps are configured correctly (production: hidden-source-map, development: eval-source-map)

2. **Rendering Performance**
   - Identify components that re-render excessively due to:
     - Parent re-renders without React.memo/shouldComponentUpdate
     - Inline objects or functions passed as props
     - Context values that change on every render
     - Missing or incorrect memoization (useMemo, useCallback)
   - Check for expensive DOM operations: layout thrashing, forced synchronous layouts
   - Verify virtual scrolling for large lists (> 100 items)
   - Assess code splitting: route-level splitting, component-level lazy loading

3. **Asset Loading**
   - Image audit: format optimization (WebP/AVIF), responsive srcset, lazy loading
   - Font loading: font-display strategy, preload for critical fonts, number of font files
   - CSS delivery: critical CSS extraction, unused CSS removal, print stylesheet separation
   - JavaScript loading: async/defer attributes, module/nomodule for legacy support
   - Third-party scripts: assess impact of analytics, chat widgets, ad scripts

4. **Caching and Network**
   - Review service worker configuration for offline support and caching strategy
   - Check HTTP cache headers for static assets (immutable for hashed files)
   - Verify CDN configuration for asset distribution
   - Assess API request optimization: batching, debouncing, request deduplication

5. **Report**
   Provide a performance assessment:
   - Current metrics summary (bundle size, estimated load time, identified bottlenecks)
   - Top 5 optimizations ranked by impact with implementation difficulty
   - Code examples for each recommended optimization
   - Expected improvement estimates for each recommendation
   - Comparison against performance budget targets

---

### Mode: design consistency

Review UI elements against the project's design system and visual patterns.

1. **Design Token Audit**
   - Extract all color values used in the codebase (hex, rgb, hsl, Tailwind classes, CSS variables)
   - Compare against the design system color palette; flag any values not in the token set
   - Check typography usage: font sizes, weights, families against the type scale
   - Verify spacing values align with the spacing scale (no arbitrary pixel values)
   - Check shadow, border-radius, and z-index usage against defined tokens

2. **Component Pattern Review**
   - Verify all buttons use the design system Button component (not custom styled divs or anchors)
   - Check form inputs use the design system Input component with proper label/error patterns
   - Verify card layouts use consistent padding, shadow, and border-radius from the design system
   - Flag one-off styled elements that should use design system components
   - Check icon usage: consistent icon library (Lucide, Heroicons, etc.), consistent sizing

3. **Layout Consistency**
   - Verify page layouts follow established grid patterns
   - Check that responsive breakpoints are consistent across pages
   - Verify navigation patterns are consistent (header, sidebar, breadcrumbs)
   - Check that modals, drawers, and popups follow a consistent presentation pattern
   - Verify loading and empty state patterns are consistent across the application

4. **Theme Compliance**
   - Check that light and dark themes are fully implemented (no hardcoded colors that break in dark mode)
   - Verify theme transitions are smooth (no flash of incorrect theme on load)
   - Check that all component variants work correctly in both themes
   - Verify theme persistence across page reloads (derived from claude-ui/src/contexts/ThemeContext.jsx)

5. **Report**
   Provide a design consistency assessment:
   - Design system adoption score (percentage of UI using design tokens and components)
   - List of design token violations with file paths and specific values
   - Component usage audit: which design system components are used vs. custom implementations
   - Inconsistency inventory with visual examples (current vs. expected)
   - Prioritized fixes to improve design system adoption
