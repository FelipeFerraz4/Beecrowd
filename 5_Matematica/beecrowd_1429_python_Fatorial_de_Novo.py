import math

run = True
while run:
    number = input()
    
    if number == '0':
        run = False
        break
    
    result = 0
    for i in range(len(number)):
        result += int(number[i]) * math.factorial(len(number) - i)
    print(result)    