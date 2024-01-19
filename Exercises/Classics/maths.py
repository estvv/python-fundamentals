def factorial(m):
    if m == 0:
        return 1
    else:
        return factorial(m - 1) * m

def pgcd(a, b):
    if b == 0:
        return a
    else:
        a, b = b, a%b
        return pgcd(a, b)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
