from clicker import AutoClicker
from ui import ClickerUI


def main() -> None:
    clicker = AutoClicker()
    ui = ClickerUI(clicker)
    ui.run()


if __name__ == "__main__":
    main()
