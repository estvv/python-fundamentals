from random import *

# My sort

def my_sort(t):
    for i in range(len(t)):
        for j in range(i, len(t)):
            if (t[i] > t[j]):
                t[i], t[j] = t[j], t[i]

# Bubble sort

def bubble_sort(T):
    for i in range(len(T) - 1, 0, -1):
        for j in range(i):
            if T[j] > T[j + 1]:
                temp = T[j]
                T[j] = T[j + 1]
                T[j + 1] = temp
    return T

# Merge sort

def merge_sort(tab1, tab2):
    n1 =  len(tab1)
    n2 = len(tab2)
    i1 = 0
    i2 = 0
    tab = []
    while i1 < n1 and i2 < n2:
        if tab1[i1] > tab2[i2]:
            tab.append(tab2[i2])
            i2 = i2 + 1
        else :
            tab.append(tab1[i1])
            i1 = i1 + 1
    while i1 < n1 :
        tab.append(tab1[i1])
        i1 = i1 + 1
    while i2 < n2 :
        tab.append(tab2[i2])
        i2 = i2 + 1
    return tab

# Insertion sort

def insertion_sort(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j - 1]:
            tab[j] = tab[j - 1]
            j = j - 1
        tab[j] = valeur_insertion

# Selection sort

def selection_sort(t):
    for i in range(len(t) - 1):
        mini = i
        for j in range(i + 1, len(t)):
            if t[j] < t[mini]:
                mini = j
        t[i], t[mini] = t[mini], t[i]

t = [randint(0, 10) for num in range(randint(1, 10))]

# my_sort(t)
# bubble_sort(t)
# selection_sort(t)
# insertion_sort(t)

for item in t:
    print(item)
