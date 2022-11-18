
from sys import stdin, stdout

def read_int():
    return int(stdin.readline().strip())

def read_ints():
    return list(map(int, stdin.readline().strip().split()))


def test(l, r, x, a, b):
    a, b = sorted([a, b])
    diff = b - a

    if diff == 0:
        return 0

    if diff >= x:
        return 1

    # diff < x
    
    if a == l:
        if r - b < x:
            return -1
        else:
            return 2

    if a - l >= x:
        return 2




    return -1


# n = read_int()
# for _ in range(n):
#     l, r, x = read_ints()
#     a, b = read_ints()

#     result = test(l, r, x, a, b)
#     stdout.write(f'{result}\n')


if __name__ == '__main__':
    tests = [
        [3, 5, 6, 3, 3, 0],
        [0, 15, 5, 4, 5, 2],
        [0, 10, 5, 3, 7, 3],
        [3, 5, 6, 3, 4, -1],
        [-10, 10, 11, -5, 6, 1],
        [-3, 3, 4, 1, 0, -1],
        [-5, 10, 8, 9, 2, 3],
        [1, 5, 1, 2, 5, 1],
        [-1, 4, 3, 0, 2, 3],
        [-6, 3, 6, -1, -4, -1],
    ]

    for l, r, x, a, b, ans in tests:
        result = test(l, r, x, a, b)
        print(l, r, x, a, b, ans, result)