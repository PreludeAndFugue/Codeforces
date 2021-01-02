#!python3

from sys import stdin, stdout

n = int(stdin.readline())

not_distinct = True
while not_distinct:
    n += 1
    c = set(str(n))
    if len(c) == 4:
        break

stdout.write(f'{n}\n')
