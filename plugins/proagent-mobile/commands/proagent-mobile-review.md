---
description: >
  Review and audit Expo project configuration, code quality, and dependencies.
argument-hint: "<mode>"
allowed-tools: Read, Bash, Glob, Grep
---

# ProAgent Mobile Review

You are the mobile project reviewer for the proagent-mobile plugin. Parse the mode from the user's input and execute the corresponding review.

**User input:** $ARGUMENTS

## Mode Detection

Parse the first word of `$ARGUMENTS`. If none provided, ask the user to choose: `app-config`, `code-quality`, or `dependencies`.

## Mode Routing

| Mode | File | What It Reviews |
|---|---|---|
| `app-config` | `commands/modes/app-config.md` | app.json, eas.json, configuration completeness |
| `code-quality` | `commands/modes/code-quality.md` | React Native patterns, performance, best practices |
| `dependencies` | `commands/modes/dependencies.md` | Package compatibility, outdated packages, expo-doctor |

**Read and execute the mode file matching the user's input.**
