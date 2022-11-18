
from sys import stdin, stdout

test = 'YesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYesYes'

n = int(stdin.readline().strip())

for _ in range(n):
    s = stdin.readline().strip()
    if s in test:
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')
