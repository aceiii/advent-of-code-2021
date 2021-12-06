#!/usr/bin/env python3

import sys


def part1(lines):
    depths = list(map(lambda x: int(x, 10), lines))
    prev = depths.pop(0)
    count  = 0
    while depths:
        depth = depths.pop(0)
        if depth > prev:
            count += 1
        prev = depth
    return count


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

