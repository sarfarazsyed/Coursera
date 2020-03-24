# Uses python3
import sys
import random


# def lcm_naive(a, b):
#     for l in range(1, a * b + 1):
#         if l % a == 0 and l % b == 0:
#             return l
#
#     return a * b


def gcd_opt(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm_opt(x, y):
    return (x * y) // gcd_opt(x, y)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_opt(a, b))
    # while True:
    #     a = random.randint(1, 10 ** 2)
    #     b = random.randint(1, 10 ** 2)
    #     r1 = lcm_naive(a, b)
    #     r2 = lcm_opt(a, b)
    #     if r1 == r2 :
    #         print("OK")
    #     else:
    #         print("Unmatched :", a, b, r1, r2)
    #         break
