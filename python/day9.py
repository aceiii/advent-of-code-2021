#!/usr/bin/env python3

import sys
from functools import reduce


class Heightmap:
    def __init__(self, lines):
        self._heightmap = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                height = int(char, 10)
                self._heightmap[(x, y)] = height

    def _neighbours(self, pos):
        x, y = pos
        directions = [
            (x, y-1),
            (x, y+1),
            (x-1, y),
            (x+1, y),
        ]
        return [d for d in directions if d in self._heightmap]

    def _basin(self, pos):
        current = self._heightmap[pos]
        tiles = set([(pos, current)])
        for neighbour in self._neighbours(pos):
            height = self._heightmap[neighbour]
            if height >= 9:
                continue
            elif height > current:
                tiles.update(self._basin(neighbour))
        return list(tiles)

    def low_points(self):
        flow = [(pos, [self._heightmap[n] for n in self._neighbours(pos)]) for pos in self._heightmap]
        lowest = [pos for pos, neighbour in flow if all(self._heightmap[pos] < n for n in neighbour)]
        return [(pos, self._heightmap[pos]) for pos in lowest]

    def basins(self):
        return [self._basin(pos) for pos,_ in self.low_points()]


def part1(lines):
    heightmap = Heightmap(lines)
    lowest = heightmap.low_points()
    risk = [1 + height for _, height in lowest]
    return sum(risk)


def part2(lines):
    heightmap = Heightmap(lines)
    basins = heightmap.basins()
    return reduce(lambda x,y: x * y, sorted((len(basin) for basin in basins), reverse=True)[:3])


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

