#!python3

from sys import stdin, stdout

n, k = map(int, stdin.readline().strip().split(' '))

for _ in range(k):
    if n % 10:
        n -= 1
    else:
        n //= 10

stdout.write(f'{n}\n')
