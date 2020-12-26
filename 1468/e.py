#!python3

import sys


def calculate_area(line):
    values = sorted(map(int, line.strip().split(' ')))
    return values[0] * values[2]


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    answer = calculate_area(sys.stdin.readline())
    sys.stdout.write(f'{answer}\n')
