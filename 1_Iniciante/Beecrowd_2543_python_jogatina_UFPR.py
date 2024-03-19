while True:
    try:
        valores = input().split()
        gameplays = int(valores[0])
        id = int(valores[1])
        contador = 0
        for i in range(gameplays):
            info = input().split()
            if int(info[0]) == id and int(info[1]) == 0:
                contador += 1
        print(contador)
    except EOFError:
        break