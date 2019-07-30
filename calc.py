def calc():
    x = float(input('Enter first number: '))
    y = float(input('Enter second number: '))

    operator = input('Enter operation: ').strip()

    result = 0.0

    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y
    elif operator == '/':
        try:
            if y == 0:
                raise Exception('Division by zero is restricted')
            result = x / y
        except Exception as e:
            print(e)
    elif operator == '*':
        result = x * y
    else:
        try:
            raise Exception('Wrong operation')
        except Exception as e:
            print(e)

    print('Operation result (' + str(x) + ' ' + operator + ' ' + str(y) + '): ' + str(result))

