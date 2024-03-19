times = int(input())

pedidos = {'1001': 1.5, '1002': 2.5, '1003': 3.5, '1004': 4.5, '1005': 5.5}

soma = 0

for x in range(times):
    valores = input().split()
    soma += pedidos[valores[0]] * int(valores[1])

print(f'{soma:.2f}')
