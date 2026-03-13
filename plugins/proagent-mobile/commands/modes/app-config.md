# Mode: app-config

**Goal:** Review and audit app.json, eas.json, and app.config.js/ts for correctness and completeness.

> **Adequacy Gate**: Before proceeding, verify:
> 1. `app.json` or `app.config.js/ts` exists in the project root
> 2. `eas.json` exists if EAS Build is used
> If any check fails, inform the user and collect missing prerequisites before continuing.

**Announce:** "Starting app configuration review. I'll audit your Expo and EAS configuration files."

### Process

1. **Read configuration files:**
   - Look for: `app.json`, `eas.json`, `app.config.js`, `app.config.ts`
   - If not found in the root, ask the user for the path

2. **Audit app.json / app.config:**
   - `expo.name` and `expo.slug` — consistent with store listings
   - `expo.version` — follows semver
   - `expo.ios.bundleIdentifier` — matches App Store Connect
   - `expo.android.package` — matches Google Play Console
   - `expo.ios.buildNumber` and `expo.android.versionCode` — configured for auto-increment or manual
   - `expo.plugins` — all required native plugins declared
   - `expo.assets` and `expo.splash` — referenced files exist
   - `expo.extra` — no secrets stored here (use EAS Secrets for sensitive values)

3. **Audit eas.json:**
   - `build.development.developmentClient: true` is set for dev builds
   - `build.production.autoIncrement` is configured
   - `submit` profiles are present for production releases
   - No hardcoded credentials (use EAS credentials service)
   - `cli.appVersionSource` is set to `"remote"` if using EAS-managed versioning

4. **Generate review report:**
   ```
   ## App Configuration Review

   ### app.json
   | Field | Value | Status | Notes |
   |---|---|---|---|

   ### eas.json
   | Profile | Settings | Status | Notes |
   |---|---|---|---|

   ### Issues Found
   | Severity | File | Field | Issue | Fix |
   |---|---|---|---|---|

   ### Recommendations
   [Ordered list of improvements]
   ```
