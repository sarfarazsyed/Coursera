# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    a = {}
    for _ in range(len(weights)):
        a[values[_] / weights[_]] = _
    for _ in sorted(a.keys(), reverse=True):
        if capacity == 0:
            break
        mi = min(weights[a[_]], capacity)
        value += mi * (_)
        weights[a[_]] -= mi
        capacity -= mi
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
