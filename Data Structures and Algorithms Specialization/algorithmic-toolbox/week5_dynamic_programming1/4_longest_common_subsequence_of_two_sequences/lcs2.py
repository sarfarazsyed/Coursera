# Uses python3

import sys


def lcs2(s1, s2):
    n1 = len(a)
    n2 = len(b)
    c = 0
    ds = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                ds[i][j] = ds[i - 1][j - 1] + 1
            if s1[i - 1] != s2[j - 1]:
                ds[i][j] = max(ds[i][j - 1], ds[i - 1][j])
    return ds[n1][n2]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
