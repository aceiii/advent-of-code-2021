#!/usr/bin/env python3

import sys
from operator import itemgetter
from collections import defaultdict
from heapq import heapify, heappop, heappush


class RiskMap:
    def __init__(self, lines, extends=1):
        self._height = len(lines)
        self._width = len(lines[0].strip())
        self._grid = {}
        risks = list(range(1,10))
        for y in range(self._height * extends):
            line = lines[y % self._width].strip()
            extend_y = y // self._height
            for x in range(self._width * extends):
                pos = (x, y)
                extend_x = x // self._width
                char = line[x % self._width]
                risk_n = (int(char, 10) + extend_y + extend_x)
                risk = risks[(risk_n - 1) % len(risks)]
                self._grid[pos] = risk
        self._width *= extends
        self._height *= extends

    def neighbours(self, pos):
        x, y = pos
        if y > 0:
            yield (x, y-1)
        if y < self._height-1:
            yield (x, y+1)
        if x > 0:
            yield (x-1, y)
        if x < self._width-1:
            yield (x+1, y)

    def path(self):
        q = [(0, self.start())]
        dist = {v:float('inf') for v in self._grid.keys()}
        dist[self.start()] = 0
        visited = set()
        while q:
            d, u = heappop(q)
            if u in visited:
                continue
            visited.add(u)
            for v in self.neighbours(u):
                alt = d + self._grid[v]
                if alt < dist[v]:
                    dist[v] = alt
                    heappush(q, (alt, v))
        return dist[self.end()]

    def height(self):
        return self._height

    def width(self):
        return self._width

    def start(self):
        return (0, 0)

    def end(self):
        return (self._width - 1, self._height - 1)

    def risk_at(self, pos):
        return self._map[pos][0]

    def total_risk_at(self, pos):
        return self._map[pos][1]

    def __repr__(self):
        return str(self)

    def __str__(self):
        path = set(pos for pos in self.path())
        rows = []
        for y in range(self._height):
            row = []
            for x in range(self._width):
                pos = (x, y)
                if pos in path:
                    char = u"\u001b[31m" + str(self._map[pos][0]) + u"\u001b[0m"
                else:
                    char = str(self._map[pos][0])
                row.append(char)
            rows.append("".join(row))
        return "\n".join(rows)

def part1(lines):
    risk = RiskMap(lines)
    return risk.path()


def part2(lines):
    risk = RiskMap(lines, 5)
    return risk.path()


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

