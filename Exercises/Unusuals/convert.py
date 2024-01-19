def bin_to_dec(tab):
    tab.reverse()
    c = 0
    for i in range(len(tab)):
        if tab[i] == 1:
            c = c + 2 ** i
    return c

def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal