def cesar(message, decalage):
    resultat = ""
    for lettre in message:
        if lettre >= 'A' and lettre <= 'Z':
            resultat = resultat + chr(((ord(lettre) - 65) + decalage) % 26 + 65)
        elif lettre >= 'a' and lettre <= 'z':
            resultat = resultat + chr(((ord(lettre) - 97) + decalage) % 26 + 97)
        else:
            resultat = resultat + lettre
    return resultat
