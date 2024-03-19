dias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
respostas = ['E natal!', 'E vespera de natal!', 'Ja passou!', 'Faltam X dias para o natal!']

while True:
    try:
        valores = input().split()
        mes = int(valores[0])
        dia = int(valores[1])
        resposta = 3
        duracao = 0
        
        if mes == 12:
            if dia == 25:
                resposta = 0
            elif dia == 24:
                resposta = 1
            elif dia > 25:
                resposta = 2
            else:
                duracao = 25 - dia
        else:
            duracao += dias[mes-1] - dia
            for i in range(mes, 11):
                duracao += dias[i]
            duracao += 25
        print(respostas[resposta].replace('X', str(duracao)))                
        
    except EOFError:
        break