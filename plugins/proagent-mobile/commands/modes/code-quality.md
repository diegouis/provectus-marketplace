# Mode: code-quality

**Goal:** Review Expo/React Native code for quality, performance, and best practices.

**Announce:** "Starting code quality review. I'll check for common issues, performance patterns, and React Native best practices."

### Process

1. **Scope the review:**
   - Parse `$ARGUMENTS` for file paths, component names, or a directory
   - If not specified, ask: "Which files or components should I review?"

2. **Read target files** and check for:

   **React Native patterns:**
   - Avoid inline styles in render (use `StyleSheet.create` or NativeWind classes)
   - `FlatList` / `SectionList` used for long lists (not `ScrollView` + `map`)
   - `KeyboardAvoidingView` used for forms on iOS
   - `Platform.select()` for platform-specific code

   **Performance:**
   - `useCallback` on event handlers passed to list items
   - `React.memo` on pure components
   - `useMemo` for expensive derivations
   - Images use appropriate formats (WebP for Android/web)

   **Expo specifics:**
   - `expo-constants` for config values (not hardcoded)
   - `expo-secure-store` for sensitive data (not `AsyncStorage`)
   - `expo-router` `Link` / `router.push` used for navigation

3. **Generate review report:**
   ```
   ## Code Quality Review

   | Severity | File | Line | Issue | Fix |
   |---|---|---|---|---|

   ### Summary
   - Critical: [count]
   - High: [count]
   - Medium: [count]
   - Low: [count]
   ```
