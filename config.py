import os
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

LOCAL_MODEL = "llama3.2:latest"
USE_CLOUD = True

WAKE_WORD = "jarvis"

SAMPLE_RATE = 16000
CHUNK_SIZE = 1024
