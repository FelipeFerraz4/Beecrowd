while True:
    try:
        valores = input().split()
        linhas = int(valores[0])
        colunas = int(valores[1])
        
        matriz = []
        for i in range(linhas):
            matrizLinha = input().split()
            linha = []
            for item in matrizLinha:
                linha.append(int(item))
            matriz.append(linha)
        novaMatriz = matriz.copy()
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] == 1:
                    print(9, end='')
                else:
                    queijosVizinhos = 0
                    if i-1 >= 0 and j >=0 and i-1 < linhas and j < colunas and matriz[i - 1][j] == 1:
                        queijosVizinhos += 1
                    if i+1 >= 0 and j >=0 and i+1 < linhas and j < colunas and matriz[i + 1][j] == 1:
                        queijosVizinhos += 1
                    if i >= 0 and j-1 >=0 and i < linhas and j-1 < colunas and matriz[i][j-1] == 1:
                        queijosVizinhos += 1
                    if i >= 0 and j+1 >=0 and i < linhas and j+1 < colunas and matriz[i][j+1] == 1:
                        queijosVizinhos += 1
                    print(queijosVizinhos, end='')
            print()     
    except EOFError:
        break