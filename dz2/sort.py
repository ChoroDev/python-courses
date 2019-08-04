from random import random
from datetime import datetime
from datetime import timedelta
from prettytable import PrettyTable
from matplotlib import pyplot

x = []
y1 = []
y2 = []
y3 = []

def fillArray(N = 0, arrayMin = 0, arrayMax = 0):
    if N <= 0:
        N = int(input('Enter count of elements: '))
    
    if arrayMin <= 0:
        arrayMin = int(input('Enter minimal element: '))
    
    if arrayMax <= 0:
        arrayMax = int(input('Enter maximal element: '))

    array = []  
    for i in range(N):
        array.append(int(round(random() * (arrayMax - arrayMin) + arrayMin)))

    return array


def cocktailSort(array, N):
    for i in range(N // 2):
        for j in range(N - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] 
                
        for j in range(N - 1 - i, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

    return array


def insertSort(array, N):
    for i in range(1, N):
        temp = array[i]
        j = i
        while j > 0 and array[j - 1] > temp:
            array[j] = array[j - 1]
            j -= 1
        array[j] = temp
    
    return array


def shellSort(array, N):
    d = N // 2
    while d > 0:
        for i in range(d):
            for j in range(i + d, N, d):
                temp = array[j]
                pos = j
                while pos >= d and array[pos - d] > temp:
                    array[pos] = array[pos - d]
                    pos -= d
                array[pos] = temp
        d //= 2

    return array


def plotAndTime():
    table = PrettyTable(['Array size', 'Cocktail time', 'Insert time', 'Shell time'])
    for N in range(1000, 5001, 1000):
        arrayAtStart = fillArray(N, 1, 1000)
    
        arrayForCocktailSort = arrayAtStart.copy()
        arrayForInsertSort = arrayAtStart.copy()
        arrayForShellSort = arrayAtStart.copy()

        t1_1 = datetime.now()
        cocktailSort(arrayForCocktailSort, N)
        t1_2 = datetime.now()

        t2_1 = datetime.now()
        insertSort(arrayForInsertSort, N)
        t2_2 = datetime.now()
        
        t3_1 = datetime.now()
        shellSort(arrayForShellSort, N)
        t3_2 = datetime.now()
        
        table.add_row([N, str(t1_2 - t1_1), str(t2_2 - t2_1), str(t3_2 - t3_1)])

        x.append(N)
        y1.append((t1_2 - t1_1).total_seconds() * 1000)
        y2.append((t2_2 - t2_1).total_seconds() * 1000)
        y3.append((t3_2 - t3_1).total_seconds() * 1000)

    print(table)
    pyplot.plot(x, y1, 'C0')
    pyplot.plot(x, y2, 'C1')
    pyplot.plot(x, y3, 'C2')
    pyplot.show()


plotAndTime()