#!python3

from sys import stdin, stdout

ns = '+'.join(sorted(stdin.readline().strip().split('+')))

stdout.write(f'{ns}\n')
