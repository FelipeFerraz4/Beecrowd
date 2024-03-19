tamanho = int(input())
while tamanho != 0:
    tamanhoMaximoDoNumero = len(str(2**((tamanho*2) - 2)))
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            valor = 2**(i+j)

            if j != tamanho-1:
                print(f'{valor:{tamanhoMaximoDoNumero}} ', end='')
            else:
                print(f'{valor:{tamanhoMaximoDoNumero}}', end='')
        print()
    print()
    
    tamanho = int(input())
