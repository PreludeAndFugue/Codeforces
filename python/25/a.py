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
m = read_ints()

evens = []
odds = []

for i, a in enumerate(m):
    if a % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

if len(evens) == 1:
    write(evens[0] + 1)
else:
    write(odds[0] + 1)
