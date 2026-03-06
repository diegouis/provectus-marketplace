# proagent-mobile

> Mobile app development with Expo and React Native — 10 skills covering UI, EAS builds, deployment, data fetching, CI/CD, and more.

**Version:** 1.0.0 | **Author:** cepm | **License:** MIT (skills © 650 Industries, Inc. aka Expo)

## What It Does

This plugin wraps 10 Expo skills into a marketplace plugin with slash commands, a specialist agent, and lifecycle hooks for mobile development with Expo Router and React Native.

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

## Attribution

Skills sourced from [expo/skills](https://github.com/expo/skills) (MIT License, © 2025-present 650 Industries, Inc. aka Expo).
