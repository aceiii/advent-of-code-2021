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
    depths = list(map(lambda x: int(x, 10), lines))
    prev_window = tuple(depths[:3])
    depths = depths[3:]
    count = 0
    while depths:
        window = tuple([*prev_window[1:], depths.pop(0)])
        if sum(window) > sum(prev_window):
            count += 1
        prev_window = window
    return count

def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

