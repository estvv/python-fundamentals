def deplacer(a, b, c, k):
    if k == 1:
        print(a,"vers",b)
    elif k == 2:
        deplacer(a, c, b, 1)
        deplacer(a, b, c, 1)
        deplacer(c, b, a, 1)
    else:
        deplacer(a, c, b, k - 1)
        deplacer(a, b, c, 1)
        deplacer(c, b, a, k - 1)

deplacer("a","b","c",5)
