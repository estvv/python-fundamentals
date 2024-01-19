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
