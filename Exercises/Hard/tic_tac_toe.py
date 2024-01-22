from random import *
import time
t=[["*","*","*"],["*","*","*"],["*","*","*"]]
o=""
j=""
def debutjeu():
    print("Vous avez le choix entre joueur 1: X et joueur 2: O")
    print("L'ordinateur prendra le choix restant.")
    j1=input("Quel joueur souhaitez-vous être ?\n")
    m=0
    while m==0:
        if j1=="1" or j1=="X":
            j1="X"
            j2="O"
            print("Vous avez choisi le joueur 1, vous serez donc la croix X et l'ordinateur sera le rond O")
            time.sleep(3)
            m=1
            return j1,j2
        elif j1=="2" or j1=="O":
            j1="O"
            j2="X"
            print("Vous avez choisi le joueur 2, vous serez donc le rond O et l'ordinateur sera la croix X")
            time.sleep(3)
            m=2
            return j2,j1
        else:
            print("Ne trichez pas !!! Choississez 1 ou 2")
            m=3
    if m==3:
        debutjeu()

j,o=debutjeu()

def pileouface(j1,j2):
    joueur1=0
    joueur2=0
    pileouface=[randint(1,2) for i in range(49)]
    for i in range(len(pileouface)):
        if pileouface[i]==1:
            joueur1+=1
        else:
            joueur2+=1
    if joueur1>joueur2:
        return j1
    else:
        return j2

def tirage(j1,j2):
    print("Vous allez être tiré au sort pour savoir qui joue en premier.")
    time.sleep(3)
    if pileouface(j1,j2)==j1:
        print("Le joueur qui jouera en premier sera le joueur 1.")
        time.sleep(3)
        return j1
    elif pileouface(j1,j2)==j2:
        print("Le joueur  qui jouera en premier sera le joueur 2.")
        time.sleep(3)
        return j2

def coup_possible(t,l,c):
    if t[l][c]!="*":
        c=0
        return c
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i]=="*":
                c=1
                return c
    c=2
    return c

def coup(jc,t):
    time.sleep(1)
    l=int(input("Choississez l'emplacement dans lequel vous souhaitez jouer votre coup en donnant la ligne: "))
    c=int(input("Choississez l'emplacement dans lequel vous souhaitez jouer votre coup en donnant la colonne: "))
    time.sleep(2)
    if coup_possible(t,l,c)==1:
        print("Vous ne pouvez pas faire ce coup ! Quelqu'un a déjà joué dessus !")
        coup(j,t)
    elif coup_possible(t,l,c)==0:
        return (l,c)

def changetab(jc,t):
    p,s=coup(jc,t)
    t[p][s]=jc
    return t

def changetabordi(oc,t):
    m=coupordinateur(oc,t)
    t[m[0]][m[1]]=oc
    return t

def coupordinateur(oc,t):
    l=randint(0,2)
    c=randint(0,2)
    if coup_possible(t,l,c)==0:
        t[l][c]=oc
    else:
        coupordinateur(oc,t)
    return t

def gagner():
    if coup_possible==3:
        print("Match nul")
        return True
    for i in range(3):
        if t[0][i]==t[1][i]==t[2][i]:
            if t[0][i]==t[1][i]==t[2][i]=="X":
                print("La partie est finie ! Le joueur 1 a gagné !")
                return True
            elif t[0][i]==t[1][i]==t[2][i]=="O":
                print("La partie est finie ! Le joueur 2 a gagné !")
                return True
            else:
                return False
    for i in range(3):
        if t[i][0]==t[i][1]==t[i][2]:
            if t[i][0]==t[i][1]==t[i][2]=="X":
                print("La partie est finie ! Le joueur 1 a gagné !")
                return True
            elif t[i][0]==t[i][1]==t[i][2]=="O":
                print("La partie est finie ! Le joueur 2 a gagné !")
                return True
            else:
                return False
    for i in range(3):
        if t[0][0]==t[1][1]==t[2][2] or t[0][2]==t[1][1]==t[2][0]:
            if t[0][0]==t[1][1]==t[2][2]=="X" or t[0][2]==t[1][1]==t[2][0]=="X":
                print("La partie est finie ! Le joueur 1 a gagné !")
                return True
            elif t[0][0]==t[1][1]==t[2][2]=="X" or t[0][2]==t[1][1]==t[2][0]=="O":
                print("La partie est finie ! Le joueur 2 a gagné !")
                return True
            else:
                return False

def partie():
    i=0
    t=[["*","*","*"],["*","*","*"],["*","*","*"]]
    premier=tirage(j,o)
    if premier==j:
        while gagner()!=True:
            print("----")
            for i in range(len(t[i])):
                    print(t[1])
            print("----")
            t=changetab(j,t)
            print("----")
            for i in range(len(t[i])):
                    print(t[1])
            print("----")
            t=changetab(o,t)
    else:
        while gagner()!=True:
            print("----")
            for i in range(len(t[i])):
                    print(t[1])
            print("----")
            t=changetab(o,t)
            print("----")
            for i in range(len(t[i])):
                    print(t[1])
            print("----")
            t=changetab(j,t)
partie()
