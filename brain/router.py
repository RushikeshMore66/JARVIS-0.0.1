def route(prompt: str):
    prompt = prompt.lower()

    # Greeting detection
    if any(word in prompt for word in ["hey", "hello", "hi", "jarvis"]):
        return "chat"

    if any(word in prompt for word in ["plan", "schedule"]):
        return "autonomous"

    if any(word in prompt for word in ["open", "run", "execute"]):
        return "action"

    if any(word in prompt for word in ["screen", "see"]):
        return "vision"

    return "local"