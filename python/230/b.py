from sys import stdin, stdout

from math import isqrt


def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


def spp(n, a):
    '''
    Checks whether n is a strong probable prime base a.

    https://primes.utm.edu/prove/prove2_3.html
    '''
    s, d = factor2(n - 1)
    if pow(a, d, n) == 1:
        return True
    for r in range(s):
        if pow(a, d*(2**r), n) == n - 1:
            return True
    return False


def factor2(n):
    '''
    When n is even, finds out how many factors of 2 n contains
    that is n=2**s*x, x odd
    '''
    s = 0
    while n%2 == 0:
        s += 1
        n = n//2
    return s, n


def is_prime(n):
    '''
    Works for n < 25,326,001

    https://primes.utm.edu/prove/prove2_3.html
    '''
    if n in set([2, 3, 5]):
        return True
    for p in [2, 3, 5]:
        if not spp(n, p):
            return False
    return True


def is_t_prime(n):
    '''
    n must be a square and the sqrt must be prime.
    '''
    if n == 1:
        return False
    m = isqrt(n)
    if m**2 != n:
        return False
    return is_prime(m)


n = read_int()
x = read_ints()

cache = dict()

for i in x:
    if i in cache:
        write(cache[i])
    else:
        if is_t_prime(i):
            cache[i] = 'YES'
            yes()
        else:
            cache[i] = 'NO'
            no()
