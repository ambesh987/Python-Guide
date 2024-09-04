# 0 1 1 2 3 5 8 13 21
def fibonacci(n):
    a = 0
    b = 1
    fib_series = []

    for _ in range(n):
        fib_series.append(a)
        a,b=b,a+b
    return fib_series

n=1000
print(fibonacci(n))


