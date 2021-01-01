#!python3

from sys import stdin, stdout

s1 = stdin.readline().strip().lower()
s2 = stdin.readline().strip().lower()

if s1 < s2:
    stdout.write('-1\n')
elif s1 == s2:
    stdout.write('0\n')
else:
    stdout.write('1\n')
