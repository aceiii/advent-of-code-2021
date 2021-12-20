#!/usr/bin/env python3

import sys


def part1(lines):
    positions = sorted([int(n, 10) for n in lines[0].strip().split(',')])
    med = positions[len(positions)//2]
    cost = sum(abs(n - med) for n in positions)
    return cost


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

