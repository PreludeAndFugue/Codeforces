#!python3

from sys import stdin, stdout

m, n = map(int, stdin.readline().strip().split(' '))

if m == 1 and n == 1:
    answer = 0
elif m % 2 == 0:
    answer = (m // 2) * n
else:
    answer = (m // 2) * n + (n // 2)

stdout.write(f'{answer}\n')
