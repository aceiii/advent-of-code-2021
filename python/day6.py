#!/usr/bin/env python3

import sys

days_between_birth = 7
new_fish_birth_offset = 2

class LanternFish:
    def __init__(self, n):
        self._timer = n

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self._timer)

    def tick(self):
        if self._timer == 0:
            self._timer = days_between_birth - 1
            return LanternFish(days_between_birth + new_fish_birth_offset - 1)
        self._timer -= 1


def parse_fish(line):
    return [LanternFish(int(n, 10)) for n in line.strip().split(',')]


def part1(lines):
    fish = parse_fish(lines[0])
    count = 80
    while count > 0:
        count -= 1
        new_fish = []
        for f in fish:
            nf = f.tick()
            if nf:
                new_fish.append(nf)
        fish += new_fish

    return len(fish)

def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

