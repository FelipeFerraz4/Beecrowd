def printMatriz(matriz, size):
    for i in range(0, size):
        for j in range(0, size):
            if j == size-1:
                print(f'{matriz[i][j]}')
            else:
                print(f'{matriz[i][j]}', end=' ')


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
            if j > i:
                soma += matriz[i][j]
    print(f'{soma:.1f}')
else:
    mean = 0
    for i in range(0, tamanhoMatriz):
        for j in range(0, tamanhoMatriz):
            if j > i:
                mean += matriz[i][j]
                count += 1
    mean /= count
    print(f'{mean:.1f}')

printMatriz(matriz, tamanhoMatriz)