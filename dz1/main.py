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

    if 10 > n // 100 > 0:
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
        if Y % 100 == 0:
            if Y % 400 == 0:
                isLeap = True
        else:
            isLeap = True

    if isLeap:
        print('Year is leap')
    else:
        print('Year is not leap')


def eighthTask():
    n = int(input('Enter natural three-digit number: '))

    if 10 > n // 100 > 0:
        nStr = str(n)
        isNotEqual = False

        if nStr[0] != nStr[1] and nStr[0] != nStr[2]:
            if nStr[1] != nStr[2]:
                isNotEqual = True
        
        if isNotEqual:
            print('Digits are not equal')
        else:
            print('There are some equal digits')
    else:
        print('Error: number must be three-digit')


def ninthTask():
    A = float(input('Enter numerator: '))
    B = float(input('Enter denominator: '))
    
    if -1 >= A / B >= 1:
        print('Improper fraction')
    else:
        print('Proper fraction')


def tenthTask():
    n = int(input('Enter natural three-digit number: '))

    if 10 > n // 100 > 0:
        nStr = str(n)

        sum = 0
        for c in nStr:
            sum += int(c)

        if sum % 3 == 0 and n % 3 == 0:
            print('It\'s true')
        else:
            print('Scientists lie')
    else:
        print('Error: number must be three-digit')


def eleventhTask():
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    c = float(input('Enter third number: '))

    d = max(a, b, c)
    print('Max = {0}'.format(d))


def twelwethTask():
    n = int(input('Enter natural two-digit number: '))
    if 10 > n // 10 > 0:
        nStr = str(n)
        has1or9 = False
        for c in nStr:
            if c == '1':
                print('There is 1 in this number')
                has1or9 = True
            elif c == '9':
                print('There is 9 in this number')
                has1or9 = True
        if not has1or9:
            print('There is no 1 or 9 in this number')
    else:
        print('Error: number must be two-digit')


def thirteenthTask():
    n = int(input('Enter count of mushrooms: '))

    if n == 1:
        print('We\'ve found {0} mushroom'.format(n))
    else:
        print('We\'ve found {0} mushrooms'.format(n))


def fourteenthTask():
    n = int(input('Enter number in range from 1 to 9: '))

    if 10 > n // 1 > 0:
        if n == 1:
            print('I\'m {0} year old'.format(n))
        else:
            print('I\'m {0} years old'.format(n))
    else:
        print('Error: wrong number')

