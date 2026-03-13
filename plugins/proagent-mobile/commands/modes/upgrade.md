# Mode: upgrade

**Goal:** Upgrade the Expo SDK version and handle migration tasks.

> **Adequacy Gate**: Before proceeding, verify:
> 1. Current SDK version is identified from package.json
> 2. Git working tree is clean (commit or stash changes first)
> 3. User has reviewed the Expo changelog for breaking changes
> If any check fails, inform the user and collect missing prerequisites before continuing.

**Announce:** "Starting SDK upgrade workflow. I'll guide you through the upgrade process and any required migrations."

> **CONTEXT GUARD**: ONLY read the reference file below now that the user has selected this mode.

Read and execute the guidance in `skills/mobile-assistant/references/upgrading-expo.md`.

For specific migration topics, load sub-references at point-of-need:
- New Architecture migration → `skills/mobile-assistant/references/upgrading-expo/new-architecture.md`
- React 19 migration → `skills/mobile-assistant/references/upgrading-expo/react-19.md`
- React Compiler → `skills/mobile-assistant/references/upgrading-expo/react-compiler.md`
- Native tabs changes → `skills/mobile-assistant/references/upgrading-expo/native-tabs.md`
- expo-av → @expo/video → `skills/mobile-assistant/references/upgrading-expo/expo-av-to-video.md`
- expo-av → expo-audio → `skills/mobile-assistant/references/upgrading-expo/expo-av-to-audio.md`
