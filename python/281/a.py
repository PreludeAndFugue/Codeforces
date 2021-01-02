#!python3

from sys import stdin, stdout

word = stdin.readline().strip()
word = word[0].upper() + word[1:]

stdout.write(f'{word}\n')
