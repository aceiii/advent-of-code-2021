#!/usr/bin/env python3

import sys
from functools import reduce


class Packet:
    def __init__(self, version, type_id):
        self._version = version
        self._type_id = type_id
        self._value = None
        self._sub_packets = []

    def version(self):
        return self._version

    def type_id(self):
        return self._type_id

    def is_literal(self):
        return self._type_id == 4

    def is_sum(self):
        return self._type_id == 0

    def is_product(self):
        return self._type_id == 1

    def is_minimum(self):
        return self._type_id == 2

    def is_maximum(self):
        return self._type_id == 3

    def is_greater_than(self):
        return self._type_id == 5

    def is_less_than(self):
        return self._type_id == 6

    def is_equal_to(self):
        return self._type_id == 7

    def value(self):
        if self.is_literal():
            return self.get_literal_value()

        values = (p.value() for p in self.sub_packets())

        if self.is_sum():
            return sum(values)
        elif self.is_product():
            return reduce(lambda x,y: x * y, values)
        elif self.is_minimum():
            return min(values)
        elif self.is_maximum():
            return max(values)
        elif self.is_greater_than():
            first, second = self.sub_packets()
            return 1 if first.value() > second.value() else 0
        elif self.is_less_than():
            first, second = self.sub_packets()
            return 1 if first.value() < second.value() else 0
        elif self.is_equal_to():
            first, second = self.sub_packets()
            return 1 if first.value() == second.value() else 0

    def total_version(self):
        if self.is_literal():
            return self.version()
        total = sum(p.total_version() for p in self.sub_packets())
        return self.version() + total

    def get_literal_value(self):
        return self._value

    def set_literal_value(self, value):
        self._value = value

    def add_sub_packet(self, packet):
        self._sub_packets.append(packet)

    def sub_packets(self):
        return self._sub_packets[:]

    def to_str(self, level=0, spacing=2):
        version = str(self.version())
        type_id = str(self.type_id())
        head = f"<Packet version=\"{version}\" type=\"{type_id}\">"
        tail = "</Packet>"
        spacer = " " * (level * spacing)

        if self.is_literal():
            return spacer + head + str(self.get_literal_value()) + tail

        body = "\n".join(p.to_str(level+1) for p in self.sub_packets())
        if body.strip() == "":
            return spacer + head + tail

        return "\n".join([
            spacer + head,
            body,
            spacer + tail
        ])

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.to_str()


def decode_bits(line):
    num = int(line, 16)
    return bin(num)[2:]


def parse_literal_value(bits):
    offset = 0
    value_bits = []
    stop = False
    while not stop:
        group = bits[offset:offset+5]
        prefix = group[0]
        value_bits.append(group[1:])
        offset += 5
        stop = prefix == "0"

    return int("".join(value_bits), 2), offset


def parse_packet_recursive(bits):
    offset = 0
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    bits = bits[6:]
    offset += 6

    packet = Packet(version, type_id)

    if packet.is_literal():
        value, new_offset = parse_literal_value(bits)
        packet.set_literal_value(value)
        offset += new_offset
        return packet, offset

    length_type_id = int(bits[0], 2)
    bits = bits[1:]
    offset += 1

    if length_type_id == 0:
        bits_remaning = int(bits[:15], 2)
        bits = bits[15:]
        offset += 15
        while bits_remaning > 0:
            sub_packet, new_offset = parse_packet_recursive(bits)
            packet.add_sub_packet(sub_packet)
            bits = bits[new_offset:]
            bits_remaning -= new_offset
            offset += new_offset

    else:
        packets_remaining = int(bits[:11], 2)
        bits = bits[11:]
        offset += 11
        while packets_remaining > 0:
            sub_packet, new_offset = parse_packet_recursive(bits)
            packet.add_sub_packet(sub_packet)
            bits = bits[new_offset:]
            offset += new_offset
            packets_remaining -= 1

    return packet, offset


def parse_packet(bits):
    return parse_packet_recursive(bits)[0]


def part1(lines):
    bits = decode_bits(lines[0])
    packet = parse_packet(bits)
    return packet.total_version()


def part2(lines):
    bits = decode_bits(lines[0])
    packet = parse_packet(bits)
    return packet.value()


def main():
    lines = sys.stdin.readlines()
    print("Part1: {}".format(part1(lines)))
    print("Part2: {}".format(part2(lines)))


if __name__ == "__main__":
    main()

