number_test = int(input())
for i in range(number_test):
    values = input()
    if values[0] == 'P':
        print('skipped')
    else:
        number_1, number_2 = values.split('+')
        print(int(number_1) + int(number_2))
