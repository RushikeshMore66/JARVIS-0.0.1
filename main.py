from urllib import response
from orchestrator.graph import build_graph

from voice.stt import listen_once
from voice.tts import speak
from voice.wake_word import listen_for_wake_word

def main():
    print("🧠 JARVIS is online...")
    graph = build_graph()

    while True:
        try:
            listen_for_wake_word()
            
            user_input = listen_once()

            if not user_input.strip():
                continue

            print(f"👤 You said: {user_input}")

            result = graph.invoke({
                "input":user_input
            })

            response=result["output"]

            speak(response)

        except KeyboardInterrupt:
            print("🤖 Jarvis: Goodbye!")
            break

if __name__ == "__main__":
    main()
