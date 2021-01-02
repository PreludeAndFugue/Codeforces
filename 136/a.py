#!python3

from sys import stdin, stdout

n = int(stdin.readline())
ps = map(int, stdin.readline().strip().split(' '))
result = [0] * n
for i, p in enumerate(ps, start=1):
    result[p - 1] = i
answer = ' '.join(map(str, result))

stdout.write(f'{answer}\n')
