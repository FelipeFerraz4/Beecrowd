import math

number = int(input())
for _ in range(number):
    numbers = list(map(int, input().split()))
    print(int(numbers[1] * math.log10(numbers[0])) + 1)