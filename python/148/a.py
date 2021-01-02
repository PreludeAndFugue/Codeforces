#!python3

from sys import stdin, stdout

k = int(stdin.readline())
l = int(stdin.readline())
m = int(stdin.readline())
n = int(stdin.readline())
d = int(stdin.readline())

count = 0
for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        count += 1

stdout.write(f'{count}\n')
