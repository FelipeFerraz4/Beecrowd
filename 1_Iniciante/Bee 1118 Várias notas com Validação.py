state = 0
count = 0
mean = 0

while state != 1:
    number = float(input())

    if 0 <= number <= 10:
        mean += number
        count += 1
    else:
        print('nota invalida')
    
    if count == 2:
        print(f'media = {mean/2:.2f}')
        new_calculo = 0
        while new_calculo != 1 and new_calculo != 2:
            print('novo calculo (1-sim 2-nao)')
            new_calculo = int(input())
        if new_calculo == 2:
            break
        else:
            count = 0
            mean = 0
