#!python3

from sys import stdin, stdout

a, b = map(int, stdin.readline().strip().split(' '))

i = 0
while a <= b:
    a *= 3
    b *= 2
    i += 1

stdout.write(f'{i}\n')
