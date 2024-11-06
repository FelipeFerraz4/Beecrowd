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

number = int(input())
prime = []
result = []

for i in range(2, number + 1):
    if isPrime(i):
        if prime and prime[-1] == i - 2:
            result = [prime[-1], i]
        prime.append(i)

print(f'{result[0]} {result[1]}')
