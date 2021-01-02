#!python3

from sys import stdin, stdout

n, h = map(int, stdin.readline().strip().split(' '))
heights = map(int, stdin.readline().strip().split(' '))

width = 0
for a in heights:
    width += 1 if a <= h else 2

stdout.write(f'{width}\n')
