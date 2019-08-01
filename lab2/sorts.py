import matplotlib.pyplot as plt
from datetime import datetime

def filledArray():
#     N = int(input('Enter count of elements: '))
    
#     lMin = int(input('Enter minimal element: '))
#     lMax = int(input('Enter maximal element: '))
#     mass = []
    x = []
    y1 = []
    y2 = []

    from random import random
    for N in range(1000, 5001, 1000):
        # mass.append(randint(lMin, lMax))
        x.append(N)
        min = 1
        max = N
        mass = []
        for i in range(N):
            mass.append(int(round(random() * (max - min) + min)))
        B = mass.copy()
        t1, t2 = bubbleSort(N, mass, mass.copy())
        t3, t4 = quickSort(N, B, B.copy())
        y1.append((t2 - t1).total_seconds())
        y2.append((t4 - t3).total_seconds())
        plt.plot(x, y1, 'C0')
        plt.plot(x, y2, 'C1')
        plt.show()

    #return (N, mass, mass.copy())


def bubbleSort(N, mass, B):
    #N, mass, B = filledArray()
    
    t1 = datetime.now()
    i = 0
    while i != N - 1:
        j = i + 1
        while j != N:
            if mass[i] > mass[j]:
                temp = mass[i]
                mass[i] = mass[j]
                mass[j] = temp
            j += 1
        i += 1

    #print('List before: {0}'.format(B))
    #print('List after: {0}'.format(mass))
    t2 = datetime.now()
    return (t1, t2)


def quickSortPart(mass, fst, lst):
    if fst >= lst:
        return

    pivot = mass[fst]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if mass[first_bigger] >= pivot:
            break
        first_bigger += 1

    i = first_bigger + 1

    while i <= lst:
        if mass[i] < pivot:
            mass[i], mass[first_bigger] = mass[first_bigger], mass[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1

    mass[fst], mass[last_smaller] = mass[last_smaller], mass[fst]

    quickSortPart(mass, fst, last_smaller - 1)
    quickSortPart(mass, first_bigger, lst)


def quickSort(N, mass, B):
    #N, mass, B = filledArray()
    t3 = datetime.now()
    quickSortPart(mass, 0, N - 1)
    #print('Array before: {0}'.format(B))
    #print('Array after: {0}'.format(mass))
    t4 = datetime.now()
    return (t3, t4)

#t1, t2, N = bubbleSort()

#t3, t4 = quickSort()

# print('Sort: bubble - start: {0}, end: {1}, run time: {2}'.format(t1, t2, t2 - t1))
# print('Sort: quick  - start: {0}, end: {1}, run time: {2}'.format(t3, t4, t4 - t3))


# from prettytable import PrettyTable

# table = PrettyTable(['List size', 'Bubble time', 'Quick time'])
# table.add_row([str(N), str(t2 - t1), str(t4 - t3)])

# print(table)

filledArray()