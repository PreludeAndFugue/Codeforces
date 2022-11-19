from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda _: write('YES')
no = lambda _: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


names = {}

n = read_int()
for _ in range(n):
    name = stdin.readline().strip()
    if name in names:
        i = names[name]
        names[name] = i + 1
        write(f'{name}{i}')
    else:
        names[name] = 1
        write('OK')
