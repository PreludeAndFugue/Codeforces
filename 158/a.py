#!python3

from sys import stdin, stdout

n, k = map(int, stdin.readline().strip().split(' '))
a = list(map(int, stdin.readline().strip().split(' ')))
c = a[k - 1]
p = sum(1 for i in a if i >= c and i > 0)
stdout.write(f'{p}\n')
