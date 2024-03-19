times = int(input())

for i in range(0, times):
    value = int(input())
    if value == 0:
        print('NULL')
    else:
        if value % 2 == 0:
            print(f'EVEN', end=' ')
        else:
            print(f'ODD', end=' ')

        if value > 0:
            print(f'POSITIVE')
        else:
            print(f'NEGATIVE')
