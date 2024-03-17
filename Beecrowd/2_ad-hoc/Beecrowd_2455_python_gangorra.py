valores = input().split()
peso1 = int(valores[0])
comprimento1 = int(valores[1])
peso2 = int(valores[2])
comprimento2 = int(valores[3])

diferenca = (peso1 * comprimento1) - (peso2 * comprimento2)

if diferenca > 0:
    print('-1')
elif diferenca < 0:
    print('1')
else:
    print('0')
