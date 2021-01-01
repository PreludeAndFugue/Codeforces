#!python3

from sys import stdin, stdout

k, n, w = map(int, stdin.readline().strip().split(' '))
t = k * (w*(w + 1)) // 2
b = max(t - n, 0)

stdout.write(f'{b}\n')
