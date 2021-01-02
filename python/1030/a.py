#!python3

from sys import stdin, stdout

n = int(stdin.readline())

s = sum(map(int, stdin.readline().strip().split(' ')))
answer = 'HARD' if s > 0 else 'EASY'

stdout.write(f'{answer}\n')
