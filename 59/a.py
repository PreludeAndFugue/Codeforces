#!python3

from sys import stdin, stdout

word = stdin.readline().strip()

lower_count = 0
upper_count = 0
for ch in word:
    if ch.islower():
        lower_count += 1
    else:
        upper_count += 1

if lower_count >= upper_count:
    word = word.lower()
else:
    word = word.upper()

stdout.write(f'{word}\n')
