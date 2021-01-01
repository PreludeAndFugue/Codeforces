#!python3

from sys import stdin, stdout

n = int(stdin.readline())

colours = iter(stdin.readline().strip())

c = next(colours)
count = 0
for d in colours:
    if d == c:
        count += 1
    else:
        c = d

stdout.write(f'{count}\n')
