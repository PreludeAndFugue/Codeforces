#!python3

import sys


def calculate(c1, c2, c3, a1, a2, a3, a4, a5):
    c1 -= a1
    if c1 < 0:
        return 'NO'
    c2 -= a2
    if c2 < 0:
        return 'NO'
    c3 -= a3
    if c3 < 0:
        return 'NO'
    a4 -= min(a4, c1)
    a5 -= min(a5, c2)
    if c3 < a4 + a5:
        return 'NO'
    return 'YES'


test_count = int(sys.stdin.readline())
for _ in range(test_count):
    c1, c2, c3 = map(int, sys.stdin.readline().strip().split(' '))
    a1, a2, a3, a4, a5 = map(int, sys.stdin.readline().strip().split(' '))
    answer = calculate(c1, c2, c3, a1, a2, a3, a4, a5)
    sys.stdout.write(f'{answer}\n')
