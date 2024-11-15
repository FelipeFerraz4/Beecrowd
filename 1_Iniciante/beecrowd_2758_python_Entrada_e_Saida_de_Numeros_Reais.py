# questão com erro de aproximação do python

from decimal import Decimal
from math import ceil
def insert_zero(number):
    index = number.find('.')
    return number + ('0' * (6 - len(number[index+1:])))
    
numbers1 = input().split()
numbers2 = input().split()

print(f'A = {insert_zero(numbers1[0])}, B = {insert_zero(numbers1[1])}')
print(f'C = {insert_zero(numbers2[0])}, D = {insert_zero(numbers2[1])}')

print(f'A = {Decimal(numbers1[0]):.1f}, B = {Decimal(numbers1[1]):.1f}')
print(f'C = {Decimal(numbers2[0]):.1f}, D = {Decimal(numbers2[1]):.1f}')

print(f'A = {Decimal(numbers1[0]):.2f}, B = {Decimal(numbers1[1]):.2f}')
print(f'C = {Decimal(numbers2[0]):.2f}, D = {Decimal(numbers2[1]):.2f}')

print(f'A = {Decimal(numbers1[0]):.3f}, B = {Decimal(numbers1[1]):.3f}')
print(f'C = {Decimal(numbers2[0]):.3f}, D = {Decimal(numbers2[1]):.3f}')

print(f'A = {Decimal(numbers1[0]):.3E}, B = {Decimal(numbers1[1]):.3E}')
print(f'C = {Decimal(numbers2[0]):.3E}, D = {Decimal(numbers2[1]):.3E}')

print(f'A = {int(ceil(Decimal(numbers1[0])))}, B = {int(ceil(Decimal(numbers1[1])))}')
print(f'C = {int(ceil(Decimal(numbers2[0])))}, D = {int(ceil(Decimal(numbers2[1])))}')