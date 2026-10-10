"""
SOC Log Analysis - Beginner Python Project
Analyzes sample authentication logs and summarizes failed login attempts.
This project uses only local, fictional sample data.
"""

from collections import Counter
from pathlib import Path
import re

LOG_FILE = Path(__file__).parent / "sample_logs.txt"
FAILED_LOGIN_THRESHOLD = 3


def parse_failed_login(line: str):
    """Return the source IP if this line represents a failed login."""
    if "FAILED_LOGIN" not in line:
        return None

    match = re.search(r"\bip=(\d{1,3}(?:\.\d{1,3}){3})\b", line)
    return match.group(1) if match else None


def main():
    if not LOG_FILE.exists():
        print(f"Log file not found: {LOG_FILE}")
        print("Make sure sample_logs.txt is in the same folder as main.py.")
        return

    lines = LOG_FILE.read_text(encoding="utf-8").splitlines()
    failed_ips = Counter()
    successful = 0
    failed_total = 0

    for line in lines:
        if "SUCCESS_LOGIN" in line:
            successful += 1

        ip = parse_failed_login(line)
        if ip:
            failed_ips[ip] += 1
            failed_total += 1

    print("=" * 48)
    print("         SOC LOG ANALYSIS REPORT")
    print("=" * 48)
    print(f"Total log entries:          {len(lines)}")
    print(f"Successful login events:    {successful}")
    print(f"Failed login events:        {failed_total}")
    print()

    print("Failed login attempts by IP:")
    if not failed_ips:
        print("  No failed login events found.")
    else:
        for ip, count in failed_ips.most_common():
            label = "  [REVIEW]" if count >= FAILED_LOGIN_THRESHOLD else ""
            print(f"  {ip}: {count}{label}")

    flagged = [
        (ip, count)
        for ip, count in failed_ips.items()
        if count >= FAILED_LOGIN_THRESHOLD
    ]

    print()
    print(f"IPs with {FAILED_LOGIN_THRESHOLD}+ failed attempts:")
    if flagged:
        for ip, count in sorted(flagged, key=lambda item: item[1], reverse=True):
            print(f"  {ip} — {count} failed attempts; review the source and surrounding events.")
    else:
        print("  None")

    print()
    print("Note: This is a simple learning demo, not a production detection system.")
    print("Repeated failures can have legitimate causes; investigate before drawing conclusions.")


if __name__ == "__main__":
    main()
