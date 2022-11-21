from sys import stdin, stdout

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
    a, b, c = read_ints()

    items = [a, b, c]
    items.sort()
    m = items[1]

    write(m)
