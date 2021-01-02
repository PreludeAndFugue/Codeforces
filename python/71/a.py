#!python3

from sys import stdin, stdout

n = int(stdin.readline())

for _ in range(n):
    word = stdin.readline().strip()
    n = len(word)
    if n <= 10:
        stdout.write(f'{word}\n')
    else:
        f = word[0]
        l = word[-1]
        d = n - 2
        stdout.write(f'{f}{d}{l}\n')
