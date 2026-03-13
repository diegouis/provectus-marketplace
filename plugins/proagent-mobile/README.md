# proagent-mobile

> Mobile app development with Expo and React Native — 10 skills covering UI, EAS builds, deployment, data fetching, CI/CD, and more.

**Version:** 1.0.2 | **Author:** cepm | **License:** MIT (skills © 650 Industries, Inc. aka Expo)

## What It Does

This plugin wraps 10 Expo skills into a marketplace plugin with slash commands, a specialist agent, and lifecycle hooks for mobile development with Expo Router and React Native.

## Prerequisites

| Tool | Required For | Install |
|------|-------------|---------|
| Node.js 18+ | All Expo/React Native development | [nodejs.org](https://nodejs.org/) |
| Expo CLI | Local dev server, project scaffolding | `npx expo` (bundled) or `npm install -g expo-cli` |
| EAS CLI | Cloud builds, submissions, updates | `npm install -g eas-cli` then `eas login` |
| Apple Developer account | iOS builds and App Store submission | [developer.apple.com](https://developer.apple.com/) |
| Google Play Console account | Android deployment | [play.google.com/console](https://play.google.com/console/) |
| Watchman (macOS) | Fast file watching for Metro | `brew install watchman` |

## Installation

**Option 1 — Copy into project:**
```bash
cp -r plugins/proagent-mobile /path/to/your/project/.claude/plugins/
```

**Option 2 — Reference from marketplace:**
```json
{ "source": "./plugins/proagent-mobile" }
```

**Option 3 — Symlink:**
```bash
ln -s /path/to/provectus-marketplace/plugins/proagent-mobile ~/.claude/plugins/proagent-mobile
```

## Usage

### Slash Commands

```bash
# See all capabilities
/proagent-mobile-hub

# Run a workflow
/proagent-mobile-run build          # EAS dev client build
/proagent-mobile-run deploy         # App Store / Play Store deployment
/proagent-mobile-run setup          # New project setup
/proagent-mobile-run ui             # UI and navigation development
/proagent-mobile-run cicd           # CI/CD with EAS workflows
/proagent-mobile-run upgrade        # Expo SDK version upgrade
/proagent-mobile-run data-fetching  # Data fetching patterns

# Review your project
/proagent-mobile-review app-config     # Audit app.json / eas.json
/proagent-mobile-review code-quality   # Code quality review
/proagent-mobile-review dependencies   # Dependency health check
```

### Via the Router

```bash
/proagent set up EAS Build for my React Native app
/proagent deploy my Expo app to TestFlight
/proagent add React Query to my Expo project
/proagent upgrade my app to Expo SDK 52
```

## Environment Variables

| Variable | Used By |
|----------|---------|
| `EXPO_TOKEN` | EAS CLI authentication (CI/CD environments) |
| `APPLE_ID` | iOS App Store submission via `eas submit` |
| `APPLE_TEAM_ID` | iOS code signing and provisioning |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | GitHub MCP server |
| `SLACK_MCP_XOXC_TOKEN` / `SLACK_MCP_XOXD_TOKEN` | Slack MCP server |

## MCP Servers

| Server | Package | Purpose |
|--------|---------|---------|
| GitHub | `@modelcontextprotocol/server-github` | Repos, PRs, issues, Actions |
| Slack | `slack-mcp-server` | Team communication, channels, messages, threads |
| Google Drive | `@modelcontextprotocol/server-gdrive` | Drive files, Docs, Sheets, Slides |
| Google Workspace | `mcp-gsuite` | Gmail and Google Calendar |
| Excalidraw | `excalidraw/excalidraw-mcp` (remote) | Interactive visual diagramming in chat |

## Workflow Examples

### First EAS Build

1. Run `/proagent-mobile-run setup` to scaffold or verify project structure.
2. Run `eas build:configure` to generate `eas.json` with development, preview, and production profiles.
3. Run `eas build --profile development --platform ios` to kick off a cloud build.
4. Scan the QR code from the EAS dashboard to install the dev client on your device.

### Deploy to App Store

1. Bump `version` and `ios.buildNumber` in `app.json`.
2. Run `eas build --profile production --platform ios` for a release build.
3. Run `eas submit --platform ios` to upload to App Store Connect.
4. Monitor submission status with `eas submit:status`.

### Add Data Fetching

1. Run `/proagent-mobile-run data-fetching` to get guided setup.
2. Install React Query: `npx expo install @tanstack/react-query`.
3. Wrap your root layout with `QueryClientProvider`.
4. Replace raw `fetch` calls with `useQuery` hooks for caching and offline support.

## Component Inventory

| Component | Count | Description |
|---|---|---|
| Skills | 1 | `mobile-assistant` — thin router to 10 topic references |
| Reference files | 34 | 10 skill files + 24 sub-references (sourced from expo/skills) |
| Commands | 3 | hub, run, review |
| Mode files | 10 | 7 run modes + 3 review modes |
| Agents | 1 | `mobile-specialist` (sonnet) |
| Hooks | 3 | EAS build guard, app config watcher, session completion |

## Skills Reference

| Skill | Topics Covered |
|---|---|
| `building-native-ui` | Expo Router, components, navigation, animations, native tabs |
| `expo-dev-client` | EAS dev clients, TestFlight distribution, local builds |
| `expo-deployment` | App Store, Play Store, web hosting, TestFlight |
| `native-data-fetching` | fetch, React Query, SWR, caching, offline support |
| `expo-api-routes` | Server API routes with Expo Router + EAS Hosting |
| `expo-cicd-workflows` | EAS workflow YAML, CI/CD automation |
| `expo-tailwind-setup` | NativeWind v5, Tailwind CSS v4, react-native-css |
| `upgrading-expo` | SDK upgrades, new architecture, React 19 migration |
| `expo-android-safe-area` | Android navigation bar insets, safe area handling |
| `use-dom` | Expo DOM components for web-in-native |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| EAS build fails with auth error | Run `eas whoami` to verify login. Re-authenticate with `eas login`. For CI, set `EXPO_TOKEN`. |
| Expo Doctor shows warnings | Run `npx expo install --fix` to align dependency versions with the current SDK. |
| Native module not found at runtime | You need a dev client build (`eas build --profile development`), not Expo Go. |
| Metro bundler stuck or stale cache | Clear with `npx expo start --clear` or delete `node_modules/.cache`. |
| iOS build missing provisioning profile | Run `eas credentials` to set up or sync Apple certificates and profiles. |

## Attribution

Skills sourced from [expo/skills](https://github.com/expo/skills) (MIT License, © 2025-present 650 Industries, Inc. aka Expo).
