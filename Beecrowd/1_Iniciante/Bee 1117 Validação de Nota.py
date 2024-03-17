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
        state = 1