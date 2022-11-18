
from sys import stdin, stdout

s = stdin.readline().strip()

find = 'hello'
i = 0

for c in s:
    if c == find[i]:
        i += 1

    if i == 5:
        stdout.write('YES\n')
        break
else:
    stdout.write('NO\n')
