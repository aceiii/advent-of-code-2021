#!/usr/bin/env python3

import sys
from math import sqrt
from collections import defaultdict


class LineSegment:
    def __init__(self, start, end):
        sx, sy = start
        ex, ey = end
        dx, dy = ex-sx, ey-sy

        self._start = (sx, sy)
        self._end = (ex, ey)
        self._diff = (dx, dy)
        self._len = int(sqrt(dx * dx + dy * dy))

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"{self._start} -> {self._end}"

    def is_vertical(self):
        return self._diff[0] == 0

    def is_horizontal(self):
        return self._diff[1] == 0

    def points(self):
        x, y = self._start
        dx, dy = self._diff
        dx = dx / abs(dx) if dx != 0 else 0
        dy = dy / abs(dy) if dy != 0 else 0
        while True:
            point = (x, y)
            yield point
            if point == self._end:
                break
            x, y = (x + dx, y + dy)


def parse_line_segments(lines):
    segments = (line.strip().split(" -> ") for line in lines)
    segments = (start.split(',') + end.split(',') for start, end in segments)
    segments = [[int(x, 10) for x in segment] for segment in segments]
    return [LineSegment((sx, sy), (ex, ey)) for sx, sy, ex, ey in segments]


def part1(lines):
    segments = parse_line_segments(lines)
    points = defaultdict(lambda: 0)
    for segment in segments:
        if not segment.is_vertical() and not segment.is_horizontal():
            continue
        for point in segment.points():
            points[point] += 1

    answer = 0
    for key, count in points.items():
        if count >= 2:
            answer += 1
    return answer


def part2(lines):
    pass


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

