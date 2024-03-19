state = 0

while state != 1:
    number = int(input())

    for i in range(1, number+1):
        if i % number == 0:
            print(f'{i}')
        else:
            print(f'{i}', end=' ')
    
    if number == 0:
        state == 1
        break
