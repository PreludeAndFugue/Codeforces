#!python3

from sys import stdin, stdout

n = int(stdin.readline())
t = ('I love' if i % 2 else 'I hate' for i in range(n))
t = ' that '.join(t) + ' it'

stdout.write(f'{t}\n')
