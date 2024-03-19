def printMatriz(matriz, size):
    for i in range(0, size):
        for j in range(0, size):
            if j == size-1:
                print(f'{matriz[i][j]}')
            else:
                print(f'{matriz[i][j]}', end=' ')


linha = int(input())
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
        soma += matriz[linha][i]
    print(f'{soma:.1f}')
else:
    mean = 0
    for i in range(0, tamanhoMatriz):
        mean += matriz[linha][i]
    mean /= tamanhoMatriz
    print(f'{mean:.1f}')

printMatriz(matriz, tamanhoMatriz)