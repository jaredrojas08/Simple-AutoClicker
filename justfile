# Simple AutoClicker — common commands
# Run `just` (no args) to see this list.

venv := ".venv"
python := venv / "bin/python"
pip := venv / "bin/pip"

# Show available recipes
default:
    @just --list

# First-time setup: create venv and install dependencies
setup:
    python3 -m venv {{venv}}
    {{pip}} install --upgrade pip
    {{pip}} install -r requirements.txt
    @echo ""
    @echo "Setup complete. Run the app with:  just run"
    @echo "macOS users: grant Accessibility permission to your terminal"
    @echo "             (System Settings → Privacy & Security → Accessibility)"

# Run the autoclicker
run:
    {{python}} main.py

# Remove venv and Python caches
clean:
    rm -rf {{venv}}
    find . -type d -name __pycache__ -exec rm -rf {} +
    @echo "Cleaned. Run 'just setup' to reinstall."

# Reinstall from scratch
reset: clean setup

# Lock current dependency versions
freeze:
    {{pip}} freeze > requirements.lock.txt
