#!python3

from collections import defaultdict
from itertools import combinations
from sys import stdin, stdout


def run_test(count, coords):
    counter = defaultdict(int)
    for x1, x2 in combinations(coords, 2):
        area = (x2 - x1) / 2
        counter[area] += 1
    return len(counter.keys())


def main():
    test_count = int(stdin.readline())
    for _ in range(test_count):
        count = int(stdin.readline())
        coords = map(int, stdin.readline().strip().split(' '))
        c = run_test(count, coords)
        stdout.write(f'{c}\n')


main()
