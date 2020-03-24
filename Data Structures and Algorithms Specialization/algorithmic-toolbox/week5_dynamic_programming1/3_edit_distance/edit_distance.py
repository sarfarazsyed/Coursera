# Uses python3
def edit_distance(s, t):
    ls = (len(s) + 1)
    lt = (len(t) + 1)
    ds = [[_ for _ in range(ls)]] + [[_] + [0] * (ls - 1) for _ in range(1, lt)]
    for i in range(1, lt):
        for j in range(1, ls):
            tmp1 = ds[i - 1][j] + 1
            tmp2 = ds[i][j - 1] + 1
            tmp3 = 0
            if (s[j - 1] == t[i - 1]):
                tmp3 = ds[i - 1][j - 1]
            else:
                tmp3 = ds[i - 1][j - 1] + 1
            ds[i][j] = min(tmp1, tmp2, tmp3)
    return ds[lt - 1][ls - 1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
