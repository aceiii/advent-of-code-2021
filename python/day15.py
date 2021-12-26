#!/usr/bin/env python3

import sys
from operator import itemgetter
from collections import defaultdict


class RiskMap:
    def __init__(self, lines):
        self._height = len(lines)
        self._width = len(lines[0].strip())
        self._map = {}
        for y, line in enumerate(lines):
            for x, char in enumerate(line.strip()):
                pos = (x, y)
                up = (x, y - 1)
                left = (x - 1, y)
                risk = int(char, 10)
                up_risk, up_path = self._map[up][1:] if up in self._map else (None, [])
                left_risk, left_path = self._map[left][1:] if left in self._map else (None, [])
                if up_risk is not None and left_risk is not None:
                    if up_risk <= left_risk:
                        new_risk = risk + up_risk
                        new_path = up_path + [pos]
                    else:
                        new_risk = risk + left_risk
                        new_path = left_path + [pos]
                elif up_risk is not None:
                    new_risk = risk + up_risk
                    new_path = up_path + [pos]
                elif left_risk is not None:
                        new_risk = risk + left_risk
                        new_path = left_path + [pos]
                else:
                    new_risk = 0
                    new_path = [pos]
                self._map[pos] = (risk, new_risk, new_path)

    def height(self):
        return self._height

    def width(self):
        return self._width

    def path(self):
        end = (self._width - 1, self._height - 1)
        return self._map[end][2]

    def risk_at(self, pos):
        return self._map[pos][0]


def part1(lines):
    risk = RiskMap(lines)
    path = risk.path()
    return sum(risk.risk_at(pos) for pos in path[1:])


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

