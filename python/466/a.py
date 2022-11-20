from sys import stdin, stdout

def write(s):
    stdout.write(f'{s}\n')

yes = lambda: write('YES')
no = lambda: write('NO')

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


n, m, a, b = read_ints()

def test(n, m, a, b):
    # Special ticket is cheaper than individual ticket
    if b < a:
        q, r = divmod(n, m)
        s = 1 if r != 0 else 0
        return (q + s)*b

    # Special tick covers more than required number of journeys.
    # But it's still cheaper to buy than individual tickets.
    if m > n and b < n*a:
        return b

    # The special ticket is no cheaper than `m` standard tickets.
    if a*m <= b:
        return n*a

    q, r = divmod(n, m)
    return q*b + r*a


t = test(n, m, a, b)
write(t)
