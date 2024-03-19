times = int(input())

for i in range(0, times):
    numbers = input().split()
    number1 = float(numbers[0])
    number2 = float(numbers[1])

    if number2 == 0:
        print('divisao impossivel')
    else:
        print(f'{number1/number2:.1f}')
