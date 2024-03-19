times = int(input())
for i in range(0, times):
    sum = 0
    value = input().split()
    number1, number2 = int(value[0]), int(value[1])
    if number2 < number1:
        if number2 % 2 == 0:
            for i in range(number2, number1):
                if i % 2 == 1:
                    sum += i
        else:
            for i in range(number2+1, number1):
                if i % 2 == 1:
                    sum += i
    else:
        if number1 % 2 == 0:
            for i in range(number1, number2):
                if i % 2 == 1:
                    sum += i
        else:
            for i in range(number1+1, number2):
                if i % 2 == 1:
                    sum += i
    print(sum)
