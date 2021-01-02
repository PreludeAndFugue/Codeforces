#!python3

from collections import Counter
from sys import stdin, stdout

n = int(stdin.readline())
games = stdin.readline().strip()
count = Counter(games)
if count['A'] > count['D']:
    answer = 'Anton'
elif count['A'] < count['D']:
    answer = 'Danik'
else:
    answer = 'Friendship'

stdout.write(f'{answer}\n')
