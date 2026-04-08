import requests

def call_mcp_tool(tool: str, data: dict):
    # Example local MCP server endpoint
    url = f"http://localhost:3001/mcp/{tool}"

    try:
        response = requests.post(url, json=data)
        return response.json()
    except Exception as e:
        return {"error": str(e)}