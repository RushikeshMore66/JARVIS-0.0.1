import whisper
import sounddevice as sd

_model = None


def _get_model():
    global _model
    if _model is None:
        _model = whisper.load_model("base")
    return _model


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

    model = _get_model()
    result = model.transcribe(audio)

    return result.get("text", "").strip()