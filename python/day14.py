#!/usr/bin/env python3

import sys
from operator import itemgetter


def parse_polymerization(lines):
    lines = lines[:]
    template = lines.pop(0).strip()
    lines.pop(0)
    insertion_map ={}
    for line in lines:
        key, value = [s.strip() for s in line.strip().split("->")]
        insertion_map[key] = value
    return template, insertion_map


def polymer_insertion(polymer, insertion_map):
    polymer = list(polymer)
    new_polymer = []
    prev = polymer.pop(0)
    new_polymer.append(prev)
    while polymer:
        current = polymer.pop(0)
        pair = prev + current
        if pair in insertion_map:
            new_polymer.append(insertion_map[pair])
        new_polymer.append(current)
        prev = current
    return "".join(new_polymer)


def part1(lines):
    polymer, insertion_map = parse_polymerization(lines)
    steps = 10
    for _ in range(steps):
        polymer = polymer_insertion(polymer, insertion_map)
    counts = {c:polymer.count(c) for c in polymer}
    sorted_counts = sorted(((c, counts[c]) for c in counts), key=itemgetter(1))
    _, max_elements = sorted_counts[-1]
    _, min_elements = sorted_counts[0]
    return max_elements - min_elements


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

