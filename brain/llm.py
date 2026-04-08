from __future__ import annotations

from typing import Any

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except Exception:  # pragma: no cover - dependency/runtime availability
    ChatGoogleGenerativeAI = None

try:
    from langchain_ollama import ChatOllama
except Exception:  # pragma: no cover - dependency/runtime availability
    ChatOllama = None

from config import GEMINI_API_KEY, SETTINGS

SYSTEM_PROMPT = """
You are JARVIS, a highly intelligent AI assistant.

Personality:
- Calm, confident, slightly witty
- Speak like a helpful butler (Tony Stark style)
- Keep responses short and natural
- Do NOT sound robotic
- Be conversational

Examples:
User: hey
JARVIS: I'm here. What do you need?

User: how are you
JARVIS: Fully operational, as always.

User: hello jarvis
JARVIS: Hello. How can I assist?
"""


def _build_messages(prompt: str) -> list[tuple[str, str]]:
    return [("system", SYSTEM_PROMPT), ("human", prompt)]


def _safe_content(result: Any) -> str:
    content = getattr(result, "content", "")
    if isinstance(content, list):
        return " ".join(str(part) for part in content)
    return str(content)


def route_llm(task: str) -> str:
    text = (task or "").lower()
    if len(task) > 1500:
        return "cloud"
    if any(word in text for word in ["search", "internet", "web", "latest", "news"]):
        return "cloud"
    if any(word in text for word in ["analyze", "reason", "architect", "multi-step"]):
        return "cloud"
    return "local"


def ask_local_llm(prompt: str) -> str:
    if ChatOllama is None:
        return "Local model unavailable: langchain-ollama is not installed."
    try:
        local_llm = ChatOllama(model=SETTINGS.local_model, temperature=0.2)
        response = local_llm.invoke(_build_messages(prompt))
        return _safe_content(response)
    except Exception as exc:
        if SETTINGS.use_cloud_fallback:
            return ask_cloud_llm(prompt)
        return f"Local model error: {exc}"


def ask_cloud_llm(prompt: str) -> str:
    if ChatGoogleGenerativeAI is None:
        return "Cloud model unavailable: langchain-google-genai is not installed."
    if not GEMINI_API_KEY:
        return "Cloud model unavailable: GEMINI_API_KEY is not set."
    try:
        cloud_llm = ChatGoogleGenerativeAI(
            model=SETTINGS.cloud_model,
            google_api_key=GEMINI_API_KEY,
        )
        response = cloud_llm.invoke(_build_messages(prompt))
        return _safe_content(response)
    except Exception as exc:
        return f"Cloud model error: {exc}"


def ask_llm(prompt: str) -> str:
    provider = route_llm(prompt)
    if provider == "cloud":
        return ask_cloud_llm(prompt)
    return ask_local_llm(prompt)


def analyze_screen(image_path: str, user_prompt: str) -> str:
    prompt = (
        "You are analyzing a user screenshot.\n"
        f"Image path: {image_path}\n"
        f"User request: {user_prompt}\n"
        "Provide concise actionable insights."
    )
    return ask_llm(prompt)