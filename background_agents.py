from __future__ import annotations

import asyncio
from collections.abc import Callable, Awaitable


class BackgroundAgentPool:
    """Small async worker pool for optional background tasks."""

    def __init__(self) -> None:
        self._tasks: set[asyncio.Task] = set()

    def submit(self, coro_factory: Callable[[], Awaitable[None]]) -> None:
        task = asyncio.create_task(coro_factory())
        self._tasks.add(task)
        task.add_done_callback(self._tasks.discard)

    async def shutdown(self) -> None:
        for task in list(self._tasks):
            task.cancel()
        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)
