from sys import stdin, stdout

from itertools import combinations

def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


def operate_on(a):
    yield a
    for i, x in enumerate(a):
        ca = a.copy()
        if x == 0:
            ca[i] = 1
        else:
            ca[i] = 0
        yield ca


def count_inversions(a):
    c = 0
    for a1, a2 in combinations(a, 2):
        if a1 > a2:
            c += 1
    return c


def count_inversions1(a):
    c1 = 0
    answer = 0
    for x in a:
        if x == 0:
            answer += c1
        else:
            c1 += 1
    return answer


def test(a):
    m = 0
    for b in operate_on(a):
        m = max(m, count_inversions1(b))
    return m


t = read_int()

for _ in range(t):
    t = read_int()
    a = read_ints()

    m = test(a)
    write(m)


# a = [1 for _ in range(200_000)]

# m = test(a)
# print(m)