def firstTask():
    m = int(input('Enter first number: '))
    n = int(input('Enter second number: '))
    p = int(input('Enter third number: '))
    negativeCount = 0
    if n < 0:
        negativeCount += 1
    if m < 0:
        negativeCount += 1
    if p < 0:
        negativeCount += 1
    print('Count of negative numbers: {0}'.format(negativeCount))


def secondTask():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    c = float(input('Enter third number: '))

    if a == b:
        print('a = {0} and b = {1} are equal'.format(a, b))
    elif a == c:
        print('a = {0} and c = {1} are equal'.format(a, c))
    elif b == c:
        print('b = {0} and c = {1} are equal'.format(b, c))


def thirdTask():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    c = float(input('Enter third number: '))

    if a != 0 and b != 0 and c != 0:
        import math
        print('Geometric mean: {0}'.format(math.sqrt(a * b * c)))
    else:
        print('Arithmetical mean: {1}'.format((a + b + c) / 3))


def fourthTask():
    month = int(input('Enter number of month: '))
    
    import datetime
    monthString = datetime.date(2000, month, 1).strftime('%B')
    print('Month is: {0}'.format(monthString))


def fifthTask():
    A = float(input('Enter first number: '))
    B = float(input('Enter second number: '))
    C = float(input('Enter third number: '))
    D = float(input('Enter fourth number: '))

    if A % 2 == 1:
        print('A is odd')
    if B % 2 == 1:
        print('B is odd')
    if C % 2 == 1:
        print('C is odd')
    if D % 2 == 1:
        print('D is odd')


def sixthTask():
    n = int(input('Enter natural three-digit number: '))

    if 10 > n // 1000 > 0:
        nStr = str(n)
        has0or9 = False
        for c in nStr:
            if c == '0':
                print('There is 0 in this number')
                has0or9 = True
            elif c == '9':
                print('There is 9 in this number')
                has0or9 = True
        if not has0or9:
            print('There is no 0 or 9 in this number')
    else:
        print('Error: number must be three-digit')


def seventhTask():
    Y = int(input('Enter year: '))

    isLeap = False
    if Y < 0:
        print('Error: value must be positive')
    elif Y % 4 == 0:
        if Y % 100 != 0:
            print('Not finished yet')