import math

while True:
    try:
        number = input()
        values = list(map(float, input().split()))
        average = sum(values) / len(values)
        standard_deviation = sum((value - average)**2 for value in values)
        standard_deviation = math.sqrt(standard_deviation / (len(values) - 1))
        print(f'{standard_deviation:.5f}')
    except EOFError:
        break