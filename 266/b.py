#!python3

from sys import stdin, stdout

n, t = map(int, stdin.readline().strip().split(' '))
queue = stdin.readline().strip()

elements = list(queue)
for _ in range(t):
    swaps = []
    for i, (x, y) in enumerate(zip(elements, elements[1:])):
        if x == 'B' and y == 'G':
            swaps.append(i)
    for s in swaps:
        elements[s] = 'G'
        elements[s + 1] = 'B'
result = ''.join(elements)

stdout.write(f'{result}\n')
