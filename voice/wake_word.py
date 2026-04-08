import pvporcupine
import pyaudio
import struct
from config import PICOVOICE_ACCESS_KEY, SETTINGS

_porcupine = None
_audio_stream = None
_audio = None
HAS_PORCUPINE = False


def _init_wake_word() -> None:
    global _porcupine, _audio_stream, _audio, HAS_PORCUPINE
    if HAS_PORCUPINE:
        return
    if not PICOVOICE_ACCESS_KEY:
        print("⚠️ Wake word detection disabled: missing PICOVOICE_ACCESS_KEY")
        return
    try:
        _porcupine = pvporcupine.create(
            access_key=PICOVOICE_ACCESS_KEY,
            keywords=[SETTINGS.wake_word],
        )
        _audio = pyaudio.PyAudio()
        _audio_stream = _audio.open(
            rate=_porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=_porcupine.frame_length,
        )
        HAS_PORCUPINE = True
    except Exception as exc:
        print(f"⚠️ Wake word detection disabled: {exc}")
        HAS_PORCUPINE = False

def listen_for_wake_word():
    _init_wake_word()
    if not HAS_PORCUPINE:
        print("Skipping wake word (disabled)...")
        return

    print("Waiting for wake word 'Jarvis'...")
    while True:
        try:
            pcm = _audio_stream.read(_porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * _porcupine.frame_length, pcm)
            keyword_index = _porcupine.process(pcm)
            if keyword_index >= 0:
                print("Wake word detected!")
                return
        except Exception as exc:
            print(f"⚠️ Wake word listener error: {exc}")
            return