while True:
    try:
        numeroTreino = int(input())
        dias = []
        velocidadeMedia = 0
        
        for i in range(numeroTreino):
            valores = input().split()
            tempo = int(valores[0])
            distancia = int(valores[1])
            velocidade = distancia/tempo
            
            if i == 0 or velocidade > velocidadeMedia:
                velocidadeMedia = velocidade
                dias.append(i+1)
        
        for i in range(len(dias)):
            print(dias[i])
        
    except EOFError:
        break