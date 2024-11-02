
def equation(number):
    import math
    return (-1 + math.sqrt(1 + (8*number)))//2

number_tests = int(input())
for _ in range(number_tests):
    number = int(input())
    result = equation(number)
    print(int(result))