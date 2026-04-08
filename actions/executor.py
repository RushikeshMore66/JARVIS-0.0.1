from datetime import datetime
from pathlib import Path
from config import SETTINGS
try:
    from interpreter import interpreter
except Exception:  # pragma: no cover - dependency/runtime availability
    interpreter = None

if interpreter is not None:
    interpreter.auto_run = True
    interpreter.system_message = """
You are JARVIS, an AI system controller.
Execute safe and efficient system commands.
Avoid destructive operations.
Be precise.
"""

_DANGEROUS_PATTERNS = [
    "rm -rf",
    "format c:",
    "shutdown /s",
    "del /f /q",
    "mkfs",
]


def _is_dangerous(prompt: str) -> bool:
    text = (prompt or "").lower()
    return any(pattern in text for pattern in _DANGEROUS_PATTERNS)


def evaluate_action_safety(prompt: str) -> bool:
    return not _is_dangerous(prompt)


def _log_action(prompt: str, result: str) -> None:
    Path("logs").mkdir(exist_ok=True)
    with open("logs/actions.log", "a", encoding="utf-8") as fh:
        ts = datetime.utcnow().isoformat()
        fh.write(f"{ts}\t{prompt}\t{result}\n")


def run_action(prompt: str):
    print(f"⚡ Executing: {prompt}")
    if _is_dangerous(prompt) and not SETTINGS.allow_dangerous_actions:
        result = "Blocked by safety policy: potentially dangerous command."
        _log_action(prompt, result)
        return result
    if interpreter is None:
        result = "Open Interpreter is not installed."
        _log_action(prompt, result)
        return result
    try:
        interpreter.chat(prompt)
        result = "✅ Task executed successfully."
        _log_action(prompt, result)
        return result
    except Exception as e:
        result = f"Error: {str(e)}"
        _log_action(prompt, result)
        return result