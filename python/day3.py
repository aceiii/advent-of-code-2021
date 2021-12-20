#!/usr/bin/env python3

import sys
from collections import defaultdict


def part1(lines):
    total = len(lines)
    num_bits = len(lines[0].strip())
    bits = defaultdict(lambda: 0)
    for line in lines:
        line = line.strip()
        for idx in range(0, len(line)):
            bit = line[idx]
            if bit == '1':
                bits[idx] += 1
    gamma = []
    epsilon = []
    for idx in range(num_bits):
        count = bits[idx]
        if count > (total/2):
            gamma.append('1')
            epsilon.append('0')
        else:
            gamma.append('0')
            epsilon.append('1')
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)


def part2(lines):
    candidates = list(map(lambda x: x.strip(), lines))
    oxygen_generator_rating = find_rating(candidates, oxygen_bit_criteria)
    co2_scrubber_rating = find_rating(candidates, co2_bit_criteria)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating
    return life_support_rating


def find_rating(candidates, candidate_func):
    bit_index = 0
    while len(candidates) > 1:
        bits = map(lambda c: c[bit_index], candidates)
        ones, zeroes = count_bits(bits)
        bit = candidate_func(ones, zeroes)
        candidates = list(filter(lambda c: int(c[bit_index], 10) == bit, candidates))
        bit_index += 1
    rating = int(candidates[0], 2)
    return rating


def count_bits(bits):
    ones, zeroes = 0, 0
    for b in bits:
        if b == '1':
            ones += 1
        else:
            zeroes += 1
    return (ones, zeroes)


def oxygen_bit_criteria(ones, zeroes):
    if ones >= zeroes:
        return 1
    return 0


def co2_bit_criteria(ones, zeroes):
    if zeroes <= ones:
        return 0
    return 1


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

