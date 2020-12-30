#!python3

from sys import stdin, stdout

test_count = int(stdin.readline())
for _ in range(test_count):
    l = int(stdin.readline())
    notes = map(int, stdin.readline().strip().split(' '))
    m = 0
    count = 0
    for n in notes:
        if m < n:
            count += 1
            m = n
        elif m == n:
            m = n + 1
            count += 1
        elif m > n:
            pass
    stdout.write(f'{count}\n')
