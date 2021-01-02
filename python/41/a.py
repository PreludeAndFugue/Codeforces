#!python3

from sys import stdin, stdout

s = stdin.readline().strip()
t = stdin.readline().strip()

answer = 'YES' if s == t[::-1] else 'NO'

stdout.write(f'{answer}\n')
