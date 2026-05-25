# Simple AutoClicker

A lightweight desktop autoclicker with a Tkinter UI and global hotkeys.
Works on macOS, Linux, and Windows. Clicks at the current cursor position
on a configurable interval.

## Why

Most autoclickers be sketchy so I just made my own to play Roblox fr

## Requirements

- Python 3.10+
- macOS only: Tk bindings and Accessibility permission (see below)

### macOS setup

```bash
brew install python-tk@3.14
```

After the first launch, macOS will prompt to grant **Accessibility**
permission to your terminal (or whatever Python is being run from).
Approve it under
**System Settings → Privacy & Security → Accessibility**, then relaunch.
`pynput` needs this for both synthetic clicks and global hotkeys.

## Quick start

```bash
just setup # creates .venv and installs pynput
just run # launches the app
```

## Usage

1. Set the click interval in milliseconds (lower = faster).
2. Pick the mouse button (Left or Right).
3. Move the cursor to the target.
4. Press `F6` (or click **Start**). The app clicks the cursor location
   on the interval until you press `F7` / `F8` or click **Stop**.

`F8` toggles, which is handy when you only want to bind one key.

## Notes

Might add future stuff like macros or maybe make UI prettier
