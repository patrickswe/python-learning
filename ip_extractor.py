#!/usr/bin/env python
# Lesson 1 — IP Extractor (starter)
# Fill in the TODOs. Keep the code readable and function-based.

import sys
import re
import csv
from collections import Counter
from typing import List, Tuple
import ipaddress

# A simple (loose) IPv4 regex.
IPV4_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

def detect_suspicious(rows, threshold=100):
    return [row for row in rows if row[1] >= threshold]

def is_public_ip(ip: str) -> bool:
    try: 
        return ipaddress.ip_address(ip).is_global
    except ValueError:
        return False

def extract_ips(text: str) -> List[str]:
    # Return a list of IPv4-like strings found in text.
    # TODO: Use re.findall with IPV4_REGEX
    return re.findall(IPV4_REGEX, text)

def count_ips(ips: List[str]) -> List[Tuple[str, int]]:
    # Return a list of (ip, count) sorted by count desc, then ip asc.
    # TODO: Use Counter, then sort
    cnts = Counter(ips)
    return sorted(cnts.items(), key = lambda x: (-x[1], x[0]))


def write_csv(rows: List[Tuple[str, int]], out_path: str) -> None:
    # Write rows to CSV with headers ip,count
    # TODO: Use csv.writer
    with open(out_path, 'w', newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["ip", "count"])
        w.writerows(rows)


def print_top_n(rows: List[Tuple[str, int]], n: int = 5) -> None:
    # Print the top N in the format '1) 203.0.113.5 — 18'
    # TODO: simple enumerate print
    for i, (ip,count) in enumerate(rows[:n], start=1):
        print(f"{i}) {ip} - {count}")


def main(argv: List[str]) -> int:
    if len(argv) != 3:
        print("Usage: python3 challenge1_ip_extractor.py <input_file> <output_csv>", file=sys.stderr)
        return 2

    in_path, out_path = argv[1], argv[2]

    # TODO: read the input file into a single string named data
    data = ""
    with open(in_path, 'r', encoding = "utf-8") as f:
        data = f.read()

    # TODO: call extract_ips(data) -> ips
    ips = [ip for ip in extract_ips(data) if is_public_ip(ip)]

    # TODO: call count_ips(ips) -> rows
    rows = count_ips(ips)

    write_csv(rows, out_path)

    print_top_n(rows, 5)

    suspicious = detect_suspicious(rows, 4)
    if suspicious:
        print(f"\n ⚠️  Suspicious IPs detected:")
        for ip, count in suspicious:
            print(f"{ip} - {count} requests")
    else:
        print("\nNo suspicious activity detected.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
