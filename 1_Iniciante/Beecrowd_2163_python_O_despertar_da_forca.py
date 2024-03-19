tamanho = input().split()
linhas = int(tamanho[0])
colunas = int(tamanho[1])
matrix = []
for x in range(linhas):
    valores = input().split()
    linha = []
    for x in valores:
        linha.append(int(x))
    matrix.append(linha)
pontos = [0, 0]
for i in range(linhas):
    for j in range(colunas):
        if i != 0 and j!= 0 and i != linhas-1 and j != colunas-1:
            if matrix[i][j] == 42 and matrix[i+1][j+1] == 7 and matrix[i][j+1] == 7 and matrix[i+1][j] == 7 and matrix[i+1][j-1] == 7 and matrix[i-1][j+1] == 7 and matrix[i-1][j-1] == 7 and matrix[i-1][j] == 7 and matrix[i][j-1] == 7:
                pontos[0] = i + 1
                pontos[1] = j + 1

print(f'{pontos[0]} {pontos[1]}')
