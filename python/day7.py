#!/usr/bin/env python3

import sys


def calculate_cost2(positions, target):
    return sum([sum(range(abs(n - target) + 1)) for n in positions])


def part1(lines):
    positions = sorted([int(n, 10) for n in lines[0].strip().split(',')])
    med = positions[len(positions)//2]
    cost = sum(abs(n - med) for n in positions)
    return cost


def part2(lines):
    positions = sorted([int(n, 10) for n in lines[0].strip().split(',')])
    min_position, max_position = min(positions), max(positions)
    target_range = range(min_position, max_position+1)
    costs = [calculate_cost2(positions, n) for n in target_range]
    return min(costs)


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

