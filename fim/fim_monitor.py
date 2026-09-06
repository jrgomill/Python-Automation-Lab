#!/usr/bin/env python3
"""
fim_monitor.py

Simple File Integrity Monitoring tool.
Watches a directory, hashes files, and logs changes.

Works on Windows or Linux.

Requires:
    pip install watchdog
"""

import hashlib
import json
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_DIR = "C:\\CriticalFiles"  # change as needed
OUTPUT_FILE = "fim_log.json"

def sha256_hash(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

class FIMHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            record = {
                "event": "modified",
                "path": event.src_path,
                "hash": sha256_hash(event.src_path)
            }
            log_event(record)

    def on_created(self, event):
        if not event.is_directory:
            record = {
                "event": "created",
                "path": event.src_path,
                "hash": sha256_hash(event.src_path)
            }
            log_event(record)

def log_event(record):
    print(f"[!] Change detected: {record}")
    with open(OUTPUT_FILE, "a") as f:
        f.write(json.dumps(record) + "\n")

def start_monitor():
    observer = Observer()
    handler = FIMHandler()
    observer.schedule(handler, WATCH_DIR, recursive=True)
    observer.start()
    print(f"[+] Monitoring {WATCH_DIR} for changes...")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    start_monitor()
