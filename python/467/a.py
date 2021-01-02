#!python3

from sys import stdin, stdout

n = int(stdin.readline())

count = 0
for _ in range(n):
    p, q = map(int, stdin.readline().strip().split(' '))
    if q - p >= 2:
        count += 1

stdout.write(f'{count}\n')
