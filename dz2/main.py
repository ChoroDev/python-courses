import math

def task1():
    c = 2.1
    r = 4 * 10 ** -4
    m = 7
    i = ( 4.2, 0.3, 1.7 )
    print('"For" loop:')
    for j in i:
        h = (10 * r - j) / (c ** 2 + math.exp(-m))
        print('h = ', str(h))
        y = (h * m - j ** 2) + (0.1 * c) ** 2
        print('y = ', str(y))
    
    print('"While" loop:')
    j = 0
    while j < 1.8:
        h = (10 * r - j) / (c ** 2 + math.exp(-m))
        print('h = ', str(h))
        y = (h * m - j ** 2) + (0.1 * c) ** 2
        print('y = ', str(y))
        j += 0.1

    print('Double loop:')
    i = ( 9, 1.8, 15, -3 )
    for j in i:
        m = 1
        while m < 2.1:
            m += 0.5
            h = (10 * r - j) / (c ** 2 + math.exp(-m))
            print('h = ', str(h))
            y = (h * m - j ** 2) + (0.1 * c) ** 2
            print('y = ', str(y))


def task2():
    a = 2 * 10 ** -3
    b = 8.5
    n = 2
    j = ( 2, 1, 8.3 )
    print('"For" loop:')
    for i in j:
        y = math.sqrt(i * b - b ** 2 * a)
        print('y = ', str(y))
        z = y * math.tan(n / 4) - math.exp(1 + b)
        print('z = ', str(y))
    
    print('"While" loop:')
    i = 1
    while i < 3.1:
        y = math.sqrt(i * b - b ** 2 * a)
        print('y = ', str(y))
        z = y * math.tan(n / 4) - math.exp(1 + b)
        print('z = ', str(y))
        i += 0.5

    print('Double loop:')
    i = 3
    j = ( 3, -6, 0.2, 2.8 )
    b = 2
    while b < 3.1:
        for n in j:
            y = math.sqrt(i * b - b ** 2 * a)
            print('y = ', str(y))
            z = y * math.tan(n / 4) - math.exp(1 + b)
            print('z = ', str(y))
        b += 0.5


task2()