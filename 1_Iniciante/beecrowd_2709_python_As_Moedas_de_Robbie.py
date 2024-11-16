import math

def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

while True:
    try:
        number = int(input())
        numbers = []
        for i in range(number):
            numbers.append(int(input()))
        numbers = numbers[::-1]
        step = int(input())
        sum_number = 0
        for i in range(0, number, step):
            sum_number += numbers[i]
        if isPrime(sum_number):
            print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
        else:
            print('Bad boy! I’ll hit you.')
    except EOFError:
        break