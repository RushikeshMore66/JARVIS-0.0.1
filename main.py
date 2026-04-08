import asyncio
from contextlib import suppress

from config import SETTINGS
from background_agents import BackgroundAgentPool
from voice.wake_word import listen_for_wake_word
from voice.stt import listen_command
from voice.tts import speak
from orchestrator.graph import build_graph

if SETTINGS.enable_overlay_ui:
    from ui_overlay import JarvisOverlay
else:
    JarvisOverlay = None

if SETTINGS.enable_gesture_controller:
    from gesture_controller import GestureController
else:
    GestureController = None


async def process_input(graph, user_input):
    result = await asyncio.to_thread(graph.invoke, {"input": user_input})
    response = result["output"]

    print(f"🤖 JARVIS: {response}")
    await asyncio.to_thread(speak, response)


async def main():
    print("🧠 JARVIS is online...")
    graph = build_graph()
    running_task: asyncio.Task | None = None
    agents = BackgroundAgentPool() if SETTINGS.enable_background_agents else None
    overlay = JarvisOverlay() if JarvisOverlay else None
    gestures = GestureController() if GestureController else None
    if overlay:
        overlay.show()
    if gestures:
        gestures.start()

    while True:
        try:
            await asyncio.to_thread(listen_for_wake_word)
            if overlay:
                overlay.update(listening=True)
            user_input = await asyncio.to_thread(listen_command)
            if overlay:
                overlay.update(listening=False, active_task=user_input)

            if not user_input.strip():
                continue

            print(f"🧑 You: {user_input}")
            if user_input.lower().strip() in {"stop", "cancel", "abort"}:
                if running_task and not running_task.done():
                    running_task.cancel()
                    with suppress(asyncio.CancelledError):
                        await running_task
                    print("🛑 Active task cancelled.")
                continue

            if running_task and not running_task.done():
                print("⏳ Previous task still running; please say 'cancel' to interrupt.")
                continue

            running_task = asyncio.create_task(process_input(graph, user_input))
            running_task.add_done_callback(
                lambda t: print(f"⚠️ Task error: {t.exception()}") if t.exception() else None
            )

        except KeyboardInterrupt:
            print("\n👋 Shutting down JARVIS...")
            if running_task and not running_task.done():
                running_task.cancel()
                with suppress(asyncio.CancelledError):
                    await running_task
            break
        finally:
            if overlay:
                overlay.update(active_task="")
    if gestures:
        gestures.stop()
    if overlay:
        overlay.hide()
    if agents:
        await agents.shutdown()


if __name__ == "__main__":
    asyncio.run(main())