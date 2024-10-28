import math

number_tests = int(input())
for _ in range(number_tests):
    number = int(input())
    
    if number < 2:
        print("Not Prime")
        continue
    if number == 2:
        print("Prime")
        continue
    if number % 2 == 0:
        print("Not Prime")
        continue
    
    prime = True
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            prime = False
            break
    if prime:
        print('Prime')
    else:
        print('Not Prime')