tamanho = int(input())
while tamanho != 0:
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            menorDistanciaHorizontal = 1
            menorDistanciaVertical = 1
            menorDistancia = 1

            if i < (tamanho -i -1):
                menorDistanciaHorizontal = i
            else:
                menorDistanciaHorizontal = tamanho-i-1

            if j < (tamanho -j -1):
                menorDistanciaVertical = j
            else:
                menorDistanciaVertical = tamanho-j-1

            if menorDistanciaVertical < menorDistanciaHorizontal:
                menorDistancia = menorDistanciaVertical
            else:
                menorDistancia = menorDistanciaHorizontal

            if j != tamanho-1:
                print(f'{menorDistancia+1:3} ', end='')
            else:
                print(f'{menorDistancia+1:3}', end='')
        print()
    print()
    
    tamanho = int(input())
