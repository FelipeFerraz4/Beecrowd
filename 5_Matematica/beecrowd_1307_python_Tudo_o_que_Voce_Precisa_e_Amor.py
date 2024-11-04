import math

number_tests = int(input())
for item in range(number_tests):
    number1 = int(input(), base=2)
    number2 = int(input(), base=2)
    
    gcd_value = math.gcd(number1, number2)
    
    if gcd_value > 1:
        print(f'Pair #{item + 1}: All you need is love!')
    else:
        print(f'Pair #{item + 1}: Love is not all you need!')
    