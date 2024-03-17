tamanho = int(input())
matriz = []
matrizResposta = []
for i in range(tamanho + 1):
    valores = input().split()
    linha = []
    for x in valores:
        linha.append(int(x))
    matriz.append(linha)

for i in range(tamanho):
    for j in range(tamanho):
        soma = matriz[i][j] + matriz[i+1][j] + matriz[i][j+1] + matriz[i+1][j+1]
        
        if soma >= 2:
            print('S', end='')
        else:
            print('U', end='')
    print()
