stop = -1
while stop != 0:
    numbers = input().split()
    number1 = int(numbers[0])
    number2 = int(numbers[1]) 
    if number1 == number2 == 0:
        break
    sumNumber = number1 + number2
    numberEnd = str(sumNumber).replace('0', '')
    print(numberEnd)
