def ordi():
    t = [i for i in range(101)]
    g, d = 0, len(t) - 1
    print("Choose a number between 0 - 100 but keep it safe !")
    r = ""
    while r != "=":
        m = (g + d) // 2
        print(m,"-> is your number '+', '-' or '=' ?")
        r = input()
        if r == "-":
            d = m - 1
        elif r == "+":
            g = m + 1
    print("c'est bon, votre chiffre est", m)

ordi()