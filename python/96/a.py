
from sys import stdin, stdout

s = stdin.readline().strip()

current = s[0]
count = 0

for c in s:
    if c == current:
        count += 1
    else:
        count = 1

    if count >= 7:
        stdout.write('YES\n')
        break

    current = c
else:
    stdout.write('NO\n')
