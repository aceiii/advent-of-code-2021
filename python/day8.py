#!/usr/bin/env python3

import sys

"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

Length:
 0 -> 6
 1 -> 2 unique
 2 -> 5
 3 -> 5
 4 -> 4 unique
 5 -> 5
 6 -> 6
 7 -> 3 unique
 8 -> 7 unique
 9 -> 6
"""

def normalize_signal(signal):
    return ''.join(sorted(signal))


def parse_segments(line):
    return tuple(p.strip().split() for p in line.strip().split("|"))


def decode_pattern(signals):
    signals = [normalize_signal(s) for s in signals]
    pattern_map = {str(k):set() for k in range(10)}
    for s in signals:
        signal = normalize_signal(s)
        length = len(signal)
        segments = set(signal)
        if length == 2:
            pattern_map['1'] = segments
        elif length == 4:
            pattern_map['4'] = segments
        elif length == 3:
            pattern_map['7'] = segments
        elif length == 7:
            pattern_map['8'] = segments

    segment_a = pattern_map['7'].symmetric_difference(pattern_map['1'])
    segment_bd = pattern_map['4'].symmetric_difference(pattern_map['1'])
    segment_eg = pattern_map['8'].symmetric_difference(segment_a).symmetric_difference(pattern_map['4'])

    potential_0_6 = []
    for s in signals:
        signal = normalize_signal(s)
        length = len(signal)
        segments = set(signal)
        if length == 6:
            if len(segments.intersection(segment_eg)) == 1:
                pattern_map['9'] = segments
                segment_g = segments.symmetric_difference(segment_eg)
                segment_e = segment_eg.symmetric_difference(segment_g)
            else:
                potential_0_6.append(segments)

    potential_0, potential_6 = potential_0_6
    if len(potential_6.difference(pattern_map['1'])) == 4:
        pattern_map['0'] = potential_6
        pattern_map['6'] = potential_0
    else:
        pattern_map['6'] = potential_6
        pattern_map['0'] = potential_0


    segment_d = pattern_map['6'].symmetric_difference(pattern_map['0']).difference(pattern_map['1'])
    segment_b = segment_bd.symmetric_difference(segment_d)

    for s in signals:
        signal = normalize_signal(s)
        length = len(signal)
        segments = set(signal)
        if length == 5:
            if len(segments.intersection(segment_b)) == 1:
                pattern_map['5'] = segments
            elif len(segments.intersection(pattern_map['1'])) == 2:
                pattern_map['3'] = segments
            else:
                pattern_map['2'] = segments

    return {''.join(sorted(v)):k for k, v in pattern_map.items()}


def decode_output(pattern, output):
    output = [normalize_signal(o) for o in output]
    decoded = [pattern[o] for o in output]
    value = ''.join(decoded)
    return int(value, 10)


def part1(lines):
    count = 0
    for line in lines:
        patterns, values = [p.strip().split() for p in line.strip().split("|")]
        for value in values:
            n = len(value)
            if n == 2 or n == 4 or n == 3 or n == 7:
                count += 1
    return count


def part2(lines):
    total = 0
    for line in lines:
        signals, output = parse_segments(line)
        pattern = decode_pattern(signals)
        value = decode_output(pattern, output)
        total += value
    return total

def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

