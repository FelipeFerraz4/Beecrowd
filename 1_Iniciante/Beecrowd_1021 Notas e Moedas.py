value = float(input())
value *= 100

money = [10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5, 1]
phase = ['nota', 'moeda']
counter = 0
print(f'NOTAS:')

for i in money:
    quantity_notas = value // i
    value = value - (quantity_notas * i)
    print(f'{quantity_notas:.0f} {phase[counter]}(s) de R$ {i/100:.2f}')
    if i == 200:
        print(f'MOEDAS:')
        counter += 1
