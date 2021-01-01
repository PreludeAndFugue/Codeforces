#!python3

from itertools import accumulate
from sys import stdin, stdout


def solve():
    _ = int(stdin.readline().strip())
    rs = map(int, stdin.readline().strip().split())
    _ = int(stdin.readline().strip())
    bs = map(int, stdin.readline().strip().split())

    r_accumulator = accumulate(rs)
    b_accumulator = accumulate(bs)
    r_max = max(0, max(r_accumulator))
    b_max = max(0, max(b_accumulator))
    max_sum = r_max + b_max
    stdout.write(f'{max_sum}\n')


n = int(stdin.readline().strip())
for _ in range(n):
    solve()
