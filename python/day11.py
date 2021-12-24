#!/usr/bin/env python3

import sys


class OctopusSim:
    def __init__(self, lines):
        self._grid = {}
        self._width = len(lines[0].strip())
        self._height = len(lines)
        self._flashes = 0
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                energy = int(char, 10)
                pos = (x, y)
                self._grid[pos] = energy

    def size(self):
        return (self._width, self._height)

    def step(self):
        flashed = set()
        flashing = set()
        for pos in self._tiles():
            self._grid[pos] += 1
            if self._grid[pos] > 9:
                flashing.add(pos)

        while flashing:
            pos = flashing.pop()
            flashed.add(pos)
            for neighbour in self._neighbours(pos):
                if neighbour in flashed:
                    continue
                self._grid[neighbour] += 1
                if self._grid[neighbour] > 9:
                    flashing.add(neighbour)

        for pos in flashed:
            self._flashes += 1
            self._grid[pos] = 0

    def reset_flashes(self):
        self._flashes = 0

    def flashes(self):
        return self._flashes

    def _neighbours(self, pos):
        x, y = pos
        directions = [
            (x, y-1),
            (x+1, y-1),
            (x+1, y),
            (x+1, y+1),
            (x, y+1),
            (x-1, y+1),
            (x-1, y),
            (x-1, y-1),
        ]
        return [d for d in directions if d in self._grid]

    def _tiles(self):
        for y in range(self._height):
            for x in range(self._width):
                yield (x, y)

    def __repr__(self):
        return str(self)

    def __str__(self):
        lines = []
        for y in range(self._height):
            lines.append([])
            for x in range(self._width):
                pos = (x, y)
                level = self._grid[pos]
                if level == 0:
                    lines[-1].append(u"\u001b[37m" + str(level) + u"\u001b[0m")
                else:
                    lines[-1].append(str(level))
        return "\n".join("".join(line) for line in lines)


def part1(lines):
    sim = OctopusSim(lines)
    for _ in range(100):
        sim.step()
    return sim.flashes()


def part2(lines):
    sim = OctopusSim(lines)
    steps = 0
    width, height = sim.size()
    target = width * height
    while True:
        steps += 1
        sim.reset_flashes()
        sim.step()
        if sim.flashes() == target:
            break
    return steps


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

