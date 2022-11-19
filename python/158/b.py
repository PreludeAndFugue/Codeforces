from sys import stdin, stdout

from collections import Counter

def write(s):
    stdout.write(f'{s}\n')

yes = lambda _: write('YES')
no = lambda _: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))

n = read_int()
s = read_ints()
c = Counter(s)


while c[2] >= 2:
    c[2] -= 2
    c[4] += 1


while c[1] > 0 and c[3] > 0:
    c[1] -= 1
    c[3] -= 1
    c[4] += 1


while c[1] >= 2 and c[2] >= 1:
    c[1] -= 2
    c[2] -= 1
    c[4] += 1


while c[1] >= 4:
    c[1] -= 4
    c[4] += 1


while c[1] > 0 and c[2] > 0:
    c[1] -= 1
    c[2] -= 1
    c[4] += 1


if c[1] > 0:
    c[1] = 0
    c[4] += 1


s = sum(c.values())
write(s)
