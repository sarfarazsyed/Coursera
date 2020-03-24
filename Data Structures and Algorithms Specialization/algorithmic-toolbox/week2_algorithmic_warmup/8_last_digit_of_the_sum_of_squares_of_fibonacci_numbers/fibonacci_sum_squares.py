def fibo(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        c = c % 10
        b, a = c, b
    return c


n = int(input())
l_n = n % 100
l_np = (n + 1) % 100

if l_n <= 1:
    a = l_n
else:
    a = fibo(l_n)
if l_np <= 1:
    b = l_np
else:
    b = fibo(l_np)

print((a * b) % 10)
