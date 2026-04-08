from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class GestureEvent:
    name: str
    cursor_position: Optional[Tuple[int, int]] = None


class GestureController:
    """Feature-flag ready gesture controller scaffold."""

    def __init__(self) -> None:
        self.enabled = False

    def start(self) -> None:
        self.enabled = True

    def stop(self) -> None:
        self.enabled = False

    def poll_event(self) -> Optional[GestureEvent]:
        if not self.enabled:
            return None
        # Advanced OpenCV/MediaPipe loop can be mounted here.
        return None
