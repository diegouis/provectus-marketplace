# Google Drive MCP OAuth Setup Reference

This reference is loaded at point-of-need during the Google Drive setup flow. It contains detailed GCP console steps.

## Overview

The Google Drive MCP server (`@modelcontextprotocol/server-gdrive`) uses OAuth 2.0 with a Desktop application credential. The setup requires:

1. A GCP project with the Google Drive API enabled
2. An OAuth consent screen configured
3. A Desktop application OAuth client credential
4. The credential file downloaded and placed at `~/gcp-oauth.keys.json`
5. A one-time OAuth authorization flow

## Step-by-Step Setup

### Step 1: Create or Select a GCP Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click the project dropdown at the top of the page
3. Click **New Project** (or select an existing project)
4. Name it something recognizable, e.g., `mcp-connectors`
5. Click **Create** and wait for the project to be provisioned
6. Make sure the new project is selected in the dropdown

### Step 2: Enable the Google Drive API

1. In the GCP Console, go to **APIs & Services** → **Library**
   - Direct URL: `https://console.cloud.google.com/apis/library`
2. Search for **Google Drive API**
3. Click on **Google Drive API** in the results
4. Click **Enable**
5. Wait for the API to be enabled (a few seconds)

### Step 3: Configure the OAuth Consent Screen

1. Go to **APIs & Services** → **OAuth consent screen**
   - Direct URL: `https://console.cloud.google.com/apis/credentials/consent`
2. Select **External** user type (unless you have a Google Workspace org and want Internal)
3. Click **Create**
4. Fill in the required fields:
   - **App name**: `MCP Drive Connector` (or any name)
   - **User support email**: Your email address
   - **Developer contact information**: Your email address
5. Click **Save and Continue**
6. On the **Scopes** page, click **Add or Remove Scopes**
   - Search for and add: `https://www.googleapis.com/auth/drive.readonly`
   - (Add `drive` scope instead if you need write access)
7. Click **Save and Continue**
8. On the **Test users** page, click **Add Users**
   - Add your own Google account email
9. Click **Save and Continue**, then **Back to Dashboard**

> **Important**: While in "Testing" status, only test users you explicitly add can authorize. This is fine for personal use.

### Step 4: Create OAuth Client Credentials

1. Go to **APIs & Services** → **Credentials**
   - Direct URL: `https://console.cloud.google.com/apis/credentials`
2. Click **Create Credentials** → **OAuth client ID**
3. **Application type**: Select **Desktop app** (NOT Web application!)
4. **Name**: `MCP Drive Desktop` (or any name)
5. Click **Create**
6. A dialog shows your Client ID and Client Secret — click **Download JSON**
7. Rename the downloaded file to `gcp-oauth.keys.json`
8. Move it to your home directory:

```bash
# macOS / Linux
mv ~/Downloads/client_secret_*.json ~/gcp-oauth.keys.json
```

### Step 5: Verify the Credential File

The file should have this structure:

```json
{
  "installed": {
    "client_id": "123456789-abcdef.apps.googleusercontent.com",
    "project_id": "mcp-connectors",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "GOCSPX-...",
    "redirect_uris": ["http://localhost"]
  }
}
```

**Key check**: The top-level key must be `"installed"` (not `"web"`). If it says `"web"`, you created a Web application credential — go back and create a Desktop app credential.

### Step 6: Run the OAuth Authorization Flow

```bash
npx -y @modelcontextprotocol/server-gdrive auth ~/gcp-oauth.keys.json
```

This will:
1. Start a local HTTP server
2. Open your browser to a Google consent page
3. Ask you to sign in and grant Drive access
4. Redirect back to localhost to capture the auth code
5. Exchange the code for access/refresh tokens
6. Store tokens in `~/.gdrive-server/credentials.json`

> If the browser doesn't open automatically, copy the URL from the terminal and paste it into your browser.

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `~/gcp-oauth.keys.json` not found | File not downloaded or wrong path | Re-download from GCP Console → Credentials → Download JSON |
| `"web"` key instead of `"installed"` | Created Web application instead of Desktop app | Delete the credential, create a new one as **Desktop app** |
| "Access blocked: This app's request is invalid" | OAuth consent screen not configured | Complete Step 3 above — configure the consent screen |
| "Error 403: access_not_configured" | Google Drive API not enabled | Go to APIs & Services → Library → Enable Google Drive API |
| "Error: redirect_uri_mismatch" | Wrong credential type (Web instead of Desktop) | Create a new Desktop app credential (Step 4) |
| Auth flow completes but MCP server fails | Stale auth cache | Delete `~/.gdrive-server/credentials.json` and re-run auth |
| "This app is blocked" during consent | App in testing mode, user not added as test user | Add your email in OAuth consent screen → Test users |
| `npx` not found | Node.js not installed | Install from https://nodejs.org/ or `brew install node` |
| Port already in use during auth | Another process on the callback port | Kill the process or wait and retry |

## Auth Cache Location

After successful authorization, tokens are stored at:

```
~/.gdrive-server/credentials.json
```

This file contains access and refresh tokens. The refresh token allows the MCP server to obtain new access tokens automatically.

## Re-Authorization

If you need to re-authorize (e.g., changed scopes, revoked access):

```bash
# Delete the cached credentials
rm ~/.gdrive-server/credentials.json

# Re-run the auth flow
npx -y @modelcontextprotocol/server-gdrive auth ~/gcp-oauth.keys.json
```

## Scopes Reference

| Scope | Access Level |
|-------|-------------|
| `drive.readonly` | Read-only access to all Drive files |
| `drive` | Full read/write access to all Drive files |
| `drive.file` | Access only to files created by this app |
| `drive.metadata.readonly` | Read-only access to file metadata |
