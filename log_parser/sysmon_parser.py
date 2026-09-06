#!/usr/bin/env python3
"""
sysmon_parser.py

Parses Sysmon logs (Event ID 1, 3, etc.) using pywin32.
Exports results to JSON.

Requires:
    pip install pywin32
"""

import json
import win32evtlog

LOG_TYPE = "Microsoft-Windows-Sysmon/Operational"
OUTPUT_FILE = "sysmon_logs.json"

def parse_sysmon_logs():
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
                "Strings": event.StringInserts,
            }
            events.append(entry)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(events, f, indent=4)

    print(f"[+] Exported {len(events)} Sysmon events to {OUTPUT_FILE}")


if __name__ == "__main__":
    parse_sysmon_logs()
