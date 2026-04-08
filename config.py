import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


def _env_bool(name: str, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(frozen=True)
class Settings:
    local_model: str = os.getenv("LOCAL_MODEL", "llama3.2:latest")
    local_vision_model: str = os.getenv("LOCAL_VISION_MODEL", "llava:latest")
    cloud_model: str = os.getenv("CLOUD_MODEL", "gemini-1.5-flash")
    wake_word: str = os.getenv("WAKE_WORD", "jarvis")
    sample_rate: int = int(os.getenv("SAMPLE_RATE", "16000"))
    chunk_size: int = int(os.getenv("CHUNK_SIZE", "1024"))
    use_cloud_fallback: bool = _env_bool("USE_CLOUD_FALLBACK", True)
    allow_dangerous_actions: bool = _env_bool("ALLOW_DANGEROUS_ACTIONS", False)
    enable_gesture_controller: bool = _env_bool("ENABLE_GESTURE_CONTROLLER", False)
    enable_overlay_ui: bool = _env_bool("ENABLE_OVERLAY_UI", False)
    enable_background_agents: bool = _env_bool("ENABLE_BACKGROUND_AGENTS", False)
    enable_mcp: bool = _env_bool("ENABLE_MCP", True)


SETTINGS = Settings()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY", "")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", ELEVEN_API_KEY)
PICOVOICE_ACCESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY", "")
