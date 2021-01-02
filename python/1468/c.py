#!python3

from queue import PriorityQueue, Queue
import sys

class Customer(object):
    def __init__(self, i):
        self.i = i
        self.seen = False

    def __lt__(self, other):
        return self.i < other.i


def parse_input():
    test_count = int(sys.stdin.readline())
    poly_customers = PriorityQueue()
    mono_customers = Queue()
    i = 0
    for _ in range(test_count):
        line = sys.stdin.readline().strip()
        if line.startswith('1'):
            a, b = line.split(' ', maxsplit=1)
            a, b = int(a), int(b)
            i += 1
            c = Customer(i)
            poly_customers.put((-b, c))
            mono_customers.put(c)
        else:
            c = int(line)
            if c == 2:
                yield get_mono(mono_customers)
                # sys.stdout.write(f'{o}\n')
            elif c == 3:
                yield get_poly(poly_customers)
                # sys.stdout.write(f'{o}\n')
            else:
                raise Exception


def get_mono(mono_customers):
    c = mono_customers.get()
    while c.seen:
        c = mono_customers.get()
    c.seen = True
    return c.i


def get_poly(poly_customers):
    _, c = poly_customers.get()
    while c.seen:
        _, c = poly_customers.get()
    c.seen = True
    return c.i


def main():
    for o in parse_input():
        sys.stdout.write(f'{o}\n')


main()
