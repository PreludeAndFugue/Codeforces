#!python3

from sys import stdin, stdout

for r in range(5):
    row = list(map(int, stdin.readline().strip().split(' ')))
    try:
        c = row.index(1)
        r = r + 1
        c = c + 1
        d = abs(3 - c) + abs(3 - r)
        stdout.write(f'{d}\n')
    except ValueError:
        pass
