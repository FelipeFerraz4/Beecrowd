count = 1
i = 0
j = [100, 200, 300]
while i <= 200:
    if i % 100 == 0:
        print(f'I={i/100:.0f}', end=' ')
    else:
        print(f'I={i/100:.1f}', end=' ')
    
    if j[count-1] % 100 == 0:
        print(f'J={j[count-1]/100:.0f}')
    else:
        print(f'J={j[count-1]/100:.1f}')

    j[count-1] += 20
    if count == 3:
        i += 20
        count = 1
    else:
        count += 1
