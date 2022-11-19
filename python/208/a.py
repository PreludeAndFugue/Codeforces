from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda _: write('YES')
no = lambda _: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


s = stdin.readline().strip()

while s.startswith('WUB'):
    s = s[3:]

while s.endswith('WUB'):
    s = s[:-3]

s = s.split('WUB')
s = [t for t in s if t]
s = ' '.join(s)

write(s)
