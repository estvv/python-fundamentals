from random import *

# My sort

def my_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if (array[i] > array[j]):
                array[i], array[j] = array[j], array[i]

# Insertion sort

def glisser(array,i):
    j = i
    val = array[i]
    while j > 0 and array[j - 1] > val:
        array[j], array[j - 1] = array[j - 1], array[j]
        j = j - 1

def insertion_sort(array):
    for i in range(1, len(array)):
        glisser(array, i)

# Selection sort

def ind_minimum(array, i):
    m = i
    for j in range(i + 1, len(array)):
        if array[j] < array[m]:
            m = j
    return m

def selection_sort(array):
    for i in range(len(array)):
        ind_mini = ind_minimum(array, i)
        array[i], array[ind_mini] = array[ind_mini], array[i]

array = [randint(0, 10) for num in range(randint(1, 10))]

# my_sort(array)
# selection_sort(array)
# insertion_sort(array)

for item in array:
    print(item)
