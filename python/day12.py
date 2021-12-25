#!/usr/bin/env python3

import sys


class Cave:
    def __init__(self, name):
        self._name = name
        self._big = name.isupper()
        self._connected = []

    def name(self):
        return self._name

    def is_big(self):
        return self._big

    def connect(self, cave):
        if cave not in self._connected:
            self._connected.append(cave)

    def connected(self):
        for cave in self._connected:
            yield cave

    def __repr__(self):
        return str(self)

    def __str__(self):
        connected = [c.name() for c in self._connected]
        return '->'.join([self._name, str(connected)])


class CaveMap:
    def __init__(self, lines):
        self._caves = {}
        for line in lines:
            a, b = line.strip().split('-')
            cave_a = self._caves[a] if a in self._caves else Cave(a)
            cave_b = self._caves[b] if b in self._caves else Cave(b)
            cave_a.connect(cave_b)
            cave_b.connect(cave_a)
            self._caves[a] = cave_a
            self._caves[b] = cave_b

    def start(self):
        return self._caves['start']

    def end(self):
        return self._caves['end']

    def pathfind(self, target_cave, current_cave, current_path):
        new_path = current_path + [current_cave.name()]
        if target_cave == current_cave:
            return [new_path]

        paths = []
        for cave in current_cave.connected():
            if not cave.is_big() and cave.name() in current_path:
                continue
            paths.extend(self.pathfind(target_cave, cave, new_path))
        return paths

    def paths(self):
        return self.pathfind(self.end(), self.start(), [])


def part1(lines):
    caves = CaveMap(lines)
    return len(caves.paths())

def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

