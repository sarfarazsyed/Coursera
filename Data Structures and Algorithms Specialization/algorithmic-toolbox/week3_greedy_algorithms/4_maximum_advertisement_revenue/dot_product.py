# Uses python3

import sys


def max_dot_product(a, b):
    return sum([x * y for x, y in zip(sorted(a), sorted(b))])


if __name__ == '__main__':
    inp = sys.stdin.read()
    data = list(map(int, inp.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
