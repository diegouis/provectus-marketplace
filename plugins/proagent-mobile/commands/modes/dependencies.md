# Mode: dependencies

**Goal:** Audit dependency health — compatibility, outdated packages, and version conflicts.

**Announce:** "Starting dependency health check. I'll audit your package.json and check Expo SDK compatibility."

### Process

1. **Read package.json** and extract:
   - Current Expo SDK version
   - All `expo-*` package versions
   - React and React Native versions
   - Key third-party dependencies

2. **Check compatibility:**
   - Run: `npx expo install --check` to identify incompatible package versions
   - Verify React Native version matches the Expo SDK requirement
   - Check for known peer dependency conflicts

3. **Run Expo health checks:**
   - Run: `npx expo-doctor` for Expo-specific diagnostics
   - Flag packages that are significantly behind their compatible version

4. **Generate report:**
   ```
   ## Dependency Health Report

   Expo SDK: [version]
   React Native: [version]

   ### Incompatible Packages
   | Package | Installed | Compatible | Fix |
   |---|---|---|---|

   ### Outdated Packages
   | Package | Installed | Latest | Notes |
   |---|---|---|---|

   ### Recommended Actions
   [Ordered list of fixes, most critical first]
   ```
