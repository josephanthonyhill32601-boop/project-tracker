#!/usr/bin/env python3
"""Project Tracker CLI - add and list records / hybrid projects.

Usage:
  python tracker.py add-record --category notes --title "My title" --content "Body text"
  python tracker.py list-records [--category notes] [--limit 20]
  python tracker.py add-project --name "My App" [--repo-link URL] [--status Active]
  python tracker.py list-projects [--status Active]

DB location: $PROJECT_TRACKER_DB if set, otherwise the Termux shared
Documents path. Run init_db.py once first.
"""
import argparse
import sqlite3
import sys
from init_db import get_db_path, init_database


def connect():
    db_path = get_db_path()
    init_database(db_path)  # no-op if tables already exist
    return sqlite3.connect(db_path)


def add_record(args):
    conn = connect()
    try:
        cur = conn.execute(
            "INSERT INTO consolidated_records (category, title, content) VALUES (?, ?, ?)",
            (args.category, args.title, args.content or ""),
        )
        conn.commit()
        print(f"[SUCCESS] Record #{cur.lastrowid} saved under '{args.category}'.")
    finally:
        conn.close()


def list_records(args):
    conn = connect()
    try:
        q = "SELECT id, category, title, created_at FROM consolidated_records"
        params = []
        if args.category:
            q += " WHERE category = ?"
            params.append(args.category)
        q += " ORDER BY id DESC LIMIT ?"
        params.append(args.limit)
        rows = conn.execute(q, params).fetchall()
        if not rows:
            print("No records found.")
            return
        for rid, cat, title, created in rows:
            print(f"#{rid} [{cat}] {title} ({created})")
    finally:
        conn.close()


def add_project(args):
    conn = connect()
    try:
        cur = conn.execute(
            "INSERT INTO hybrid_projects (name, repo_link, status) VALUES (?, ?, ?)",
            (args.name, args.repo_link or "", args.status),
        )
        conn.commit()
        print(f"[SUCCESS] Project #{cur.lastrowid} '{args.name}' saved (status: {args.status}).")
    finally:
        conn.close()


def list_projects(args):
    conn = connect()
    try:
        q = "SELECT project_id, name, repo_link, status, created_at FROM hybrid_projects"
        params = []
        if args.status:
            q += " WHERE status = ?"
            params.append(args.status)
        q += " ORDER BY project_id DESC"
        rows = conn.execute(q, params).fetchall()
        if not rows:
            print("No projects found.")
            return
        for pid, name, repo, status, created in rows:
            repo_str = f" <{repo}>" if repo else ""
            print(f"#{pid} {name} [{status}]{repo_str} ({created})")
    finally:
        conn.close()


def main():
    p = argparse.ArgumentParser(description="Project Tracker CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    ar = sub.add_parser("add-record", help="Save a consolidated record")
    ar.add_argument("--category", required=True)
    ar.add_argument("--title", required=True)
    ar.add_argument("--content", default="")
    ar.set_defaults(func=add_record)

    lr = sub.add_parser("list-records", help="List saved records")
    lr.add_argument("--category", default=None)
    lr.add_argument("--limit", type=int, default=20)
    lr.set_defaults(func=list_records)

    ap = sub.add_parser("add-project", help="Register a hybrid project")
    ap.add_argument("--name", required=True)
    ap.add_argument("--repo-link", default="")
    ap.add_argument("--status", default="Active")
    ap.set_defaults(func=add_project)

    lp = sub.add_parser("list-projects", help="List registered projects")
    lp.add_argument("--status", default=None)
    lp.set_defaults(func=list_projects)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
