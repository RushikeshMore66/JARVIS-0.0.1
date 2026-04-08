import whisper
import sounddevice as sd
import numpy as np
import queue

q=queue.Queue()

model=whisper.load_model("base")

def audio_callback(indata, frames, time, status):
    q.put(indata.copy())

def listen_once(duration=5,samplerate=16000):
    print("🎤 Listening...")
    
    recording=sd.rec(int(duration*samplerate),
                        samplerate=samplerate,
                        dtype="float32",
                        channels=1 )
    sd.wait()
    
    audio = recording.flatten()
    result = model.transcribe(audio)
    return result["text"]