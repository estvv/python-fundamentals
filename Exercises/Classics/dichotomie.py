from random import *

def dichotomie(t, v):
    g, d = 0, len(t)
    c = 0
    while True:
        m = (g + d) // 2
        if v > d or v < g:
            return False
        if v < m:
            d = m - 1
        elif v>m:
            g = m + 1
        elif v == g or v == d or v == m:
            return True

tab = [0,1,3,4,5,6,7,8]
c = randint(-2, 10)
print(c)
print(tab)
print(ordi(tab,c))
