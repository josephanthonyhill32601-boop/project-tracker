#!/bin/bash
# Termux one-shot setup for Motorola Moto G 5G (2025 Edition).
# Paste into Termux (F-Droid build). Pauses once for the storage permission.
set -e
pkg update -y && pkg upgrade -y
pkg install -y python sqlite git curl termux-api
termux-setup-storage
python -m pip install --upgrade pip
echo "[SUCCESS] Environment provisioning complete."
