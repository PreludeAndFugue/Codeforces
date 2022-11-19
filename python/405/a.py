#!python3

from sys import stdin, stdout

def yes():
    stdout.write('YES\n')

def no():
    stdout.write('NO\n')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))

n = read_int()
ai = read_ints()
ai.sort()

stdout.write(' '.join(str(a) for a in ai))
stdout.write('\n')
