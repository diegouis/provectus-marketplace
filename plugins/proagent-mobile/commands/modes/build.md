# Mode: build

**Goal:** Set up and run EAS Build to create a development client for testing native code on a device.

> **Adequacy Gate**: Before proceeding, verify:
> 1. `eas whoami` returns a valid account
> 2. `app.json` exists with `expo.slug` defined
> 3. Platform target is specified (ios, android, or both)
> If any check fails, inform the user and collect missing prerequisites before continuing.

**Announce:** "Starting EAS Build workflow. I'll help you create a development client for iOS or Android."

> **CONTEXT GUARD**: ONLY read the reference file below now that the user has selected this mode.
> Do NOT pre-load additional references until the user needs them.

Read and execute the guidance in `skills/mobile-assistant/references/expo-dev-client.md`.

**When complete:**
- Confirm which platform was built (iOS / Android / both)
- Remind the user to install the dev client on their device
- Suggest next step: `/proagent-mobile:proagent-mobile-run deploy` when ready for store submission
