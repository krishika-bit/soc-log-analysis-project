# SOC Log Analysis (Beginner Python Project)

## Overview
A small defensive cybersecurity project that reads fictional authentication logs and summarizes successful logins, failed logins, and IP addresses with repeated failed attempts.

## Features
- Counts successful login events.
- Counts failed login events.
- Groups failed attempts by source IP address.
- Flags IPs with three or more failed attempts for review.
- Uses fictional sample logs only.

## Requirements
- Python 3.8 or newer
- No external Python packages required

## How to run
1. Download or clone this repository.
2. Make sure `main.py` and `sample_logs.txt` are in the same folder.
3. Open a terminal in that folder.
4. Run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py`.

## Project files
- `main.py` — log parsing and report generation.
- `sample_logs.txt` — fictional sample authentication events.
- `README.md` — project documentation.

## Example finding
The sample data contains repeated failed login attempts from `198.51.100.23`. The script flags this address for review because it reaches the configured threshold.

## Limitations
This is an educational demonstration. It does not prove that an IP is malicious, and it should not be used as a production SOC tool. Investigate alerts in context before making decisions.

## Learning outcomes
- Python file handling
- String parsing with regular expressions
- Counting and summarizing events
- Basic security log triage
- Documenting a project for GitHub
