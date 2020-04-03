def fibonacci_iterative(n):
    previous = 0
    current = 1
    if n <= 1:
        return n
    else:
        for i in range(2, n+1):
            current, previous = current + previous, current
        return fibo[n]


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_dynamic(n):
    fibo = {}
    fibo[0] = 0
    fibo[1] = 1
    for i in reversed(range(n + 1)):
        if i in fibo:
            return fibo[i]
        else:
            fibo[i] = fibo[i - 1] + fibo[i - 2]
            return fibo[i]