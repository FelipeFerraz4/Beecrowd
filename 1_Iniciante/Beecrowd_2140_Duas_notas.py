while True:
    valores = input().split()
    troco = int(valores[1]) - int(valores[0])
    
    if int(valores[1]) == int(valores[0]) == 0:
        break
    nota = 0
    notas = [100, 50, 20, 10, 5, 2]
    
    for x in range(len(notas)):
       nota += troco // notas[x]
       troco = troco % notas[x]

    if nota == 2:
        print('possible')
    else:
        print('impossible')
