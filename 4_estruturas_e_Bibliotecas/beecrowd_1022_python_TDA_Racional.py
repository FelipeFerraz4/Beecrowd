import math
from sys import stdin

def simplify_fraction(numarator, denominator):
    divisor = math.gcd(numarator, denominator)
    return numarator // divisor, denominator // divisor

number_test = int(stdin.readline())
for i in range(number_test):
    expression = stdin.readline().split()
    if expression[3] == '+':
        numerator = int(expression[0])*int(expression[6]) + int(expression[4])*int(expression[2])
        denominator = int(expression[2])*int(expression[6])
    elif expression[3] == '-':
        numerator = int(expression[0])*int(expression[6]) - int(expression[4])*int(expression[2])
        denominator = int(expression[2])*int(expression[6])
    elif expression[3] == '*':
        numerator = int(expression[0])*int(expression[4])
        denominator = int(expression[2])*int(expression[6])
    else:
        numerator = int(expression[0])*int(expression[6])
        denominator = int(expression[4])*int(expression[2])
    new_numerator, new_denominator = simplify_fraction(numerator, denominator)
    print(f'{numerator}/{denominator} = {new_numerator}/{new_denominator}')
    