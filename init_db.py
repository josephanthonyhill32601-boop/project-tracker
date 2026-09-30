#!/usr/bin/env python3
"""Project Tracker - database initialization.

Creates the master SQLite database with all tables.
DB location: $PROJECT_TRACKER_DB if set, otherwise the Termux shared
Documents path (~/storage/shared/Documents/project_master.db).
"""
import sqlite3
import os
import sys


def get_db_path():
    return os.environ.get(
        "PROJECT_TRACKER_DB",
        os.path.expanduser("~/storage/shared/Documents/project_master.db"),
    )


SCHEMA = """
CREATE TABLE IF NOT EXISTS consolidated_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT NOT NULL,
    title TEXT NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS hybrid_projects (
    project_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    repo_link TEXT,
    status TEXT DEFAULT 'Active',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX IF NOT EXISTS idx_records_category ON consolidated_records(category);
CREATE INDEX IF NOT EXISTS idx_records_created ON consolidated_records(created_at);
CREATE INDEX IF NOT EXISTS idx_projects_status ON hybrid_projects(status);
"""


def init_database(db_path=None):
    db_path = db_path or get_db_path()
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(SCHEMA)
        conn.commit()
    finally:
        conn.close()
    print(f"[SUCCESS] Master database initialized at: {db_path}")
    return db_path


if __name__ == "__main__":
    init_database(sys.argv[1] if len(sys.argv) > 1 else None)
