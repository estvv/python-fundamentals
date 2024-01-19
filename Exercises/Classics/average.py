print("Quel est le nombre de copies ?")
nmbcopies = int(input())
t = [0] * nmbcopies

for i in range(nmbcopies):
    print("Quelle est la note de l'élève numéro", i + 1 , "?")
    t[i] = int(input())

def moyenne(t):
    num = 0
    for i in range(len(t)):
        num = num + i * t[i]
    moyenne = num / len(t)
    print("La moyenne de la classe est de", moyenne)

moyenne(t)
