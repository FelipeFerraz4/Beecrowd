valor = input()


if valor[0] != '-':
    print(f'+{float(valor):.4E}')
else:
    print(f'{float(valor):.4E}')
