from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda _: write('YES')
no = lambda _: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


w = stdin.readline().strip()

if w.isupper():
    w = w.lower()
else:
    start_is_lower = w[0].islower()
    rest = w[1:]
    if rest:
        if start_is_lower and rest.isupper():
            w = w.title()
    else:
        if start_is_lower:
            w = w.title()


write(w)
