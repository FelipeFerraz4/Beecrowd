number_limit = int(input())
operation = input().split()

if operation[1] == '+':
    if number_limit - int(operation[0]) - int(operation[2]) < 0:
        print('OVERFLOW')
    else:
        print('OK')
else:
    if number_limit / int(operation[0]) < int(operation[2]):
        print('OVERFLOW')
    else:
        print('OK')
