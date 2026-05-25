import tkinter as tk
from tkinter import ttk

from clicker import AutoClicker


class ClickerUI:
    def __init__(self, clicker: AutoClicker):
        self.clicker = clicker
        self.root = tk.Tk()
        self.root.title("Simple AutoClicker")
        self.root.geometry("360x260")
        self.root.resizable(False, False)

        self.interval_var = tk.StringVar(value="100")
        self.button_var = tk.StringVar(value="Left")
        self.cps_var = tk.StringVar()
        self.status_var = tk.StringVar(value="Status: Stopped")

        self._build()
        self.interval_var.trace_add("write", self._on_interval_change)
        self._refresh_cps()

        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build(self) -> None:
        ttk.Label(self.root, text="Click Interval (ms):").grid(
            row=0, column=0, sticky="w", padx=12, pady=6
        )
        ttk.Entry(self.root, textvariable=self.interval_var, width=10).grid(
            row=0, column=1, sticky="w", padx=12, pady=6
        )

        ttk.Label(self.root, text="Click Button:").grid(
            row=1, column=0, sticky="w", padx=12, pady=6
        )
        ttk.Combobox(
            self.root,
            textvariable=self.button_var,
            values=["Left", "Right"],
            state="readonly",
            width=8,
        ).grid(row=1, column=1, sticky="w", padx=12, pady=6)
        self.button_var.trace_add("write", self._on_button_change)

        ttk.Label(self.root, textvariable=self.cps_var, foreground="#555").grid(
            row=2, column=0, columnspan=2, padx=12, pady=2
        )

        ttk.Button(self.root, text="Start", command=self._on_start).grid(
            row=3, column=0, padx=12, pady=6
        )
        ttk.Button(self.root, text="Stop", command=self._on_stop).grid(
            row=3, column=1, padx=12, pady=6
        )

        ttk.Label(self.root, textvariable=self.status_var).grid(
            row=4, column=0, columnspan=2, padx=12, pady=6
        )

        ttk.Separator(self.root, orient="horizontal").grid(
            row=5, column=0, columnspan=2, sticky="ew", padx=12, pady=4
        )
        ttk.Label(
            self.root,
            text="Hotkeys:  F6 Start  ·  F7 Stop  ·  F8 Toggle",
            foreground="#555",
        ).grid(row=6, column=0, columnspan=2, padx=12, pady=4)

    def _interval_ms(self) -> int:
        try:
            return max(1, int(self.interval_var.get()))
        except ValueError:
            return 100

    def _refresh_cps(self) -> None:
        cps = 1000.0 / self._interval_ms()
        self.cps_var.set(f"≈ {cps:.1f} clicks / sec")

    def _on_interval_change(self, *_args) -> None:
        self._refresh_cps()

    def _on_button_change(self, *_args) -> None:
        self.clicker.set_button(self.button_var.get())

    def _on_start(self) -> None:
        interval = self._interval_ms()
        self.interval_var.set(str(interval))
        self.clicker.set_interval(interval)
        self.clicker.set_button(self.button_var.get())
        self.clicker.start()
        self.status_var.set("Status: Running")

    def _on_stop(self) -> None:
        self.clicker.stop()
        self.status_var.set("Status: Stopped")

    def _on_toggle(self) -> None:
        if self.clicker.running:
            self._on_stop()
        else:
            self._on_start()

    def _on_close(self) -> None:
        self.clicker.stop()
        self.root.destroy()

    def safe_start(self) -> None:
        self.root.after(0, self._on_start)

    def safe_stop(self) -> None:
        self.root.after(0, self._on_stop)

    def safe_toggle(self) -> None:
        self.root.after(0, self._on_toggle)

    def run(self) -> None:
        self.root.mainloop()
