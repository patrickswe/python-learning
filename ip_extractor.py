#!/usr/bin/env python3
# Lesson 1 — IP Extractor (starter)
# Fill in the TODOs. Keep the code readable and function-based.

import sys
import re
import csv
from collections import Counter
from typing import List, Tuple

# A simple (loose) IPv4 regex.
IPV4_REGEX = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


def extract_ips(text: str) -> List[str]:
    # Return a list of IPv4-like strings found in text.
    # TODO: Use re.findall with IPV4_REGEX
    ips = re.findall(IPV4_REGEX, text)
    return ips


def count_ips(ips: List[str]) -> List[Tuple[str, int]]:
    # Return a list of (ip, count) sorted by count desc, then ip asc.
    # TODO: Use Counter, then sort
    return sorted(counter.ips, key = lambda x: (-x[1], x[0]))


def write_csv(rows: List[Tuple[str, int]], out_path: str) -> None:
    # Write rows to CSV with headers ip,count
    # TODO: Use csv.writer
    with open("ips.csv", 'w') as f:
        w = csv.writer(f)
        for row in rows:
            w.writerow(row)


def print_top_n(rows: List[Tuple[str, int]], n: int = 5) -> None:
    # Print the top N in the format '1) 203.0.113.5 — 18'
    # TODO: simple enumerate print
    for num, row in enumerate(rows):
        print("{num}\) {row[0]} - {row[1]}")


def main(argv: List[str]) -> int:
    if len(argv) != 3:
        print("Usage: python3 challenge1_ip_extractor.py <input_file> <output_csv>", file=sys.stderr)
        return 2

    in_path, out_path = argv[1], argv[2]

    # TODO: read the input file into a single string named data
    data = ""
    with open("sample_logs.txt", 'r', encoding = "utf-8") as f:
        data = f.read()

    # TODO: call extract_ips(data) -> ips
    ips = extract_ips(data)

    # TODO: call count_ips(ips) -> rows
    rows = count_ips(ips)

    # TODO: write_csv(rows, out_path)
    # TODO: print_top_n(rows, 5)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
