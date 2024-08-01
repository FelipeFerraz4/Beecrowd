def eh_primo(numero):
    if numero == 1:
        return False
    for i in range (2, numero):
        if numero % i == 0:
            return False
    return True

testes = int(input())

for i in range(testes):
    numero = int(input())
    respostas = []
    desempate = []
    
    
    for x in range(numero):
        if eh_primo(x):
            continue
        for y in range(numero):
            if eh_primo(y) or x >= y:
                continue
            if x+y == numero:
                respostas.append([x,y])
                desempate.append(abs(x-y))
                
    if len(respostas) == 0:
        print(-1)
    elif len(respostas) == 1:
        print(f'{respostas[0][0]} {respostas[0][1]}')
    else:
        posicao = desempate.index(min(desempate))
        print(f'{respostas[posicao][0]} {respostas[posicao][1]}')
                