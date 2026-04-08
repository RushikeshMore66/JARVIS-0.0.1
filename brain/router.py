from __future__ import annotations


def classify_intent(prompt: str) -> str:
    text = (prompt or "").lower()
    if any(word in text for word in ["stop", "cancel", "abort"]):
        return "interrupt"
    if any(word in text for word in ["plan", "schedule", "multi-step", "autonomous"]):
        return "autonomous"
    if any(word in text for word in ["open", "run", "execute", "launch"]):
        return "action"
    if any(word in text for word in ["look at this", "analyze screen", "screen", "see"]):
        return "vision"
    if any(word in text for word in ["cloud", "internet", "web", "online"]):
        return "cloud"
    return "chat"


def route(prompt: str) -> str:
    intent = classify_intent(prompt)
    if intent == "interrupt":
        return "chat"
    return intent