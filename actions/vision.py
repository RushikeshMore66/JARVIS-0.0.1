from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

import pyautogui


def capture_screen(
    region: Optional[Tuple[int, int, int, int]] = None,
    output_dir: str = "captures",
) -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    filename = f"screen_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.png"
    path = str(Path(output_dir) / filename)
    shot = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()
    shot.save(path)
    return path