#!python3

from sys import stdin, stdout

n1 = list(stdin.readline().strip())
n2 = list(stdin.readline().strip())
r = ''.join('1' if d1 != d2 else '0' for d1, d2 in zip(n1, n2))

stdout.write(f'{r}\n')
