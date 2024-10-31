import math

def isPrime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    prime = True
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

while True:
    try:
        number = int(input())
        prime = isPrime(number)
        if not(prime):
            print('Nada')
            continue
        
        super_prime = True
        for i in str(number):
            super_prime = isPrime(int(i))
            if not(super_prime):
                break
        
        if super_prime:
            print('Super')
        else:
            print('Primo')
        
    except EOFError:
        break