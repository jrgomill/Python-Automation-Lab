# Python-Automation-Lab

## Overview

This lab demonstrates Python-based automation for cybersecurity engineering,
including:

- Windows Event Log parsing
- Sysmon log parsing
- File Integrity Monitoring (FIM)
- Simple EDR-style behavioral detections
- Offensive simulation scripts (password spraying, RDP brute-force)

This project pairs with my Active Directory Attack Simulation Lab and Wazuh SIEM
Deployment Lab to create a full end-to-end detection engineering portfolio.

---

## Features

### ✔ Log Parsing
- Extract Windows Security logs
- Extract Sysmon process creation logs
- Export results to JSON for SIEM ingestion

### ✔ File Integrity Monitoring
- Watches critical directories
- Hashes files using SHA-256
- Logs changes to a local file

### ✔ Simple EDR Detections
- Detects encoded PowerShell commands
- Detects suspicious parent-child process relationships

### ✔ Offensive Simulation
- Password spraying script
- RDP brute-force script

---

## Folder Structure

log_parser/        → Windows + Sysmon log parsers
fim/               → File Integrity Monitoring tool
edr/               → Behavioral detection scripts
offensive/         → Attack simulation scripts
detections/        → Documentation of detection logic
screenshots/       → Output examples
