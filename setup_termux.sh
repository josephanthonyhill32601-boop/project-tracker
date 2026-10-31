#!/bin/bash
# Minimal Termux setup for the WickedJester Project Tracker.
# Installs only the packages this project uses; does not run a full system upgrade.
set -euo pipefail

pkg update -y
pkg install -y python sqlite git curl termux-api

# Android will ask for shared-storage permission when needed.
termux-setup-storage

echo "[SUCCESS] Required packages installed. No full package upgrade was run."
echo "Next: run python init_db.py from the project directory."
