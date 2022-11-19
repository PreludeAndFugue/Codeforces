
from sys import stdin, stdout

instructions = set(['H', 'Q', '9'])

p = stdin.readline().strip()

for c in p:
    if c in instructions:
        stdout.write('YES\n')
        break
else:
    stdout.write('NO\n')
