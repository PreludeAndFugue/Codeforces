#!python3

from sys import stdin, stdout

x = int(stdin.readline())

y = x // 5
if x % 5:
    y += 1

stdout.write(f'{y}\n')
