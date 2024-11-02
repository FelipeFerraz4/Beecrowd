number_tests = int(input())
numbers = {}

for _ in range(number_tests):
    number = int(input())
    if number in numbers:
        numbers[number] += 1
    else:
        numbers[number] = 1

numbers = dict(sorted(numbers.items()))

for key, value in numbers.items():
    print(f'{key} aparece {value} vez(es)')
