import threading
import time

from pynput.mouse import Button, Controller


class AutoClicker:
    def __init__(self, interval_ms: int = 100):
        self._mouse = Controller()
        self._interval_ms = max(1, interval_ms)
        self._button: Button = Button.left
        self._running = False
        self._thread: threading.Thread | None = None
        self._lock = threading.Lock()

    @property
    def running(self) -> bool:
        return self._running

    def set_interval(self, ms: int) -> None:
        self._interval_ms = max(1, int(ms))

    def set_button(self, name: str) -> None:
        self._button = Button.right if name.strip().lower() == "right" else Button.left

    def start(self) -> None:
        with self._lock:
            if self._running:
                return
            self._running = True
            self._thread = threading.Thread(target=self._loop, daemon=True)
            self._thread.start()

    def stop(self) -> None:
        self._running = False

    def _loop(self) -> None:
        while self._running:
            self._mouse.click(self._button)
            time.sleep(self._interval_ms / 1000.0)
