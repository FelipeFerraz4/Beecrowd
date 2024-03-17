numbers = input().split()
number1 = int(numbers[0])
number2 = int(numbers[1])

for i in range(1, number2+1):
    if i % number1 == 0:
        print(f'{i}')
    else:
        print(f'{i}', end=' ')