from sys import stdin, stdout

from collections import Counter

def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


t = read_int()

for _ in range(t):
    n = read_int()
    s = read_ints()

    m = max(s)
    unique = set(s)

    s1 = [x - m for x in s]

    if len(unique) > 1:
        s_sorted = sorted(s)
        m1 = s_sorted[-2]
        for i, x in enumerate(s1):
            if x == 0:
                s1[i] = m - m1

    write(' '.join(str(x) for x in s1))
