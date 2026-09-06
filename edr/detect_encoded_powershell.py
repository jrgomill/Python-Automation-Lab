#!/usr/bin/env python3
"""
detect_encoded_powershell.py

Detects encoded PowerShell commands by scanning process command lines.
"""

import psutil

def detect():
    print("[+] Scanning for encoded PowerShell commands...")
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmd = " ".join(proc.info['cmdline'])
            if "powershell" in cmd.lower() and "encodedcommand" in cmd.lower():
                print(f"[!] Suspicious PowerShell detected: PID={proc.info['pid']} CMD={cmd}")
        except Exception:
            pass

if __name__ == "__main__":
    detect()
