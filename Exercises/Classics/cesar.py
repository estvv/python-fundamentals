def cesar(message, decalage):
    resultat = ""
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = (position_alphabet(c) + decalage) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c
    return resultat
