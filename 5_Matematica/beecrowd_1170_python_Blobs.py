import math

number_tests = int(input())
for _ in range(number_tests):
    number = float(input())
    days = math.ceil(math.log2(number))
    print(f'{days} dias')
