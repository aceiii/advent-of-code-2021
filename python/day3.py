#!/usr/bin/env python3

import sys
from collections import defaultdict


def part1(lines):
    total = len(lines)
    num_bits = len(lines[0].strip())
    bits = defaultdict(lambda: 0)
    for line in lines:
        line = line.strip()
        for idx in range(0, len(line)):
            bit = line[idx]
            if bit == '1':
                bits[idx] += 1
    gamma = []
    epsilon = []
    for idx in range(num_bits):
        count = bits[idx]
        if count > (total/2):
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

