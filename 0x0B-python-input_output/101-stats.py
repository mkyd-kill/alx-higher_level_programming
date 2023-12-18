#!/usr/bin/python3
import sys
from collections import defaultdict
"""
Reads stdin line by line and computes its metrics
By Status code and file size
"""


def print_statistics(total_size, status_codes):
    """Prints the stats of the status codes and file size"""
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def parse_line(line):
    """Parses the lines"""
    try:
        parts = line.split()
        file_size = int(parts[-1])
        status_code = parts[-2]
        return file_size, status_code
    except ValueError:
        return 0, None

def main():
    """Runs the program"""
    total_size = 0
    status_codes = defaultdict(int)
    count = 0

    try:
        for line in sys.stdin:
            file_size, status_code = parse_line(line)
            if file_size and status_code:
                total_size += file_size
                status_codes[status_code] += 1
                count += 1

            if count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
