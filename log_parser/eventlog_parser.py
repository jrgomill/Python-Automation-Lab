#!/usr/bin/env python3
"""
eventlog_parser.py

Parses Windows Security Event Logs using pywin32.
Exports results to JSON for SIEM ingestion.

Requires:
    pip install pywin32
"""

import json
import win32evtlog

LOG_TYPE = "Security"
OUTPUT_FILE = "security_logs.json"

def parse_security_logs():
    server = "localhost"
    handle = win32evtlog.OpenEventLog(server, LOG_TYPE)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = []

    while True:
        records = win32evtlog.ReadEventLog(handle, flags, 0)
        if not records:
            break

        for event in records:
            entry = {
                "EventID": event.EventID,
                "TimeGenerated": str(event.TimeGenerated),
                "SourceName": event.SourceName,
                "EventCategory": event.EventCategory,
                "EventType": event.EventType,
                "ComputerName": event.ComputerName,
                "Strings": event.StringInserts,
            }
            events.append(entry)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(events, f, indent=4)

    print(f"[+] Exported {len(events)} events to {OUTPUT_FILE}")


if __name__ == "__main__":
    parse_security_logs()
