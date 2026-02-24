## MCP Server Development

Reference: `taches-cc-resources/skills/create-mcp-servers/SKILL.md`

Build Model Context Protocol servers that expose tools, resources, and prompts to Claude and other LLM clients.

**Python MCP Server (using mcp SDK):**

```python
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

server = Server("my-backend-tools")

@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="query-database",
            description="Execute a read-only SQL query against the application database",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL SELECT query to execute"},
                },
                "required": ["query"],
            },
        ),
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "query-database":
        if not arguments["query"].strip().upper().startswith("SELECT"):
            return [TextContent(type="text", text="Error: Only SELECT queries are allowed")]
        result = await db.fetch(arguments["query"])
        return [TextContent(type="text", text=str(result))]

async def main():
    async with mcp.server.stdio.stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())
```

**TypeScript MCP Server:**

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new Server({ name: "my-backend-tools", version: "1.0.0" }, {
  capabilities: { tools: {} },
});

server.setRequestHandler("tools/list", async () => ({
  tools: [{
    name: "health-check",
    description: "Check the health of backend services",
    inputSchema: { type: "object", properties: { service: { type: "string" } }, required: ["service"] },
  }],
}));

server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "health-check") {
    const response = await fetch(`http://${request.params.arguments.service}/health`);
    return { content: [{ type: "text", text: JSON.stringify(await response.json()) }] };
  }
});

const transport = new StdioServerTransport();
await server.connect(transport);
```
