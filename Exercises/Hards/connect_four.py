import random
import time
import copy

def grille_vide():
    t=[[0]*7 for i in range(6)]
    return t

def affiche(g):
    for i in range(len(g)-1,-1,-1):
        line="|"
        for j in range(len(g[0])):
            if g[i][j]==0:
                line+=" . "
            elif g[i][j]==1:
                line+=" X "
            elif g[i][j]==2:
                line+=" O "
        line+="|"
        print(line)
    print(" "+"-"*21)

def coup_possible(g,co):
    return  g[-1][co]==0

def jouer(g,j,co):
    if coup_possible(g,co):
        li=0
        while g[li][co]!=0: 
            li+=1
        g[li][co]=j

def horiz(g,j,li,co):
    if co<4:
        return  g[li][co:co+4].count(j)==4 
    return False

def vert(g,j,li,co):
    t=[0,0,0,0]
    if li<3:
        for i in range(len(t)):
            t[i]=g[li+i][co] 
        return  t.count(j)==4 
    return False

def diag(g,j,li,co):
    t=[0,0,0,0] 
    if li<3 and co<4:  
        for i in range(len(t)):
            t[i]=g[li+i][co+i] 
        if t.count(j)==4:
            return  True
    if li<3 and co>2:
        for i in range(len(t)):
            t[i]=g[li+i][co-i] 
        if t.count(j)==4:
            return  True
    return False

def victoire(g,j):
    for li in range(len(g)):
        for co in range(len(g[0])):
            if horiz(g,j,li,co) or vert(g,j,li,co) or diag(g,j,li,co):
                return True
    return False

def match_nul(g):
    return  g[-1][:].count(0)==0 

def coup_aleatoire(g,j):
    numcolonne=[]
    for co in range(len(g[0])):
        if coup_possible(g,co):
            numcolonne.append(co)
    nbraleatoire=random.randint(0,len(numcolonne)-1)
    jouer(g,j,numcolonne[nbraleatoire])

def coup_aleatoireintelligent(g,j): 
    numcolonne=[]
    for co in range(len(g[0])):
        if coup_possible(g,co):
            numcolonne.append(co)
    for co in numcolonne:
        gprime=copy.deepcopy(g)
        jouer(gprime,j,co)
        if victoire(gprime,j):
            jouer(g,j,co)
            return
    if j==1:
        jautre=2
    else :
        jautre=1
    for co in numcolonne:
        gprime=copy.deepcopy(g)
        jouer(gprime,jautre,co)
        if victoire(gprime,jautre):
            jouer(g,j,co)
            return
    nbraleatoire=random.randint(0,len(numcolonne)-1)
    jouer(g,j,numcolonne[nbraleatoire])

def automate():
    g=grille_vide()
    j1=1
    j2=2
    while (not match_nul(g)): 
        coup_aleatoireintelligent(g,j1)
        affiche(g)
        if victoire(g,j1):
            print("j1 a gagné")
            break
        time.sleep(0.1)
        coup_aleatoireintelligent(g,j2)
        affiche(g)
        if victoire(g,j2):
            print("j2 a gagné")
            break
        time.sleep(0.1)

def jeuContreAuto():
    g=grille_vide()
    j1=1
    j2=2
    while (not match_nul(g)):
        numcol = -1
        coup_aleatoireintelligent(g,j1)
        affiche(g)
        if victoire(g,j1):
            print("L'ordinateur a gagné")
            break
        while numcol < 0 or numcol > 6:
            numcol=int(input("Dans quelle colonne souhaitez-vous jouer ? (0-6) "))
        jouer(g,j2,numcol)
        affiche(g)
        if victoire(g,j2):
            print("Vous avez gagné")
            break

if __name__ == '__main__':
    jeuContreAuto()
    #automate()