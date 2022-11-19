
from sys import stdin, stdout
from operator import add, mul

def yes():
    stdout.write('YES\n')

def no():
    stdout.write('NO\n')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))

OPERATORS = [
    [add, add],
    [add, mul],
    [mul, add],
    [mul, mul]
]


a = read_int()
b = read_int()
c = read_int()

m = 0
for op1, op2 in OPERATORS:
    x = op1(a, op2(b, c))
    m  = max(m, x)
    y = op2(op1(a, b), c)
    m = max(m, y)

stdout.write(f'{m}\n')
