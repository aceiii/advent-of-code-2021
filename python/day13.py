#!/usr/bin/env python3

import sys


class TransparentPaper:
    def __init__(self, lines):
        self._dots = {}
        self._width = 0
        self._height = 0
        for line in lines:
            x, y = [int(c, 10) for c in line.strip().split(",")]
            self._dots[(x, y)] = True
            self._width = max(self._width, x)
            self._height = max(self._height, y)

    def foldx(self, value):
        new_dots = {}
        for pos in self._dots:
            x, y = pos
            if x <= value:
                new_dots[pos] = self._dots[pos]
                pass
            else:
                new_dots[(value - (x - value), y)] = self._dots[pos]
        self._dots = new_dots
        self._width = min(value - 1, self._width)

    def foldy(self, value):
        new_dots = {}
        for pos in self._dots:
            x, y = pos
            if y <= value:
                new_dots[pos] = self._dots[pos]
            else:
                new_dots[(x, value - (y - value))] = self._dots[pos]
        self._dots = new_dots
        self._height = min(value - 1, self._height)

    def fold(self, axis, value):
        if axis == "x":
            self.foldx(value)
        elif axis == "y":
            self.foldy(value)
        else:
            assert 0, "Axis must be 'x' or 'y'"

    def count_dots(self):
        return sum(1 if self._dots[pos] else 0 for pos in self._dots)

    def __repr__(self):
        return str(self)

    def __str__(self):
        rows = []
        for y in range(self._height + 1):
            row = []
            for x in range(self._width + 1):
                pos = (x, y)
                dot = self._dots[pos] if pos in self._dots else False
                row.append("#" if dot else ".")
            rows.append("".join(row))
        return "\n".join(rows)


def parse_paper(lines):
    lines = lines[:]
    dots = []
    while True:
        line = lines.pop(0).strip()
        if line == "":
            break
        dots.append(line)
    folds = []
    for line in lines:
        fold = line.strip()[10:]
        axis, val = fold.split("=")
        folds.append((axis.strip(), int(val, 10)))

    return TransparentPaper(dots), folds


def part1(lines):
    paper, folds = parse_paper(lines)
    paper.fold(*folds[0])
    return paper.count_dots()


def part2(lines):
    paper, folds = parse_paper(lines)
    for fold in folds:
        paper.fold(*fold)
    return "\n" + str(paper)


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

