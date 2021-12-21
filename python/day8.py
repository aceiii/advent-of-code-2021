#!/usr/bin/env python3

import sys


def part1(lines):
    count = 0
    for line in lines:
        patterns, values = [p.strip().split() for p in line.strip().split("|")]
        for value in values:
            n = len(value)
            if n == 2 or n == 4 or n == 3 or n == 7:
                count += 1
    return count


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

