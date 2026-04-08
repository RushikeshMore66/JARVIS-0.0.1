# JARVIS OS - Local-First AI Desktop Assistant

Production-oriented desktop assistant with voice, vision, local LLM default routing, cloud fallback, action execution, and memory.

## Architecture

- `brain/`: routing, planning, and LLM provider selection
- `voice/`: wake word, STT, TTS
- `actions/`: system actions, MCP adapters, vision capture
- `memory/`: vector memory storage/retrieval
- `orchestrator/`: workflow graph + execution manager

Main flow:

`Wake Word -> STT -> Intent -> Router -> Planner -> Action -> Response`

## Prerequisites

- Python `3.11+`
- Windows audio dependencies for `pyaudio` and `sounddevice`
- Optional but recommended:
  - Ollama running locally for local model usage
  - Gemini API key for cloud fallback
  - Picovoice key for wake word
  - ElevenLabs key for TTS

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Fill `.env` values as needed.

## Run

```bash
python main.py
```

## Test

```bash
pytest
```

## Safety

- Action layer blocks dangerous commands by default.
- Set `ALLOW_DANGEROUS_ACTIONS=true` only in controlled environments.
- Action execution logs are written to `logs/actions.log`.
