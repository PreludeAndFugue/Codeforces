#!python3

from sys import stdin, stdout

n = int(stdin.readline().strip())

if n > 2 and n % 2 == 0:
    stdout.write('YES')
else:
    stdout.write('NO')
