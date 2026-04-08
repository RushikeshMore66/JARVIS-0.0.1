from __future__ import annotations

from dataclasses import dataclass


@dataclass
class OverlayState:
    listening: bool = False
    active_task: str = ""
    response: str = ""


class JarvisOverlay:
    """Minimal overlay facade; UI backend can be wired later."""

    def __init__(self) -> None:
        self.state = OverlayState()
        self.visible = False

    def show(self) -> None:
        self.visible = True

    def hide(self) -> None:
        self.visible = False

    def update(self, *, listening: bool | None = None, active_task: str | None = None, response: str | None = None) -> None:
        if listening is not None:
            self.state.listening = listening
        if active_task is not None:
            self.state.active_task = active_task
        if response is not None:
            self.state.response = response
