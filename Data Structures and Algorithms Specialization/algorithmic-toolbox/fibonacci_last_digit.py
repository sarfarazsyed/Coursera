n = int(input())
if n<=1:
    print(n)
    quit()
def fib(n):
    a, b = 0, 1
    for _ in range(n-1):
        c = a + b
        b, a = c, b
    print(c%10)
fib(n)
