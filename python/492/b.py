from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda _: write('YES')
no = lambda _: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


n, l = read_ints()
a = read_ints()

a.sort()

distances = []
for a1, a2 in zip(a, a[1:]):
    distances.append((a2 - a1)/2)

if a[0] != 0:
    distances.append(a[0])

if a[-1] != l:
    distances.append(l - a[-1])

m = max(distances)
write(m)
