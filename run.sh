#!/usr/bin/env bash
# Create a virtualenv, install dependencies and start the app.
set -e
cd "$(dirname "$0")"

python3 -m venv env 2>/dev/null || python -m venv env

# Linux/macOS use env/bin, Windows (Git Bash) uses env/Scripts
if [ -f env/bin/activate ]; then
  source env/bin/activate
else
  source env/Scripts/activate
fi

python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
