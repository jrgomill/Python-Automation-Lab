#!/usr/bin/env python3
"""
rdp_bruteforce.py

Simulates RDP brute-force attempts for detection testing.
"""

USERS = ["alice", "bob"]
PASSWORDS = ["Password1!", "Password2!", "Password3!"]

def brute_force():
    for user in USERS:
        for pwd in PASSWORDS:
            print(f"[*] Trying RDP login user={user} password={pwd}")
            # Placeholder for actual RDP auth attempts

if __name__ == "__main__":
    brute_force()
