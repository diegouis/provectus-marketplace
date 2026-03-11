---
description: >
  Guided Google Drive MCP OAuth setup: GCP project creation, Drive API enablement,
  OAuth consent screen, Desktop credential, auth flow, and verification.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# Setup Google Drive — MCP OAuth Configuration

Walk the user through configuring Google Drive MCP credentials via GCP OAuth. Follow each step sequentially — confirm completion at each adequacy gate before proceeding.

## Step 1: Prerequisites Check

1. **Ask the user** which OS they are on: **macOS**, **Windows**, or **Linux**. Remember their answer — it determines file paths throughout this flow.
2. Verify `npx` is available:
   ```bash
   which npx 2>/dev/null && npx --version || echo "npx not found"
   ```
3. Check if `~/gcp-oauth.keys.json` already exists:
   ```bash
   test -f ~/gcp-oauth.keys.json && echo "Credential file exists" || echo "No credential file"
   ```
4. Check if auth cache already exists:
   ```bash
   test -f ~/.gdrive-server/credentials.json && echo "Auth cache exists" || echo "No auth cache"
   ```

If both files exist, offer to skip directly to **Step 5: Verify** or start fresh.

**Adequacy gate**: OS, shell, and npx confirmed. Existing state assessed.

## Step 2: GCP Project and Drive API

> **CONTEXT GUARD**: ONLY read the reference file below when the user reaches this step. Do NOT pre-load it during earlier steps or at skill initialization.

Load the detailed reference:
```
Read file: skills/connector-setup-assistant/references/google-drive-setup.md
```

Guide the user through:

1. **Create or select a GCP project** at https://console.cloud.google.com/
   - Suggest naming it `mcp-connectors`
2. **Enable the Google Drive API**:
   - Navigate to APIs & Services → Library → search "Google Drive API" → Enable

Ask: "Have you enabled the Google Drive API in your GCP project?"

**Bounded iteration**: If the user reports errors (403, access denied), troubleshoot using the reference. After 3 failed attempts, offer to pause.

**Adequacy gate**: User confirms Drive API is enabled.

## Step 3: OAuth Consent Screen

Guide the user through configuring the consent screen:

1. Go to APIs & Services → OAuth consent screen
2. Select **External** user type
3. Fill in app name, support email, developer email
4. Add scope: `https://www.googleapis.com/auth/drive.readonly`
5. Add themselves as a test user

Ask: "Have you configured the OAuth consent screen and added yourself as a test user?"

**Adequacy gate**: User confirms consent screen is configured.

## Step 4: Create OAuth Credentials and Download

Guide the user through:

1. Go to APIs & Services → Credentials
2. Create Credentials → OAuth client ID
3. **Application type: Desktop app** (emphasize this — "Web application" is the most common mistake)
4. Download the JSON file
5. Rename and move it:

```bash
# The user should run this with their actual downloaded filename
mv ~/Downloads/client_secret_*.json ~/gcp-oauth.keys.json
```

Verify the file:
```bash
# Check the file exists and has the correct structure
test -f ~/gcp-oauth.keys.json && python3 -c "
import json
with open('$HOME/gcp-oauth.keys.json') as f:
    data = json.load(f)
    if 'installed' in data:
        print('OK: Desktop app credential (installed)')
        print('Client ID:', data['installed']['client_id'][:20] + '...')
    elif 'web' in data:
        print('ERROR: Web application credential detected. Please create a Desktop app credential.')
    else:
        print('ERROR: Unexpected credential format')
" || echo "File not found or invalid JSON"
```

**Bounded iteration**: If the user downloaded the wrong type (web instead of installed), guide them to delete and recreate. After 3 attempts, offer to pause.

**Adequacy gate**: `~/gcp-oauth.keys.json` exists with `"installed"` key.

## Step 5: Run OAuth Authorization Flow

```bash
npx -y @modelcontextprotocol/server-gdrive auth ~/gcp-oauth.keys.json
```

Tell the user:
- A browser window will open asking them to sign in with Google
- They should use the same Google account they added as a test user
- Grant the requested Drive permissions
- The browser will redirect to localhost — this is expected

Wait for the user to confirm the flow completed.

**Failure handling**:
- "This app is blocked" → User not added as test user in consent screen
- "redirect_uri_mismatch" → Wrong credential type (web vs desktop)
- "access_not_configured" → Drive API not enabled
- Browser doesn't open → Copy the URL from terminal and paste manually

**Bounded iteration**: After 3 failed attempts, offer to pause or restart from Step 2.

**Adequacy gate**: Auth flow completes and `~/.gdrive-server/credentials.json` is created.

## Step 6: Verify Live Connectivity

```bash
# Check auth cache was created
test -f ~/.gdrive-server/credentials.json && echo "Auth cache: OK" || echo "Auth cache: MISSING"

# Quick server test
timeout 5 npx -y @modelcontextprotocol/server-gdrive 2>&1 || true
```

**Success indicators**:
- Auth cache file exists
- Server starts without OAuth errors

## Completion Report

When verification succeeds, present:

```
Google Drive MCP Setup Complete
================================
GCP Project:     [project name if known]
Credential file: ~/gcp-oauth.keys.json  ✓ present (Desktop app)
Auth cache:      ~/.gdrive-server/credentials.json  ✓ present
Live test:       ✓ connected successfully

Next steps:
- Plugins with Google Drive in .mcp.json will now authenticate automatically
- If you revoke access in Google Account settings, re-run this setup
- Run /proagent-connector-setup-run verify-all to check all connectors
```
