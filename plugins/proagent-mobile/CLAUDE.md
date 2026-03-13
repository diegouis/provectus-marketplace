# proagent-mobile

Mobile app development plugin for Expo and React Native. Wraps 10 skills from [expo/skills](https://github.com/expo/skills) (MIT License) with marketplace commands, a specialist agent, and lifecycle hooks.

## Plugin Scope

This plugin covers ten mobile development domains: UI development (components, navigation, animations), EAS builds (dev client, cloud builds), App Store and Play Store deployment (including TestFlight), data fetching (React Query, SWR, offline patterns), API routes (Expo Router + EAS Hosting), CI/CD workflows (EAS workflow YAML), Tailwind/NativeWind styling, SDK upgrades (migration guides, new architecture, React 19), Android safe area handling, and DOM components. All skills wrap reference content from the expo/skills repository.

## Directory Tree

```
proagent-mobile/
├── .claude-plugin/plugin.json              # Manifest: name, version, author
├── .mcp.json                               # No MCP servers (local tooling only)
├── LICENSE                                 # MIT — Copyright 650 Industries, Inc. (Expo)
├── skills/mobile-assistant/
│   ├── SKILL.md                            # Thin router (<80 lines) — auto-triggers on Expo keywords
│   └── references/
│       ├── building-native-ui.md           # Expo Router UI, components, navigation, animations
│       ├── building-native-ui/             # 13 topic references (animations, tabs, icons…)
│       ├── expo-dev-client.md              # EAS dev client builds
│       ├── expo-deployment.md              # App Store, Play Store, TestFlight
│       ├── expo-deployment/                # 5 platform references (ios, android, testflight…)
│       ├── expo-api-routes.md              # API routes with Expo Router + EAS Hosting
│       ├── expo-android-safe-area.md       # Android navigation bar inset handling
│       ├── expo-cicd-workflows.md          # EAS workflow YAML files
│       ├── expo-tailwind-setup.md          # NativeWind v5 + Tailwind CSS v4
│       ├── upgrading-expo.md               # SDK version upgrades
│       ├── upgrading-expo/                 # 6 migration references (new arch, React 19…)
│       ├── use-dom.md                      # Expo DOM components
│       └── native-data-fetching.md         # fetch, React Query, SWR, offline
├── commands/
│   ├── proagent-mobile-hub.md              # /proagent-mobile-hub — capabilities overview
│   ├── proagent-mobile-run.md              # /proagent-mobile-run — execution dispatcher
│   ├── proagent-mobile-review.md           # /proagent-mobile-review — review dispatcher
│   └── modes/
│       ├── build.md                        # EAS dev client build workflow
│       ├── deploy.md                       # App Store / Play Store deployment
│       ├── setup.md                        # New project setup
│       ├── ui.md                           # UI and navigation development
│       ├── cicd.md                         # CI/CD with EAS workflows
│       ├── upgrade.md                      # SDK version upgrades
│       ├── data-fetching.md                # Data fetching patterns
│       ├── app-config.md                   # Review: app.json / eas.json audit
│       ├── code-quality.md                 # Review: React Native code patterns
│       └── dependencies.md                 # Review: package compatibility
├── agents/mobile-specialist.md             # Specialist agent — routes to references at point-of-need
├── hooks/hooks.json                        # EAS operation guards and app config watchers
├── CLAUDE.md                               # This file
└── README.md                               # User-facing docs
```

## Skills

| Skill | Auto-triggers on |
|---|---|
| `mobile-assistant` | Expo, React Native, EAS, expo-router, mobile app, iOS, Android, dev client, NativeWind, TestFlight, React Query, SWR, safe area |

## Commands

| Command | Modes |
|---|---|
| `/proagent-mobile-hub` | — (overview) |
| `/proagent-mobile-run` | `build`, `deploy`, `setup`, `ui`, `cicd`, `upgrade`, `data-fetching` |
| `/proagent-mobile-review` | `app-config`, `code-quality`, `dependencies` |

## Agents

| Agent | Model | Purpose |
|---|---|---|
| `mobile-specialist` | sonnet | Full-stack Expo specialist, loads references at point-of-need |

## Hooks

| Event | Trigger | Action |
|---|---|---|
| PreToolUse/Bash | `eas build/submit/deploy` | Remind to verify credentials and version numbers |
| PostToolUse/Write | `app.json`, `eas.json`, `app.config.*` | Remind to run `eas build:configure` |
| PostToolUse/Task | `mobile-specialist` dispatch | Remind to test on device before store submission |

## Key Conventions

- **Expo-first**: prefer Expo APIs over bare React Native when an Expo equivalent exists
- **Device testing**: always test on a physical device before any store submission
- **Platform handling**: explicitly address iOS vs Android differences in layouts, permissions, and navigation
- **EAS workflow**: use EAS Build for cloud builds, EAS Submit for store deployment — avoid local `xcodebuild`/`gradle` unless debugging
- **Version management**: bump `expo.version` + `ios.buildNumber`/`android.versionCode` before each store submission
- **Safe area**: always wrap root layout in `SafeAreaProvider`; use `useSafeAreaInsets` for custom headers
- **Tailwind**: use NativeWind v5 with Tailwind CSS v4 — no Babel plugin needed, configure via `metro.config.js`

## MCP Integrations

- **GitHub**: EAS GitHub Actions workflows, PR reviews, release management
- **Slack**: Build failure notifications, team coordination on release windows
- **Google Drive**: App Store screenshots, release notes, certification documents
- **Google Workspace**: Calendar for release scheduling, Gmail for store correspondence
- **Excalidraw**: App architecture diagrams, navigation flow visualization

## Attribution

Skills sourced from [expo/skills](https://github.com/expo/skills) (MIT License, © 2025-present 650 Industries, Inc.). 34 reference files covering 10 topic areas.
