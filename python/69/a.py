
from sys import stdin, stdout

n = int(stdin.readline().strip())

X = 0
Y = 0
Z = 0

for _ in range(n):
    x, y, z = list(map(int, stdin.readline().strip().split()))
    X += x
    Y += y
    Z += z

if X == 0 and Y == 0 and Z == 0:
    stdout.write('YES\n')
else:
    stdout.write('NO\n')
