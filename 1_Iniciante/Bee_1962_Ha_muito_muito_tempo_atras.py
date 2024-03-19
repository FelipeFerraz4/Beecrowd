times = int(input())

for x in range(times):
    anosPassados = int(input())
    
    if anosPassados > 2015:
        print(f'{anosPassados-2014} A.C.')
    elif anosPassados == 2015:
        print(f'1 A.C.')
    else: 
        print(f'{2015 - anosPassados} D.C.')