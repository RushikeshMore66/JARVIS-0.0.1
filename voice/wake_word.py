from pvporcupine import Porcupine
import pvporcupine
import pyaudio
import struct

Porcupine = pvporcupine.create(keywords=["jarvis"])

pa = pyaudio.PyAudio()

audio_stream = pa.open(
    rate=Porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=Porcupine.frame_length
)

def listen_for_wake_word():
    print("Waiting for wake word 'Jarvis'...")
    while True:
        pcm = audio_stream.read(Porcupine.frame_length)
        pcm = struct.unpack_from("h"*Porcupine.frame_length, pcm)
        
        keyword_index = Porcupine.process(pcm)
        
        if keyword_index >= 0:
            print("Wake word detected!")
            return

        