from sys import stdin, stdout

from math import ceil

def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


def run(k, a, c, d):
    total = 0
    step = k + 1
    for i, ai in enumerate(a):
        l = len(range(i, d, step))
        total += ai * l
    if total >= c:
        return k
    else:
        return None


def test(a, c, d):
    a.sort(reverse=True)
    for k in range(d, -1, -1):
        x = run(k, a, c, d)
        if x is not None:
            if x == d:
                return 'Infinity'
            else:
                return f'{k}'
    return 'Impossible'


t = read_int()

for _ in range(t):
    n, c, d = read_ints()
    a = read_ints()

    x = test(a, c, d)
    write(x)

