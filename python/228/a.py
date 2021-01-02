#!python3

from sys import stdin, stdout

n = set(map(int, stdin.readline().strip().split(' ')))
s = 4 - len(n)

stdout.write(f'{s}\n')
