def ordi():
    t = [i for i in range(101)]
    g,d = 0,len(t) - 1
    print("Choisissez un nombre entre 0 et 100 mais ne le dites pas à l'ordi !!")
    r = ""
    while r != "=":
        m = (g + d) // 2
        print(m,"votre nombre ? +, - ou = ?")
        r = input()
        if r == "-":
            d = m - 1
        elif r == "+":
            g = m + 1
    print("c'est bon, votre chiffre est", m)

ordi()