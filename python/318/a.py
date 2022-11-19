
from sys import stdin, stdout


n, k = list(map(int, stdin.readline().strip().split()))

if n % 2 == 0:
    # even number of elements
    m = n // 2
else:
    m = n // 2 + 1

if k <= m:
    # an odd number
    a = 2*k - 1
    stdout.write(f'{a}\n')
else:
    # an even number
    k -= m
    a = 2 * k
    stdout.write(f'{a}\n')
