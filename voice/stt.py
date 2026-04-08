import whisper
import sounddevice as sd
import numpy as np

model = whisper.load_model("base")


def listen_command(duration=4, samplerate=16000):
    print("🎤 Listening for command...")

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype='float32'
    )

    sd.wait()

    audio = recording.flatten()

    result = model.transcribe(audio)

    return result["text"]