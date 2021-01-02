#!python3

from collections import Counter
from sys import stdin, stdout

n = map(int, list(stdin.readline().strip()))
c = Counter(n)
s = c[4] + c[7]
a = 'YES' if s == 4 or s == 7 else 'NO'

stdout.write(f'{a}\n')
