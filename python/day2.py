#!/usr/bin/env python3

import sys


def parse_command(line):
    cmd, amount = line.split(' ', 1)
    return (cmd, int(amount, 10))


def parse_commands(lines):
    return list(map(parse_command, lines))


def run_commands(commands, start):
    x, y = start
    while commands:
        cmd, amount = commands.pop(0)
        if cmd == 'forward':
            x += amount
        elif cmd == 'up':
            y -= amount
        elif cmd == 'down':
            y += amount

    return x, y


def run_commands2(commands, start):
    x, y = start
    aim = 0
    while commands:
        cmd, amount = commands.pop(0)
        if cmd == 'forward':
            x += amount
            y += aim * amount
        elif cmd == 'up':
            aim -= amount
        elif cmd == 'down':
            aim += amount

    return x, y


def part1(lines):
    commands = parse_commands(lines)
    x, y = run_commands(commands, (0, 0))
    return x * y


def part2(lines):
    commands = parse_commands(lines)
    x, y = run_commands2(commands, (0, 0))
    return x * y


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

