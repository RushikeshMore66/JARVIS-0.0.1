from langchain_ollama import OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from config import LOCAL_MODEL, USE_CLOUD, GEMINI_API_KEY

# Initialize LLMs
local_llm = OllamaLLM(model=LOCAL_MODEL)
cloud_llm = None

if USE_CLOUD and GEMINI_API_KEY:
    cloud_llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        google_api_key=GEMINI_API_KEY
    )

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

def ask_local_llm(prompt: str):
    """Local LLM logic (can fallback to cloud if enabled)"""
    if USE_CLOUD and cloud_llm:
        return ask_cloud_llm(prompt)
        
    full_prompt = f"""
{SYSTEM_PROMPT}

User: {prompt}
JARVIS:
"""
    return local_llm.invoke(full_prompt)

def ask_cloud_llm(prompt: str):
    """Smart response using Gemini"""
    if not cloud_llm:
        return ask_local_llm(prompt)
        
    messages = [
        ("system", SYSTEM_PROMPT),
        ("human", prompt),
    ]
    response = cloud_llm.invoke(messages)
    return response.content

def analyze_screen(image_path: str, prompt: str):
    """Vision analysis (implemented later or via cloud)"""
    # TODO: Implement vision logic
    return "I'm looking at the screen, but my eyes aren't fully configured yet."