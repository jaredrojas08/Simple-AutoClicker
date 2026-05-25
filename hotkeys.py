from typing import Callable

from pynput import keyboard


class HotkeyManager:
    def __init__(self, bindings: dict[str, Callable[[], None]]):
        self._listener = keyboard.GlobalHotKeys(bindings)

    def start(self) -> None:
        self._listener.start()

    def stop(self) -> None:
        self._listener.stop()
