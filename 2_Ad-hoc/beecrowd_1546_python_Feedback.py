number_tests = int(input())

for item in range(number_tests):
    tests = int(input())
    for item in range(tests):
        number = int(input())
        if number == 1:
            print('Rolien')
        elif number == 2:
            print('Naej')
        elif number == 3:
            print('Elehcim')
        else:
            print('Odranoel')
