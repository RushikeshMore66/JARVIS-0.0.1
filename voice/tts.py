from elevenlabs import play, generate
from config import ELEVENLABS_API_KEY

def speak(text: str):
    print(f"🔊 JARVIS: {text}")
    if not ELEVENLABS_API_KEY:
        return

    try:
        audio = generate(
            text=text,
            voice="Brian",
            model="eleven_multilingual_v2",
            api_key=ELEVENLABS_API_KEY,
        )
        play(audio)
    except Exception as exc:
        print(f"⚠️ TTS unavailable: {exc}")
