# Uses python3
import sys


def get_change(m):
    coins = [1, 3, 4]
    minC = [0] * (m + 1)
    for M in range(1, m + 1):
        minC[M] = -1
        for i in range(len(coins)):
            if M >= coins[i]:
                nC = minC[M - coins[i]] + 1
                if minC[M] == -1 or nC < minC[M]:
                    minC[M] = nC
    return minC[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
