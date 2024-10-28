number_tests = int(input())
for item in range(number_tests):
    number = float(input())
    days = 0
    while number > 1:
        number /= 2
        days += 1
    print(f'{days} dias')