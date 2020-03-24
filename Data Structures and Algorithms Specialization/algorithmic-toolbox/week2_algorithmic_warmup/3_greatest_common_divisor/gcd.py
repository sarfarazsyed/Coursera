# Uses python3
import sys


def gcd_opt(x, y):
    while y:
        x, y = y, x % y
    return x


if __name__ == "__main__":
    inp = sys.stdin.read()
    a, b = map(int, inp.split())
    print(gcd_opt(a, b))
