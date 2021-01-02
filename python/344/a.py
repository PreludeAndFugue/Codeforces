#!python3

from sys import stdin, stdout

n = int(stdin.readline())

previous = None
groups = 0
for _ in range(n):
    magnet = stdin.readline().strip()
    if magnet != previous:
        groups += 1
        previous = magnet


stdout.write(f'{groups}\n')
