# 🧠 JARVIS OS – Local-First AI Desktop Agent

> A fully local-first, multimodal AI assistant that can see your screen, hear your voice, and control your computer — with optional cloud intelligence when needed.
> 

---

## 🚀 Vision

JARVIS OS is not a chatbot.

It is a **Personal AI Operating System Layer** that sits on top of your machine and enables:

- 🎤 Natural voice interaction (real-time)
- 👁️ Screen understanding (vision)
- ⚡ Direct system control (keyboard, mouse, apps)
- 🧠 Memory & contextual awareness
- 🌐 Optional cloud intelligence (only when required)

---

## 🧩 Core Philosophy

```bash
LOCAL-FIRST → PRIVATE, FAST
CLOUD-OPTIONAL → POWERFUL, SCALABLE
```

---

## 🏗️ Architecture Overview

```
JARVIS/
├── brain/              # LLM routing + reasoning
├── voice/              # STT + TTS + wake word
├── vision/             # screen capture + analysis
├── actions/            # OS control + tool execution
├── memory/             # short-term + long-term memory
├── orchestrator/       # LangGraph workflow engine
```

---

## 🧠 Tech Stack

### 🧠 Agent Framework

- LangGraph (stateful orchestration)
- LangChain (tools + integrations)

### 🧠 LLM Layer

- Local: Ollama (LLaMA 3.2 Vision)
- Cloud (optional): Gemini 1.5 Pro

### 🎤 Voice

- STT: Whisper (local)
- Wake Word: Porcupine
- TTS: Cartesia / ElevenLabs

### 👁️ Vision

- PyAutoGUI (screenshots)
- PIL / OpenCV

### ⚡ Execution Layer

- Open Interpreter (system control via Python)

### 🔌 Tool Integration

- Model Context Protocol (MCP)

### 🧠 Memory

- Chroma / FAISS (vector DB)

---

## 🔁 System Flow

```
Wake Word
   ↓
Speech-to-Text (Whisper)
   ↓
Intent Classification
   ↓
Router (Local vs Cloud)
   ↓
Planner (LangGraph)
   ↓
Tool Execution (Interpreter + MCP)
   ↓
Memory Update
   ↓
Text-to-Speech Response
```

---

## 🔥 Features

- ✅ Fully local voice interaction
- ✅ Screen-aware AI (vision enabled)
- ✅ Autonomous task execution
- ✅ Multi-step planning (agent workflows)
- ✅ Hybrid intelligence (local + cloud)
- ✅ Persistent memory (context-aware)

---

## ⚙️ Installation

### 1. Clone Repo

```bash
git clone https://github.com/yourusername/jarvis-os.git
cd jarvis-os
```

### 2. Create Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Setup Local LLM (Ollama)

Install Ollama:

```bash
ollama run llama3.2-vision
```

---

## ⚡ Install Open Interpreter

```bash
pip install open-interpreter
```

---

## 🎤 Run JARVIS (Phase 1)

```bash
python main.py
```

---

## 🧪 Current Status

| Module | Status |
| --- | --- |
| Voice Input | 🚧 In Progress |
| Brain | 🚧 In Progress |
| Vision | ⏳ Planned |
| Actions | ⏳ Planned |
| Memory | ⏳ Planned |

---

## 🧠 Roadmap

### Phase 1

- Voice → Command loop
- Basic LLM response

### Phase 2

- LangGraph orchestration
- Tool execution (Interpreter)

### Phase 3

- Vision (screen awareness)

### Phase 4

- MCP integrations (apps)

### Phase 5

- Memory system (RAG)

---

## ⚠️ Safety

JARVIS has system-level access.

- Commands are sandboxed
- Critical actions require confirmation (future)
- Logs are maintained

---

## 🤝 Contributing

PRs are welcome.

This is an experimental AI OS project.

---

## 📜 License
Sarthi AI Labs

---

## 🧠 Author

Mr.Rushikesh Sunil More

---

## ⭐ Final Note

This is not just an assistant.

This is the beginning of a **personal AI operating system**.
