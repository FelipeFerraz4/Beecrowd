while True:
    try:
        valores = input().split()
        numeroPessoa = int(valores[0])
        alturaMinima = int(valores[1])
        alturaMaxima = int(valores[2])
        
        contador = 0
        
        for i in range(numeroPessoa):
            altura = int(input())
            if alturaMinima <= altura <= alturaMaxima:
                contador += 1
        
        print(contador)

    except EOFError:
        break