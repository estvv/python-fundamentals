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
