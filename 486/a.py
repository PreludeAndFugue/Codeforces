#!python3

from sys import stdin, stdout

n = int(stdin.readline())

def f(n):
    if n == 1:
        return -1
    if n % 2:
        return n // 2 - n
    else:
        return n // 2

stdout.write(f'{f(n)}\n')
