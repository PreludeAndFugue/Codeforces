#!python3

from sys import stdin, stdout

n = int(stdin.readline())
s = sum(map(int, stdin.readline().strip().split(' ')))
f = s / n

stdout.write(f'{f}\n')
