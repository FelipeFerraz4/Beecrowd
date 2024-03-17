number1 = 1
number2 = 1
while number1 != 0 and number2 != 0:
    numbers = input().split()
    number1 = int(numbers[0])
    number2 = int(numbers[1])

    if number1 == 0 or number2 == 0:
        break

    if number1 > 0 and number2 > 0:
        print('primeiro')
    elif number1 < 0 and number2 < 0:
        print('terceiro')
    elif number1 > 0 and number2 < 0:
        print('quarto')
    else:
        print('segundo')
