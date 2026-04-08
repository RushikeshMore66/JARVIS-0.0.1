from pvporcupine import Porcupine
import pvporcupine
import pyaudio
import struct
from config import PICOVOICE_ACCESS_KEY

try:
    Porcupine = pvporcupine.create(
        access_key=PICOVOICE_ACCESS_KEY,
        keywords=["jarvis"]
    )
    
    pa = pyaudio.PyAudio()
    
    audio_stream = pa.open(
        rate=Porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=Porcupine.frame_length
    )
    HAS_PORCUPINE = True
except Exception as e:
    print(f"⚠️ Wake word detection disabled: {e}")
    HAS_PORCUPINE = False

def listen_for_wake_word():
    if not HAS_PORCUPINE:
        print("Skipping wake word (disabled)...")
        return
        
    print("Waiting for wake word 'Jarvis'...")
    while True:
        pcm = audio_stream.read(Porcupine.frame_length)
        pcm = struct.unpack_from("h"*Porcupine.frame_length, pcm)
        
        keyword_index = Porcupine.process(pcm)
        
        if keyword_index >= 0:
            print("Wake word detected!")
            return

        