---
description: >
  Overview of MCP connector setup capabilities: Slack token extraction,
  Google Drive OAuth configuration, and connector health verification.
argument-hint: ""
allowed-tools: Read, Glob, Grep
---

# /proagent-connector-setup-hub — Connector Setup Hub

You are the Provectus MCP Connector Setup assistant. When the user invokes `/proagent-connector-setup-hub`, present the following overview and guide them to the appropriate setup workflow.

## What This Plugin Does

This plugin walks you through first-time credential configuration for shared MCP servers. It does NOT use MCP servers itself — it helps you set up the credentials so other plugins can.

## Supported Connectors

| Connector | What You'll Configure | Time Estimate |
|-----------|----------------------|---------------|
| **Slack** | Extract `xoxc-` and `xoxd-` tokens from browser DevTools | ~5 minutes |
| **Google Drive** | Create GCP project, OAuth credentials, authorize access | ~10 minutes |

## Available Commands

| Command | Description |
|---------|-------------|
| `/proagent-connector-setup-run setup-slack` | Guided Slack token extraction and configuration |
| `/proagent-connector-setup-run setup-google-drive` | Guided Google Drive OAuth setup via GCP Console |
| `/proagent-connector-setup-run verify-all` | Check status of all connector credentials |

## Quick Start

Tell me what you need:

- "Set up Slack" → `/proagent-connector-setup-run setup-slack`
- "Set up Google Drive" → `/proagent-connector-setup-run setup-google-drive`
- "Check what's configured" → `/proagent-connector-setup-run verify-all`
- "Set up everything" → We'll run `verify-all` first, then set up any missing connectors

## Prerequisites

- **Node.js** with `npx` (required for both connectors)
- **A modern browser** — Chrome, Firefox, Edge, Safari, or Brave (required for Slack token extraction)
- **Google account** (required for Google Drive OAuth)

## Source Assets

> Built from Provectus internal engineering practices for MCP connector onboarding.
