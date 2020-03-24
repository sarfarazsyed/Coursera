def fibonacci_partial_sum(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c - 1


m, n = map(int, input().split())
if n <= 1:
    print(n)
    quit()
l_n = (n + 2) % 60
l_m = (m + 1) % 60

if l_n <= 1:
    a = l_n - 1
else:
    a = fibonacci_partial_sum(l_n)
if l_m <= 1:
    b = l_m - 1
else:
    b = fibonacci_partial_sum(l_m)
if a >= b:
    print(a - b)
else:
    print(10 + a - b)
