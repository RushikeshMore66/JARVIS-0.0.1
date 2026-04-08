from orchestrator.graph import build_graph
from voice.stt import listen_once

def main():
    print("🧠 JARVIS is online...")
    graph = build_graph()

    while True:
        try:
            user_input = listen_once()

            if not user_input.strip():
                continue

            print(f"👤 You said: {user_input}")

            result = graph.invoke({"input":user_input})
            print(f"🤖 Jarvis: {result['output']}")

        except KeyboardInterrupt:
            print("🤖 Jarvis: Goodbye!")
            break

if __name__ == "__main__":
    main()
