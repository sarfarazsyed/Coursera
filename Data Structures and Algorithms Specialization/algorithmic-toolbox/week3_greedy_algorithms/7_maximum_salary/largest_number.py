# Uses python3

import sys


def largest_number(a):
    l = len(max(a, key=len))
    return ''.join(
        list(map(lambda x: x.replace('~', ''), sorted(list(map(lambda x: x.ljust(l, '~'), a)), reverse=True))))


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

'''
n = int(input())
lst = [int(i) for i in input().split()]


def isGE(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def ln(lst):
    answer = []

    while lst != []:
        max_digit = 0
        for digit in lst:
            if isGE(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        lst.remove(max_digit)

    return answer


print(''.join([str(i) for i in ln(lst)]))
'''
