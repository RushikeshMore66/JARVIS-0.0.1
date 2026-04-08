from __future__ import annotations

from actions.mcp_clients import call_mcp_tool


def mcp_filesystem(payload: dict) -> dict:
    return call_mcp_tool("filesystem", payload)


def mcp_google_calendar(payload: dict) -> dict:
    return call_mcp_tool("google-calendar", payload)


def mcp_email(payload: dict) -> dict:
    return call_mcp_tool("email", payload)
