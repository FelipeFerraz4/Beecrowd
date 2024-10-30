number_tests = int(input())
for item in range(number_tests):
    number_case = int(input())
    last_case = ((2)**(number_case) - 1)//12000
    print(f'{last_case} kg')