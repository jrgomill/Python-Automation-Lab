# Detection Notes

This document explains how each Python script contributes to detection
engineering.

## Log Parsers

### eventlog_parser.py
Extracts Windows Security logs for:
- Failed logons (4625)
- Logon successes (4624)
- Account changes (4720, 4728)
- Event log clearing (1102)

### sysmon_parser.py
Extracts Sysmon logs for:
- Process creation (Event ID 1)
- Network connections (Event ID 3)

---

## File Integrity Monitoring

### fim_monitor.py
Detects:
- File creation
- File modification
- Hash changes

Useful for detecting:
- Malware drops
- Unauthorized config changes

---

## EDR Scripts

### detect_encoded_powershell.py
Detects:
- Encoded PowerShell commands
- Obfuscated execution

### detect_suspicious_processes.py
Detects:
- Suspicious parent-child process chains
- Living-off-the-land binaries (LOLBins)

---

## Offensive Scripts

Used to generate logs for detection testing.

### password_spray.py
Creates multiple failed logons.

### rdp_bruteforce.py
Simulates brute-force attempts.

---
