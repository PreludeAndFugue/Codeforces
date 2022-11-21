from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = {c: i + 1 for i, c in enumerate(alphabet)}

t = read_int()

for _ in range(t):
    n = read_int()
    s = stdin.readline().strip()

    m = max(a[c] for c in s)
    write(m)

