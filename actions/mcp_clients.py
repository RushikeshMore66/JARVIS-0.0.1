import requests
from config import SETTINGS

def call_mcp_tool(tool: str, data: dict):
    if not SETTINGS.enable_mcp:
        return {"error": "MCP integration is disabled by configuration."}
    # Example local MCP server endpoint
    url = f"http://localhost:3001/mcp/{tool}"

    try:
        response = requests.post(url, json=data, timeout=20)
        return response.json()
    except Exception as e:
        return {"error": str(e)}