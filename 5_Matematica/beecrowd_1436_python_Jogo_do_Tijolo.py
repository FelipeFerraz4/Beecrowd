number_tests = int(input())
for item in range(number_tests):
    numbers = list(map(int, input().split()))
    number_list = numbers[1:]
    print(f'Case {item+1}: {number_list[(len(number_list)//2)]}')