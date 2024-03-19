while True:
    try:
        valores = input().split()
        linhas = int(valores[0])
        colunas = int(valores[1])
        matriz = []
        pessoa = []
        analogimon = []
        for x in range(linhas):
            number = input().split()
            linha = []
            for x in number:
                linha.append(int(x))
            matriz.append(linha)
            
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] == 1:
                    pessoa = [i, j]
                if matriz[i][j] == 2:
                    analogimon = [i, j]
        tempo = abs(pessoa[0] - analogimon[0]) + abs(pessoa[1] - analogimon[1])
            
        print(tempo)
    except EOFError:
      break
