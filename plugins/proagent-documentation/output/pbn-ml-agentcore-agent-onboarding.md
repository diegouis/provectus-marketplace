# Developer Onboarding Guide: pbn-ml-agentcore-agent

> **Repository**: [Provectus-PBN/pbn-ml-agentcore-agent](https://github.com/Provectus-PBN/pbn-ml-agentcore-agent)
> **Last updated**: 2026-02-18

---

## Welcome

This guide walks you through getting productive with the **PBN ML AgentCore Agent** repository — the multi-agent system powering Punchbowl News' AI-driven political intelligence platform. By the end of this guide, you'll understand the architecture, be able to run agents locally, and know how to deploy changes.

---

## Table of Contents

1. [What This Project Does](#1-what-this-project-does)
2. [Architecture Overview](#2-architecture-overview)
3. [Prerequisites](#3-prerequisites)
4. [Day 1: Environment Setup & Orientation](#4-day-1-environment-setup--orientation)
5. [Day 2: Understanding Agent Structure](#5-day-2-understanding-agent-structure)
6. [Day 3: Running an Agent Locally](#6-day-3-running-an-agent-locally)
7. [Day 4: Gateway & MCP Protocol Deep Dive](#7-day-4-gateway--mcp-protocol-deep-dive)
8. [Day 5: Orchestrator Agent & Multi-Agent Flow](#8-day-5-orchestrator-agent--multi-agent-flow)
9. [Day 6: CI/CD, Deployment & Infrastructure](#9-day-6-cicd-deployment--infrastructure)
10. [Day 7: Making Your First Change](#10-day-7-making-your-first-change)
11. [Key Concepts Reference](#11-key-concepts-reference)
12. [Common Tasks Cheat Sheet](#12-common-tasks-cheat-sheet)
13. [Troubleshooting](#13-troubleshooting)
14. [Who to Ask](#14-who-to-ask)

---

## 1. What This Project Does

PBN AgentCore is a **multi-agent AI system** that provides political intelligence for Punchbowl News journalists and subscribers. It consists of:

- **7 specialized sub-agents** that each handle a specific data domain (votes, staffers, regulations, etc.)
- **1 orchestrator agent** that routes user queries to the appropriate sub-agent(s) and synthesizes responses
- All agents run on **AWS Bedrock AgentCore** using **Claude Sonnet 4.5** as the LLM
- Communication between agents and backend APIs uses the **Model Context Protocol (MCP)**

### Data Domains

| Agent | What It Queries |
|-------|----------------|
| Votes/Bills | House & Senate voting records, bill statuses, roll calls |
| Staffers | Congressional staff members, roles, contact info |
| FEC/LDA | Campaign finance filings, lobbying disclosure reports |
| Floor/Committees | Committee hearings, floor schedules, meeting transcripts |
| Regulations | Federal Register notices, agency rulemaking, dockets |
| PBN News | Punchbowl News articles, political reporting archives |
| Alerts | User notification subscriptions and alert management |

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     User Query (via PBN API)                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              Orchestrator Agent (Strands + BedrockModel)         │
│  - Routes queries to appropriate sub-agent(s)                    │
│  - Synthesizes multi-source responses                            │
│  - Uses Claude Sonnet 4.5 for reasoning                          │
└──┬──────┬──────┬──────┬──────┬──────┬──────┬────────────────────┘
   │      │      │      │      │      │      │
   ▼      ▼      ▼      ▼      ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│Votes ││Staff ││FEC/  ││Floor/││Regs  ││PBN   ││Alerts│
│Agent ││Agent ││LDA   ││Comm. ││Agent ││News  ││Agent │
└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘└──┬───┘
   │       │       │       │       │       │       │
   ▼       ▼       ▼       ▼       ▼       ▼       ▼
┌─────────────────────────────────────────────────────────────────┐
│              MCP Gateway (Bedrock AgentCore Gateway)             │
│  - Cognito OAuth2 authentication                                 │
│  - OpenAPI spec → MCP tool conversion                            │
│  - Streamable HTTP transport                                     │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                   FastAPI Backend Services                        │
│  (pbn-ml-coordinator-agent / pbn-backend-enbloc-api)             │
│  - Text2SQL agents for structured data                           │
│  - RAG retrieval for unstructured data                           │
│  - PostgreSQL + pgvector + S3                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Two Types of Agents

1. **Sub-agents** (e.g., `votes_agent_mcp_tools/`): Connect to backend APIs via MCP Gateway. Each wraps MCP tool calls with a custom `EnblocPayloadTool` that transforms Strands agent calls into the required payload format.

2. **Orchestrator agent** (`orchestrartor_agent/`): Doesn't use MCP. Instead, it invokes sub-agent runtimes directly via `boto3` / `aioboto3` calls to `bedrock-agentcore:invoke_agent_runtime`.

---

## 3. Prerequisites

### Required Software

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.12+ | Runtime for all agents |
| Docker | With Buildx | Container builds (ARM64) |
| AWS CLI | v2.x+ | AWS service interaction |
| Git | Any recent | Version control |
| uv | Latest | Fast Python package installer (used in Docker) |

### Required Access

- [ ] **GitHub**: Write access to `Provectus-PBN/pbn-ml-agentcore-agent`
- [ ] **AWS Account**: IAM credentials (not SSO) with access to:
  - Amazon Bedrock (AgentCore + model invocation)
  - Amazon ECR (container registry)
  - Amazon Cognito (OAuth2 tokens)
  - AWS Secrets Manager
  - CloudWatch Logs
- [ ] **AWS Region**: `us-east-1` (all resources are deployed here)

### Verify Your Setup

```bash
# Python version
python3 --version  # Should be 3.12+

# Docker
docker --version
docker buildx version

# AWS CLI
aws --version
aws sts get-caller-identity  # Should show your account

# Bedrock access
aws bedrock list-foundation-models --region us-east-1 --query 'modelSummaries[?contains(modelId, `anthropic`)].modelId' --output table
```

---

## 4. Day 1: Environment Setup & Orientation

### Clone the Repository

```bash
git clone https://github.com/Provectus-PBN/pbn-ml-agentcore-agent.git
cd pbn-ml-agentcore-agent
```

### Understand the Directory Layout

```
pbn-ml-agentcore-agent/
├── votes_agent_mcp_tools/          # Votes/Bills sub-agent
│   ├── agent_deployment/           #   Runtime code + Docker
│   └── gateway/                    #   MCP Gateway setup scripts
├── staffers_agent_mcp_tools/       # Staffers sub-agent
├── fec_lda_agent_mcp_tools/        # FEC/LDA sub-agent
├── floor_committees_agent_mcp_tools/ # Floor/Committees sub-agent
├── regulations_agent_mcp_tools/    # Regulations sub-agent
├── punchbowl_news_agent_mcp_tools/ # PBN News sub-agent
├── alerts_agent_mcp_tools/         # Alerts sub-agent
├── orchestrartor_agent/            # Orchestrator (multi-agent coordinator)
│   └── agent_deployment/           #   Runtime code + Docker
├── infrastructure/                 # Terraform configs
│   └── terraform/
│       ├── github-oidc/            #   GitHub Actions OIDC (one-time setup)
│       ├── gateways/               #   MCP Gateway Terraform modules
│       ├── modules/                #   Reusable Terraform modules
│       └── scripts/                #   Setup helper scripts
├── legacy/                         # Deprecated agent implementations
├── .github/workflows/              # CI/CD pipeline
│   └── deploy-agents.yml           #   Build + deploy workflow
├── README.md
└── .gitignore
```

### Read These Files First

Spend your first day reading these key files to build mental models:

1. **Root README.md** — High-level overview and conventions
2. **`votes_agent_mcp_tools/agent_deployment/main_app.py`** — How a sub-agent starts up (simplest entry point)
3. **`orchestrartor_agent/agent_deployment/main_app.py`** — How the orchestrator starts up
4. **`orchestrartor_agent/agent_deployment/orchestrator_instructions.txt`** — The LLM system prompt (explains what each agent does)
5. **`infrastructure/terraform/README.md`** — Deployment architecture and CI/CD flow

---

## 5. Day 2: Understanding Agent Structure

### Sub-Agent Structure (e.g., votes_agent_mcp_tools)

Every sub-agent follows this pattern:

```
<agent>_mcp_tools/
├── agent_deployment/
│   ├── main_app.py                  # Entry point — creates MCP client, agent, runs app
│   ├── enbloc_mcp_wrapper_v2.py     # Custom tool wrapper (transforms payloads for gateway)
│   ├── utils_functions.py           # Helper functions (OAuth, transport, agent creation)
│   ├── orchestrator_instructions.txt # LLM system prompt (XML format)
│   ├── Dockerfile                   # ARM64 container build
│   ├── requirements.txt             # Python dependencies
│   ├── .bedrock_agentcore.yaml      # AgentCore deployment config
│   ├── .env.example                 # Environment variables template
│   ├── build_and_push_ecr.sh        # Manual ECR build script
│   ├── deploy_prepare.py            # AgentCore runtime configuration
│   ├── test_agent.py                # Integration test script
│   ├── payload/                     # Test payloads (JSON)
│   └── env_vars/                    # Per-environment config (config.json)
└── gateway/
    ├── <agent>_gateway_setup.py     # Creates IAM, Cognito, Gateway, Target
    ├── get_credentials.py           # Retrieves Cognito credentials
    ├── utils.py                     # Shared AWS utility functions
    ├── openapi-specs/               # Modified OpenAPI specs (anyOf fixed)
    └── env_vars/                    # Gateway configuration
```

### Key Code Flow (Sub-Agent)

```python
# main_app.py — Startup sequence:

1. Load env vars (GATEWAY_URL, CLIENT_ID, CLIENT_SECRET, TOKEN_URL, MODEL_ID)
2. Fetch OAuth2 access token from Cognito
3. Create MCP client with streamable HTTP transport
4. Open MCP client context (keeps connection alive)
5. List all available MCP tools from gateway
6. Wrap each tool with EnblocPayloadTool (payload transformation)
7. Create Strands Agent with BedrockModel + wrapped tools + system prompt
8. Register @app.entrypoint handler
9. app.run() — starts BedrockAgentCoreApp server

# When a query arrives:
@app.entrypoint
async def model_invoke(event):
    query = event["sessionAttributes"]["UserQuery"]
    response = await agent.invoke_async(query, invocation_state={'event': event})
    return response.message['content'][0]['text']
```

### The EnblocPayloadTool Wrapper

This is the most complex piece. It transforms agent tool calls into the specific payload format the backend APIs expect:

```python
# What the LLM generates:
{"toolUseId": "abc123", "input": {"query": "What bills passed today?"}}

# What EnblocPayloadTool sends to the gateway:
{
    "messageVersion": "1.0",
    "httpMethod": "POST",
    "sessionId": "from-invocation-state",
    "agent": {"name": "...", "version": "...", "id": "...", "alias": "..."},
    "actionGroup": "action_group_quick_start_sb1ze",
    "apiPath": "/query-all-legislative-activity",
    "sessionAttributes": {
        "MessageId": "abc123",
        "UserId": "from-event",
        "Metadata": "congressional context...",
        "UserQuery": "What bills passed today?",
        "UserToken": "jwt-token"
    },
    "inputText": "What bills passed today?"
}
```

### Orchestrator Structure

The orchestrator is simpler — no MCP, no gateway. It directly invokes sub-agent runtimes:

```python
# orchestrartor_agent/agent_deployment/pbn_agents.py

@tool(context=True)
async def votes_bills_agent(query: str, tool_context=None) -> str:
    event = tool_context.invocation_state.get('event')
    payload = build_agent_payload(event, query)
    response = await invoke_agent_async(VOTES_BILLS_AGENT_ARN, payload)
    return response
```

Each sub-agent is exposed as a Strands `@tool` that the orchestrator's LLM can call.

---

## 6. Day 3: Running an Agent Locally

### Option A: Run a Sub-Agent Locally

```bash
cd votes_agent_mcp_tools/agent_deployment

# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment variables
cp .env.example .env
# Edit .env with real credentials (ask your team lead):
#   GATEWAY_URL=https://<gateway>.gateway.bedrock-agentcore.us-east-1.amazonaws.com/mcp
#   CLIENT_ID=<from-cognito>
#   CLIENT_SECRET=<from-cognito>
#   TOKEN_URL=https://<pool>.auth.us-east-1.amazoncognito.com/oauth2/token
#   MODEL_ID=us.anthropic.claude-sonnet-4-5-20250929-v1:0

# 4. Run the agent
python main_app.py
# Agent starts on port 8080

# 5. Test with curl (in another terminal)
curl -X POST http://localhost:8080/invocations \
  -H "Content-Type: application/json" \
  -d "$(cat payload/payload.json)"
```

### Option B: Run with Docker

```bash
cd votes_agent_mcp_tools/agent_deployment

# Build ARM64 image
docker buildx build --platform linux/arm64 -t pbn-votes-agent --load .

# Run (pass env vars)
docker run -p 8080:8080 \
  -e GATEWAY_URL="..." \
  -e CLIENT_ID="..." \
  -e CLIENT_SECRET="..." \
  -e TOKEN_URL="..." \
  -e MODEL_ID="us.anthropic.claude-sonnet-4-5-20250929-v1:0" \
  pbn-votes-agent
```

### Option C: Test Against Deployed Agent

If the agent is already deployed to AgentCore, you can test it directly:

```bash
cd votes_agent_mcp_tools/agent_deployment

# Make sure AWS credentials are configured
python test_agent.py
```

This loads `payload/payload.json` and invokes the deployed runtime via `boto3`.

### Getting Credentials

To get the MCP Gateway credentials for an agent:

```bash
cd votes_agent_mcp_tools/gateway
python get_credentials.py
```

This queries Cognito and outputs GATEWAY_URL, CLIENT_ID, CLIENT_SECRET, and TOKEN_URL.

---

## 7. Day 4: Gateway & MCP Protocol Deep Dive

### What Is an MCP Gateway?

Each sub-agent talks to backend FastAPI services through an **MCP Gateway**. The gateway:

1. **Accepts** MCP protocol requests (streamable HTTP)
2. **Authenticates** via Cognito OAuth2 (client_credentials grant)
3. **Converts** OpenAPI endpoints into MCP tools
4. **Proxies** requests to the actual FastAPI backend

### Gateway Setup (One-Time Per Agent)

```bash
cd votes_agent_mcp_tools/gateway
python legislative_gateway_setup.py
```

This creates:
1. IAM role for the gateway
2. Cognito User Pool + App Client (M2M OAuth)
3. Bedrock AgentCore Gateway
4. S3 bucket for OpenAPI specs
5. Credential provider for API key auth
6. Gateway target mapping API endpoints to MCP tools

### OpenAPI Spec Compatibility Issue

AWS Bedrock AgentCore Gateway does **not** support `anyOf` type definitions in OpenAPI schemas. FastAPI auto-generates these for nullable fields.

**Before** (broken):
```json
"Metadata": {
  "anyOf": [{"type": "string"}, {"type": "null"}],
  "title": "Metadata"
}
```

**After** (fixed, stored in `openapi-specs/`):
```json
"Metadata": {"type": "string", "title": "Metadata"}
```

When updating OpenAPI specs:
1. Download from the API: `curl https://<api>/openapi.json > openapi-specs/<name>.json`
2. Find and fix `anyOf`: `grep -n "anyOf" openapi-specs/<name>.json`
3. Replace each `anyOf` with a simple type (prefer `string`)
4. Add `servers` block if missing
5. Upload to S3 and update gateway target

### MCP Tools Exposed (Votes Agent Example)

| MCP Tool | Maps To | Description |
|----------|---------|-------------|
| `query_all` | `POST /query-all-legislative-activity` | Query Bills + House + Senate concurrently |
| `bills` | `POST /query-bills` | Query bills data only |
| `house_votes` | `POST /query-house-votes` | Query House voting records only |
| `senate_votes` | `POST /query-senate-votes` | Query Senate voting records only |

---

## 8. Day 5: Orchestrator Agent & Multi-Agent Flow

### How the Orchestrator Works

The orchestrator is the "brain" — it receives user queries and decides which specialized agent(s) to call.

**File**: `orchestrartor_agent/agent_deployment/main_app.py`

```python
agent = Agent(
    model=BedrockModel(model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0"),
    tools=[
        votes_bills_agent,       # @tool function → invokes AgentCore runtime
        articles_agent,
        congressional_meetings_agent,
        regulations_agent,
        fec_lda_agent,
        alerts_agent,
        staffers_agent,
    ],
    system_prompt=system_prompt,  # Loaded from orchestrator_instructions.txt
)
```

### Query Flow Example

```
User: "How did senators vote on the latest defense bill?"

1. Orchestrator receives query
2. Claude Sonnet reasons: "This needs votes AND bills data"
3. Claude calls votes_bills_agent tool with the query
4. votes_bills_agent:
   a. Builds payload from invocation_state (session attrs, user token, etc.)
   b. Calls bedrock-agentcore:invoke_agent_runtime with VOTES_BILLS_AGENT_ARN
   c. Votes sub-agent receives payload
   d. Sub-agent's Claude instance decides to use query_bills_and_votes MCP tool
   e. EnblocPayloadTool wraps the call into gateway-compatible format
   f. MCP Gateway proxies to FastAPI backend
   g. Backend runs Text2SQL, queries PostgreSQL
   h. Response flows back up the chain
5. Orchestrator synthesizes the response and returns to user
```

### Orchestrator Environment Variables

The orchestrator needs ARNs for all deployed sub-agents:

```env
MODEL_ID=us.anthropic.claude-sonnet-4-5-20250929-v1:0
AWS_REGION=us-east-1
VOTES_BILLS_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
CONGRESSIONAL_MEETINGS_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
STAFFERS_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
ARTICLES_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
REGULATIONS_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
FEC_LDA_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
ALERTS_AGENT=arn:aws:bedrock-agentcore:us-east-1:ACCOUNT:runtime/RUNTIME_ID
```

---

## 9. Day 6: CI/CD, Deployment & Infrastructure

### GitHub Actions Pipeline

**File**: `.github/workflows/deploy-agents.yml`

The pipeline automates everything:

```
Push to main/develop
    │
    ▼
┌─ Setup ──────────────────────────────┐
│  - Detect which agents changed       │
│  - Set environment (main=prod,       │
│    develop=staging)                   │
│  - Build deployment matrix           │
└──────────────┬───────────────────────┘
               │
               ▼
┌─ Deploy (per agent) ────────────────────────────────┐
│  1. Configure AWS via OIDC (no static credentials)  │
│  2. Create ECR repository (if not exists)           │
│  3. Build ARM64 Docker image                        │
│  4. Push to ECR (:latest + :commit-sha)             │
│  5. Create IAM execution role (if not exists)       │
│  6. Create/Update Bedrock AgentCore runtime         │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─ Integration Tests ─────────────────┐
│  Run test_agent.py against deployed │
│  runtime                            │
└─────────────────────────────────────┘
```

### Trigger Rules

| Event | Branch | Environment | Deploys? |
|-------|--------|-------------|----------|
| Push | `main` | `production` | Yes |
| Push | `develop` | `staging` | Yes |
| PR | any | — | No (tests only) |
| Manual dispatch | — | Choose (dev/staging/prod) | Yes |

### Path-Based Triggers

Only agents with changed files get deployed:
- `staffers_agent_mcp_tools/agent_deployment/**` → deploys staffers
- `votes_agent_mcp_tools/agent_deployment/**` → deploys votes

### Resource Naming Convention

| Resource | Pattern |
|----------|---------|
| ECR Repo | `pbn-agentcore-{agent}-agent_{environment}` |
| IAM Role | `pbn-agentcore-{agent}-agent_{environment}-execution-role` |
| Runtime | `pbn-agentcore-{agent}-agent_{environment}` |

### Manual Deployment (ECR Script)

For quick manual deployments:

```bash
cd votes_agent_mcp_tools/agent_deployment
bash build_and_push_ecr.sh
```

### Terraform (Infrastructure Foundation)

Terraform handles one-time foundational setup:

```bash
# GitHub OIDC for Actions (one-time)
cd infrastructure/terraform/github-oidc
terraform init && terraform apply

# Save the output role_arn as GitHub Secret: AWS_ROLE_ARN
```

### Required GitHub Secrets

| Secret | Description |
|--------|-------------|
| `AWS_ROLE_ARN` | OIDC role for GitHub Actions |
| `staffers_GATEWAY_URL` | MCP Gateway URL |
| `staffers_COGNITO_CLIENT_ID` | Cognito client ID |
| `staffers_COGNITO_CLIENT_SECRET` | Cognito client secret |
| `staffers_COGNITO_TOKEN_URL` | Cognito token URL |
| `votes_GATEWAY_URL` | (same pattern for each agent) |
| `votes_COGNITO_CLIENT_ID` | |
| `votes_COGNITO_CLIENT_SECRET` | |
| `votes_COGNITO_TOKEN_URL` | |

---

## 10. Day 7: Making Your First Change

### Scenario: Update the Votes Agent System Prompt

1. **Edit the instructions file**:
   ```bash
   vim votes_agent_mcp_tools/agent_deployment/orchestrator_instructions.txt
   ```

2. **Test locally**:
   ```bash
   cd votes_agent_mcp_tools/agent_deployment
   source venv/bin/activate
   python main_app.py
   # Test with curl in another terminal
   ```

3. **Commit and push**:
   ```bash
   git checkout -b feature/update-votes-prompt
   git add votes_agent_mcp_tools/agent_deployment/orchestrator_instructions.txt
   git commit -m "Update votes agent system prompt for better bill analysis"
   git push origin feature/update-votes-prompt
   ```

4. **Open a PR** → CI runs tests (no deploy on PR)

5. **Merge to develop** → Auto-deploys to staging

6. **Merge to main** → Auto-deploys to production

### Scenario: Add a New Agent

1. **Copy an existing agent as template**:
   ```bash
   cp -r votes_agent_mcp_tools/ new_agent_mcp_tools/
   ```

2. **Modify key files**:
   - `agent_deployment/main_app.py` — Update agent name
   - `agent_deployment/orchestrator_instructions.txt` — Write new system prompt
   - `agent_deployment/enbloc_mcp_wrapper_v2.py` — Update tool-to-API-path mapping
   - `agent_deployment/.bedrock_agentcore.yaml` — Update agent name and config
   - `gateway/<agent>_gateway_setup.py` — Configure new gateway

3. **Set up the gateway**:
   ```bash
   cd new_agent_mcp_tools/gateway
   python new_agent_gateway_setup.py
   python get_credentials.py  # Save these
   ```

4. **Add to orchestrator** (`orchestrartor_agent/agent_deployment/`):
   - Add new tool function in `pbn_agents.py`
   - Add agent ARN env var
   - Register tool in `main_app.py`
   - Update `orchestrator_instructions.txt`

5. **Add CI/CD support**: Update `.github/workflows/deploy-agents.yml` path filters and matrix

---

## 11. Key Concepts Reference

### Strands Agents SDK

The core framework for building agents. Key concepts:
- **`Agent`**: The main class — combines an LLM model with tools and a system prompt
- **`@tool`**: Decorator to expose Python functions as tools the LLM can call
- **`MCPClient`**: Connects to MCP servers (gateways) to discover and use remote tools
- **`BedrockModel`**: Wraps Amazon Bedrock models for use with Strands
- **`invocation_state`**: Runtime context passed through tool calls (carries session data)

### Bedrock AgentCore

AWS service for hosting and managing AI agents:
- **Runtime**: A deployed agent container (like a Lambda function but for agents)
- **Gateway**: An MCP-compatible proxy that converts REST APIs into MCP tools
- **Gateway Target**: Maps a specific API (via OpenAPI spec) to MCP tools within a gateway

### MCP (Model Context Protocol)

An open protocol for connecting AI models to data sources:
- **Transport**: Streamable HTTP (used here)
- **Tools**: Functions the model can call (mapped from API endpoints)
- **Authentication**: Bearer token via Cognito OAuth2

### Key Design Patterns

1. **Reusable Agent Instances**: Agents are created once at startup and handle multiple queries via `invocation_state`
2. **Payload Wrapping**: `EnblocPayloadTool` transforms simple tool calls into full gateway-compatible payloads
3. **Async All The Way**: Both orchestrator and sub-agents use `async/await` for concurrency
4. **Session Propagation**: User session attributes (UserId, UserToken, Metadata) flow from orchestrator → sub-agent → gateway → backend

---

## 12. Common Tasks Cheat Sheet

### Check Deployed Runtimes

```bash
aws bedrock-agentcore list-agent-runtimes --query 'agentRuntimes[*].{Name:agentRuntimeName,ID:agentRuntimeId,Status:status}' --output table
```

### View Agent Logs

```bash
aws logs tail /aws/bedrock-agentcore/pbn-agentcore-votes-agent_development --follow
```

### Test a Deployed Agent

```bash
cd votes_agent_mcp_tools/agent_deployment
python test_agent.py
```

### Build Docker Image Locally

```bash
cd votes_agent_mcp_tools/agent_deployment
docker buildx build --platform linux/arm64 -t pbn-votes-agent --load .
```

### Push to ECR Manually

```bash
cd votes_agent_mcp_tools/agent_deployment
bash build_and_push_ecr.sh
```

### Get Gateway Credentials

```bash
cd votes_agent_mcp_tools/gateway
python get_credentials.py
```

### Check ECR Images

```bash
aws ecr describe-images --repository-name pbn-agentcore-votes-agent_development --query 'imageDetails[*].{Tags:imageTags,Pushed:imagePushedAt}' --output table
```

### Manual Workflow Trigger

Go to **GitHub Actions** → **Deploy Bedrock AgentCore Agents** → **Run workflow** → Select environment and agent.

---

## 13. Troubleshooting

### "Authentication failed" when starting agent locally

- Verify `.env` has correct `CLIENT_ID`, `CLIENT_SECRET`, and `TOKEN_URL`
- Tokens expire — if the agent has been running a long time, restart it
- Check that Cognito User Pool and App Client still exist

### "Cannot connect to MCP gateway"

- Verify `GATEWAY_URL` ends with `/mcp`
- Check that the gateway is active: `aws bedrock-agentcore list-gateways`
- Ensure the gateway target exists and is properly configured

### Docker build fails on ARM64

- Make sure Docker Buildx is installed: `docker buildx version`
- For M1/M2 Macs, ARM64 builds are native
- For x86 machines, ensure QEMU emulation is set up: `docker run --rm --privileged multiarch/qemu-user-static --reset -p yes`

### "PermissionError: [Errno 13]" in Docker

```bash
chmod 644 *.py
```

Then rebuild the image.

### Agent timeout (300s)

- Agent invocations have a 300-second timeout
- If the backend API is slow, the agent may time out
- Check backend health: `curl https://<api-endpoint>/health`

### "anyOf" errors when creating gateway target

- The OpenAPI spec needs manual fixing — replace all `anyOf` with simple types
- See the [OpenAPI Spec Compatibility](#gateway--mcp-protocol-deep-dive) section

### AgentCore runtime fails to start

1. Check CloudWatch logs: `aws logs tail /aws/bedrock-agentcore/<runtime-name> --follow`
2. Verify env vars are set (especially GATEWAY_URL, CLIENT_ID, CLIENT_SECRET, TOKEN_URL)
3. Ensure the IAM execution role can pull from ECR
4. Check that the Docker image was built for `linux/arm64`

---

## 14. Who to Ask

| Topic | Contact |
|-------|---------|
| AWS access & permissions | DevOps / Infrastructure team |
| Agent logic & prompts | ML Engineering team |
| Backend API endpoints | Backend Engineering team |
| Gateway & MCP setup | ML Engineering team |
| CI/CD pipeline | DevOps / ML Engineering team |
| Cognito credentials | DevOps / Infrastructure team |

---

## Glossary

| Term | Definition |
|------|-----------|
| **AgentCore** | AWS Bedrock service for deploying and managing AI agent runtimes |
| **MCP** | Model Context Protocol — open standard for connecting AI models to tools/data |
| **Strands** | AWS SDK for building AI agents with tool use and multi-turn conversations |
| **Gateway** | MCP-compatible proxy that converts REST APIs into MCP tools |
| **Gateway Target** | A specific API mapping within a gateway (defined by OpenAPI spec) |
| **Cognito** | AWS identity service used for OAuth2 authentication between agents and gateways |
| **EnblocPayloadTool** | Custom wrapper that transforms Strands tool calls into backend-compatible payloads |
| **invocation_state** | Runtime context passed through the agent chain (carries session, user, and event data) |
| **Text2SQL** | Pattern where an LLM converts natural language to SQL queries |
| **ARM64** | Processor architecture required by Bedrock AgentCore (Graviton) |
