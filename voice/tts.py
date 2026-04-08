from elevenlabs import play, generate
import os
from dotenv import load_dotenv

load_dotenv()

ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")

def speak(text: str):
    print(f"🔊 JARVIS: {text}")

    audio = generate(
        text=text,
        voice="Brian",
        model="eleven_multilingual_v2",
        api_key=ELEVEN_API_KEY
    )

    play(audio)
    

    