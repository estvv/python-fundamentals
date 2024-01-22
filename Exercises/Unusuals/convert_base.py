def bin_to_dec(a):
    a.reverse()
    c = 0
    for i in range(len(a)):
        if a[i] == 1:
            c = c + 2 ** i
    return c

def dec_to_bin(a):
    bin_a = str(a % 2)
    a = a // 2
    while a > 0 :
        bin_a = str(a %2 ) + bin_a
        a = a // 2
    return bin_a
