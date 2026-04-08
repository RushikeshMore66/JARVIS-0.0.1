from urllib import response
from orchestrator.graph import build_graph

import asyncio

from voice.wake_word import listen_for_wake_word
from voice.stt import listen_command
from voice.tts import speak

from orchestrator.graph import build_graph


async def process_input(graph, user_input):
    result = graph.invoke({"input": user_input})
    response = result["output"]

    print(f"🤖 JARVIS: {response}")

    speak(response)


async def main():
    print("🧠 JARVIS is online...")

    graph = build_graph()

    while True:
        try:
            # Blocking wake word (we improve later)
            listen_for_wake_word()

            user_input = listen_command()

            if not user_input.strip():
                continue

            print(f"🧑 You: {user_input}")

            # Run in async task
            asyncio.create_task(process_input(graph, user_input))

        except KeyboardInterrupt:
            print("\n👋 Shutting down JARVIS...")
            break


if __name__ == "__main__":
    asyncio.run(main())