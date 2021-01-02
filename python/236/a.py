#!python3

from sys import stdin, stdout

name = stdin.readline().strip()
chrs = set(name)
if len(chrs) % 2 == 0:
    stdout.write('CHAT WITH HER!\n')
else:
    stdout.write('IGNORE HIM!\n')
