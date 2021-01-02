#!python3

from sys import stdin, stdout

n = int(stdin.readline())

x = 0
for _ in range(n):
    statement = stdin.readline()
    if '+' in statement:
        x += 1
    else:
        x -=1

stdout.write(f'{x}\n')
