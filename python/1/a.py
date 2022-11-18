
from sys import stdin, stdout

m, n, a = list(map(int, stdin.readline().strip().split()))

x = m // a + (1 if m % a else 0)
y = n // a + (1 if n % a else 0)

stdout.write(f'{x * y}\n')
