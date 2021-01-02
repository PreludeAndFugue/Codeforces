#!python3

from sys import stdin, stdout

n = int(stdin.readline())

min_capacity = 0
current_capacity = 0
for _ in range(n):
    a, b = map(int, stdin.readline().strip().split(' '))
    current_capacity = current_capacity - a + b
    min_capacity = max(min_capacity, current_capacity)

stdout.write(f'{min_capacity}\n')
