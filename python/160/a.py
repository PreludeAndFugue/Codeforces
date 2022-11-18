
from sys import stdin, stdout

n = stdin.readline().strip()

coins = sorted(map(int, stdin.readline().strip().split()), reverse=True)
s = sum(coins) / 2
t = 0
for i, c in enumerate(coins):
    t += c
    if t > s:
        stdout.write(f'{i + 1}\n')
        break
