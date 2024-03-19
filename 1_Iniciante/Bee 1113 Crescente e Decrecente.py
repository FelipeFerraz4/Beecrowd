number1 = 1
number2 = 0
while number1 != number2:
    numbers = input().split()
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    if number1 == number2:
        break
    if number2 < number1:
        print(f'Decrescente')
    else:
        print(f'Crescente')
