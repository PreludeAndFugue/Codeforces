#!python3

from sys import stdin, stdout

n = int(stdin.readline())

total = 0
for _ in range(n):
    x = sum(map(int, stdin.readline().strip().split(' ')))
    if x >= 2:
        total += 1
stdout.write(f'{total}\n')
