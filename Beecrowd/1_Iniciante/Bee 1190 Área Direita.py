count = 0
operation = input()
tamanhoMatriz = 12
matriz = []

for i in range(0, tamanhoMatriz):
    matriz.append([])

for i in range(0, tamanhoMatriz):
    for j in range(0, tamanhoMatriz):
        matriz[i].append(float(input()))

if operation == 'S':
    soma = 0
    for i in range(0, tamanhoMatriz):
        for j in range(0, tamanhoMatriz):
            if j + i > tamanhoMatriz-1 and j > i:
                soma += matriz[i][j]
    print(f'{soma:.1f}')
else:
    mean = 0
    for i in range(0, tamanhoMatriz):
        for j in range(0, tamanhoMatriz):
            if j + i > tamanhoMatriz-1 and j > i:
                mean += matriz[i][j]
                count += 1
    mean /= count
    print(f'{mean:.1f}')
