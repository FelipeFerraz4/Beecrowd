times = int(input())

for i in range(0, times):
    numbers = input().split()
    number1 = int(numbers[0])
    number2 = int(numbers[1])

    sum = 0

    if number1 % 2 == 0:
        number1 += 1

    for i in range(0, number2):
        sum += number1
        number1 += 2
    
    print(sum)
