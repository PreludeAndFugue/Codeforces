'''
Prime numbers.
'''

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
    if n in {2, 3, 5}:
        return True
    for p in [2, 3, 5]:
        if not spp(n, p):
            return False
    return True
