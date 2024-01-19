def h(m1, m2):
    l1, l2 = len(m1), len(m2)
    count = 0
    i = 0
    while i < len(m1) and i < len(m2):
        if m1[i] != m2[i]:
            count += 1
        i += 1
    return count + abs(len(m1) - len(m2))

def mots_voisins(word, array):
    for i in range(len(array)):
        print("Le mot du lexique", array[i],"est à une distance", h(word, array[i]),"du mot", word)

mots_voisins("ok", ["oka", "okee", "k"])
