from random import *

def motrdm():
    mdp = ""
    KEY = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*&~#!?_"
    LENGHT = randint(10, 20)
    for i in range(LENGHT):
        mdp = mdp + KEY[randint(0, len(KEY) - 1)]
    return mdp

def inverse(c):
    if c=="":
        return c
    else:
        return c[-1] + inverse(c[:-1])
