from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda _: write('YES')
no = lambda _: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


n = read_int()
a = read_ints()

i = 0
j = 1
m = 1

for j in range(1, n):
    if a[j - 1] <= a[j]:
        m = max(m, j - i + 1)
    else:
        i = j

write(m)
