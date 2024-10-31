import math

def isPitagorica(number1, number2, number3):
    test1 = number1**2 == number2**2 + number3**2
    test2 = number2**2 == number1**2 + number3**2
    test3 = number3**2 == number2**2 + number1**2
    return test1 or test2 or test3

while True:
    try:
        numbers = list(map(int, input().split()))
        if isPitagorica(numbers[0], numbers[1], numbers[2]):
            if math.gcd(numbers[0], numbers[1], numbers[2]) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
        
    except EOFError:
        break