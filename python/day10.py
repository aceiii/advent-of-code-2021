#!/usr/bin/env python3

import sys
from functools import reduce


def validate_line(line):
    open_tags = set(['(', '[', '{', '<'])
    closing_tags = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    expected_closing_tag = []
    for char in line:
        if char in open_tags:
            expected_closing_tag.append(closing_tags[char])
        elif expected_closing_tag and expected_closing_tag[-1] == char:
            expected_closing_tag.pop()
        else:
            return (char, expected_closing_tag)
    return (None, expected_closing_tag)


def part1(lines):
    score_map = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    corrupted = [validate_line(line.strip()) for line in lines]
    return sum(score_map[char] for char, _ in corrupted if char is not None)


def part2(lines):
    score_map = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    lines = [(line.strip(), validate_line(line.strip())) for line in lines]
    incomplete = [(line, reversed(tags)) for (line, (err, tags)) in lines if err is None]
    scores = [reduce(lambda x, y: (x * 5) + score_map[y], tags, 0) for _, tags in incomplete]
    return sorted(scores)[len(scores)//2]


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

