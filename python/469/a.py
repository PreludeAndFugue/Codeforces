#!python3

from sys import stdin, stdout

n = int(stdin.readline())
x = list(map(int, stdin.readline().strip().split(' ')[1:]))
y = list(map(int, stdin.readline().strip().split(' ')[1:]))
s = set(x + y)

answer = 'I become the guy.' if len(s) == n else 'Oh, my keyboard!'

stdout.write(f'{answer}\n')
