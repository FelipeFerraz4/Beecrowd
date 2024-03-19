state = 0
alcool = 0
gasolina = 0
diesel = 0

while state != 1:
    value = int(input())

    if value == 1:
        alcool += 1
    elif value == 2:
        gasolina += 1
    elif value == 3:
        diesel += 1
    elif value == 4:
        state = 1
        break

print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')