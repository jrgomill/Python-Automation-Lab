#!/usr/bin/env python3
"""
detect_suspicious_processes.py

Detects suspicious parent-child process relationships.
Example: powershell.exe spawning cmd.exe or rundll32.exe.
"""

import psutil

SUSPICIOUS_PAIRS = [
    ("powershell.exe", "cmd.exe"),
    ("powershell.exe", "rundll32.exe"),
    ("cmd.exe", "powershell.exe"),
]

def detect():
    print("[+] Scanning for suspicious process relationships...")
    for proc in psutil.process_iter(['pid', 'name', 'ppid']):
        try:
            parent = psutil.Process(proc.info['ppid'])
            pair = (parent.name().lower(), proc.info['name'].lower())

            if pair in [(p[0].lower(), p[1].lower()) for p in SUSPICIOUS_PAIRS]:
                print(f"[!] Suspicious process chain detected: {parent.name()} → {proc.info['name']}")
        except Exception:
            pass

if __name__ == "__main__":
    detect()
