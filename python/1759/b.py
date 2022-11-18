
from sys import stdin, stdout

sums = set()
sums_max = dict()
i = 0
for j in range(1, 200):
    i += j
    sums.add(i)
    sums_max[i] = j

n = int(stdin.readline().strip())

for _ in range(n):
    m, s = list(map(int, stdin.readline().strip().split()))
    bs = list(map(int, stdin.readline().strip().split()))

    total = sum(bs) + s
    if total in sums:
        a = sums_max[total]
        items = set(range(1, a + 1))
        b_set = set(bs)
        if b_set <= items:
            stdout.write('YES\n')
        else:
            stdout.write('NO\n')
    else:
        stdout.write('NO\n')
