number1 = 1
number2 = 1
while number1 > 0 and number2 > 0:
    numbers = input().split()
    number1 = int(numbers[0])
    number2 = int(numbers[1])
    if number1 <= 0 or number2 <= 0:
        break
    sum = 0
    if number2 < number1:
        for i in range(number2, number1+1):
            print(i, end=' ')
            sum += i
        print(f'Sum={sum}')
    else:
        for i in range(number1, number2+1):
            print(i, end=' ')
            sum += i
        print(f'Sum={sum}')