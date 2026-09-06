#!/usr/bin/env python3
"""
password_spray.py

Generates failed logons for detection testing.
"""

USERS = ["alice", "bob", "charlie"]
PASSWORD = "Winter2024!"

def spray():
    for user in USERS:
        print(f"[*] Attempting login for {user} with password {PASSWORD}")
        # Placeholder for actual auth attempts

if __name__ == "__main__":
    spray()
