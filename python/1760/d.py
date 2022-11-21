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
    n = read_int()
    a = read_ints()

    result = []
    for a1, a2 in zip(a, a[1:]):
        if a1 < a2:
            result.append(1)
        elif a1 > a2:
            result.append(-1)
        else:
            # same height, do nothing
            pass

    if result == sorted(result):
        yes()
    else:
        no()    
