from gesture_controller import GestureController
from ui_overlay import JarvisOverlay


def test_gesture_controller_lifecycle():
    controller = GestureController()
    controller.start()
    assert controller.enabled is True
    controller.stop()
    assert controller.enabled is False


def test_overlay_state_update():
    overlay = JarvisOverlay()
    overlay.update(listening=True, active_task="test", response="ok")
    assert overlay.state.listening is True
    assert overlay.state.active_task == "test"
    assert overlay.state.response == "ok"
