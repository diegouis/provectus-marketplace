# Mode: setup

**Goal:** Set up a new Expo project or configure tooling in an existing one.

> **Adequacy Gate**: Before proceeding, verify:
> 1. Node.js 18+ is installed
> 2. Target directory is empty or user confirms overwrite
> 3. User has chosen a template (blank, tabs, or custom)
> If any check fails, inform the user and collect missing prerequisites before continuing.

**Announce:** "Starting project setup. What would you like to configure?"

Ask the user which setup task they need:

1. **New project** — scaffold a new app with Expo Router
2. **Tailwind styling** — add NativeWind v5 + Tailwind CSS v4
3. **Android safe area** — configure safe area insets for the navigation bar
4. **DOM components** — add Expo DOM component support for web-in-native

> **CONTEXT GUARD**: ONLY read the reference file AFTER the user has selected one of the options above.

Load the relevant reference at point-of-need:
- New project or Expo Router basics → `skills/mobile-assistant/references/building-native-ui.md`
- Tailwind / NativeWind → `skills/mobile-assistant/references/expo-tailwind-setup.md`
- Android safe area → `skills/mobile-assistant/references/expo-android-safe-area.md`
- DOM components → `skills/mobile-assistant/references/use-dom.md`
