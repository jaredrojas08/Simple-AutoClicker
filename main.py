from clicker import AutoClicker
from hotkeys import HotkeyManager
from ui import ClickerUI


def main() -> None:
    clicker = AutoClicker()
    ui = ClickerUI(clicker)

    hotkeys = HotkeyManager(
        {
            "<f6>": ui.safe_start,
            "<f7>": ui.safe_stop,
            "<f8>": ui.safe_toggle,
        }
    )
    hotkeys.start()

    try:
        ui.run()
    finally:
        hotkeys.stop()
        clicker.stop()


if __name__ == "__main__":
    main()
