# Project Tracker

Your hybrid phone/cloud command center. Built 2026-09-30.
All code runs here or on your phone — zero Colab GPU minutes, zero Codespaces hours used.

## Files

- `init_db.py` — creates the master SQLite database (run once)
- `tracker.py` — command-line tool to add/list records and projects
- `setup_termux.sh` — one-shot Termux environment setup for OneLove
- `device_profile.json` — your device + execution strategy spec

## Phone setup (OneLove)

1. Install **Termux** and **Termux:API** from F-Droid (https://f-droid.org/)
2. Copy this folder to your phone (e.g. `~/storage/shared/Documents/project-tracker/`)
3. In Termux:
   ```bash
   bash setup_termux.sh
   python init_db.py
   ```

## Usage

```bash
# Save a note/record
python tracker.py add-record --category ideas --title "Video concept" --content "Details here"

# List records (newest first)
python tracker.py list-records
python tracker.py list-records --category ideas --limit 10

# Register a software project
python tracker.py add-project --name "GameVault tools" --repo-link https://github.com/you/repo

# List projects
python tracker.py list-projects
```

The database lives at `~/storage/shared/Documents/project_master.db` on the
phone, so Obsidian and other apps can read it too. To use a different location:

```bash
export PROJECT_TRACKER_DB=/path/to/my.db
```

## Notes

- Everything is stdlib Python — no downloads needed beyond the Termux setup.
- Keep GitHub repos **private** until your attorney says otherwise.
