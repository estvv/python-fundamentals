class Noeud:
    def __init__(self,g,v,d):
        self.g=g
        self.v=v
        self.d=d

def feuille(a):
    if a.g == None and a.d == None:
        print(a.v+" ",end="")
    else:
        if a.g != None:
            feuille(a.g)
        if a.d != None:
            feuille(a.d)

def taille(a):
    if a==None:
        return 0
    else:
        return taille(a.g)+taille(a.d)+1

def hauteur(a):
    if a==None:
        return 0
    else:
        return max(hauteur(a.g),hauteur(a.d))+1

def profond(a):
    if a is None:
        return None
    else:
        profond(a.g)
        print(a.v)
        profond(a.d)

def parfait(a):
    if (a.g != None and a.d == None) or (a.g == None and a.d != None):
        return False
    if a.g == None and a.d == None:
        return True
    return parfait(a.g) and parfait(a.d)

def profondVAL(a):
    if a is None:
        return None
    else:
        print("(",end="")
        profondVAL(a.g)
        print(a.v,end="")
        profondVAL(a.d)
        print(")",end="")

def gparfait(h):
    if h==0:
        return Noeud(None,h,None)
    else:
        return Noeud(None,h,gparfait(h-1))
