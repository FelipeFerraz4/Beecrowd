tamanho = int(input())
while tamanho != 0:
    for i in range(0, tamanho):
        for j in range(0, tamanho):
            valor = abs(i - j) + 1

            if j != tamanho-1:
                print(f'{valor:3} ', end='')
            else:
                print(f'{valor:3}', end='')
        print()
    print()
    
    tamanho = int(input())
