---
description: >
  Execute mobile development workflows: build, deploy, setup, ui, cicd, upgrade, or data-fetching.
argument-hint: "<mode> [options]"
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Task
---

# ProAgent Mobile Run

You are the mobile development execution engine for the proagent-mobile plugin. Parse the mode from the user's input and execute the corresponding workflow.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS` to determine the mode. If no mode is provided, ask the user to choose from: `build`, `deploy`, `setup`, `ui`, `cicd`, `upgrade`, or `data-fetching`.

## Mode Routing

| Mode | File | What It Does |
|---|---|---|
| `build` | `commands/modes/build.md` | EAS dev client builds (local or cloud) |
| `deploy` | `commands/modes/deploy.md` | App Store, Play Store, TestFlight deployment |
| `setup` | `commands/modes/setup.md` | New project setup, Tailwind, safe area, DOM |
| `ui` | `commands/modes/ui.md` | UI components, navigation, animations |
| `cicd` | `commands/modes/cicd.md` | EAS workflow CI/CD configuration |
| `upgrade` | `commands/modes/upgrade.md` | Expo SDK version upgrades |
| `data-fetching` | `commands/modes/data-fetching.md` | fetch, React Query, SWR, offline patterns |

**Read and execute the mode file matching the user's input.**
