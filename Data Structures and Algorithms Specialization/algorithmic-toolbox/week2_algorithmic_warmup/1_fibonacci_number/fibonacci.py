# Uses python3
def calc_fib_opt(n):
    a = 1
    b = 1
    if n <= 1:
        return n
    for i in range(2, n):
        a, b = b, a + b
    return b


n = int(input())
print(calc_fib_opt(n))
