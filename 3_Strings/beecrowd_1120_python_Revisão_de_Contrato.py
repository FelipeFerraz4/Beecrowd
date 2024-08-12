values = input().split()
while values[0] != '0' and values[1] != '0':
    number1 = values[0]
    number2 = values[1]
    
    number2 = number2.replace(number1, '')
    if number2 == '':
        print(0)
    else:
        print(int(number2))
    values = input().split()