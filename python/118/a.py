
from sys import stdin, stdout

vowels = set('aeiouyAEIOUY')

s = stdin.readline().strip()

t = []

for c in s:
    if c in vowels:
        continue
    else:
        t.append('.')
        t.append(c.lower())

stdout.write(f'{"".join(t)}\n')
