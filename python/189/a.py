from sys import stdin, stdout
# from sys import setrecursionlimit
# from functools import cache

# setrecursionlimit(9_000)

from itertools import product
from operator import mul

def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


n, a, b, c = read_ints()

counts = []
cuts = sorted(set([a, b, c]))

# @cache
# def subtract(m, count):
#     for c in cuts:
#         y = m - c
#         if y > 0:
#             subtract(y, count + 1)
#         elif y == 0:
#             counts.append(count + 1)
#         else:
#             # do nothing
#             pass


def test(a, b, c, n):
    if a == 1 or b == 1 or c == 1:
        return n
    if (a == 2 or b == 2 or c == 2) and n%2 == 0:
        return n//2
    m = 0
    for i in range(n//a + 1):
        # print(i, a)
        a_i = a*i
        if a_i > n:
            break
        for j in range(n//b + 1):
            # print(j, b)

            b_j = b*j
            if a_i + b_j > n:
                break
            for k in range(n//c + 1):
                # print(k, c)
                c_k = c*k
                if a_i + b_j + c_k > n:
                    break
                if a_i + b_j + c_k == n:
                    # print(i, j, k, m)
                    m = max(m, i + j + k)
    return m


def test1(values, n):
    if a == 1 or b == 1 or c == 1:
        return n
    if (a == 2 or b == 2 or c == 2) and n%2 == 0:
        return n//2
    m = 0
    ranges = [range(n//x + 1) for x in values]
    for x in product(*ranges):
        t = sum(mul(*y) for y in zip(values, x))
        if t == n:
            m = max(m, sum(x))
    return m


if len(cuts) == 3:
    m = test(a, b, c, n)
else:
    m = test1(cuts, n)

write(m)


# print(run())
