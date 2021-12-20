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


class LanternFishWithCount(LanternFish):
    def __init__(self, n, qty=1):
        super().__init__(n)
        self._qty = qty

    def add(self, qty):
        self._qty += qty

    def quantity(self):
        return self._qty

    def tick(self):
        new_fish = super().tick()
        if new_fish:
            return LanternFishWithCount(new_fish._timer, self._qty)

    def __str__(self):
        return f"({self._timer}: {self._qty})"

    def __eq__(self, other):
        return other._timer == self._timer


def parse_fish(line):
    return [LanternFishWithCount(int(n, 10)) for n in line.strip().split(',')]


def parse_fish2(line):
    nums = [int(n, 10) for n in line.strip().split(',')]
    fish_map = {idx: None for idx in range(days_between_birth)}
    for num in nums:
        fish = fish_map[num]
        if not fish:
            fish_map[num] = LanternFishWithCount(num, 1)
        else:
            fish.add(1)
    return [fish for fish in fish_map.values() if fish]


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
    fish = parse_fish2(lines[0])
    days = 256
    while days > 0:
        days -= 1
        new_fish = []
        for f in fish:
            nf = f.tick()
            if nf:
                new_fish.append(nf)
        for nf in new_fish:
            for f in fish:
                if f == nf:
                    f.add(nf.quantity())
                    break
            else:
                fish.append(nf)

    return sum(f.quantity() for f in fish)


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

