#!/usr/bin/env python3

import sys
from operator import itemgetter
from collections import defaultdict


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



class FastPolymerizer:
    def __init__(self, template, insertion_map):
        self._insertion_map = {tuple(key): value for key, value in insertion_map.items()}
        self._pairs = defaultdict(lambda: 0)
        self._elements = defaultdict(lambda: 0)
        polymer = list(template)
        prev = polymer.pop(0)
        self._elements[prev] += 1
        while polymer:
            current = polymer.pop(0)
            pair = (prev, current)
            self._pairs[pair] += 1
            self._elements[current] += 1
            prev = current

    def step(self):
        new_pairs = defaultdict(lambda: 0)
        for pair in self._pairs:
            count = self._pairs[pair]
            if pair in self._insertion_map:
                left, right = pair
                inserted = self._insertion_map[pair]
                new_pair1 = (left, inserted)
                new_pair2 = (inserted, right)
                new_pairs[new_pair1] += count
                new_pairs[new_pair2] += count
                self._elements[inserted] += count
            else:
                new_pairs[pair] += count
        self._pairs = new_pairs

    def elements(self):
        return dict(self._elements)


def part1(lines):
    polymer, insertion_map = parse_polymerization(lines)
    steps = 10
    for _ in range(steps):
        polymer = polymer_insertion(polymer, insertion_map)
    counts = {c: polymer.count(c) for c in polymer}
    sorted_counts = sorted(((c, counts[c]) for c in counts), key=itemgetter(1))
    _, max_elements = sorted_counts[-1]
    _, min_elements = sorted_counts[0]
    return max_elements - min_elements


def part2(lines):
    template, insertion_map = parse_polymerization(lines)
    polymerizer = FastPolymerizer(template, insertion_map)
    steps = 40
    for _ in range(steps):
        polymerizer.step()
    elements = polymerizer.elements()
    sorted_counts = sorted(elements.items(), key=itemgetter(1))
    _, max_elements = sorted_counts[-1]
    _, min_elements = sorted_counts[0]
    return max_elements - min_elements


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

