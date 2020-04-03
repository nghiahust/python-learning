def fibonacci_iterative(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_iterative(n - 1) + fibonacci_iterative(n - 2)