
from sys import stdin, stdout

lucky = [
    4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 774, 777
]

n = int(stdin.readline().strip())

for m in lucky:
    if m > n:
        stdout.write('NO\n')
        break
    if n % m == 0:
        stdout.write('YES\n')
        break
else:
    stdout.write('NO\n')
