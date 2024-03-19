times = int(input())
for x in range(times):
    valores = input().split()
    resposta = 'abriu!'
    
    if valores[2] == '0':
        resposta = 'fechou!'
    
    print(f'{int(valores[0]):02}:{int(valores[1]):02} - A porta {resposta}')
