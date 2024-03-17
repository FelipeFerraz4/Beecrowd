while True:
    valores = input().split()
    multiplo = int(valores[0])
    exp = int(valores[1])
    
    if multiplo == exp == 0:
        break
    
    resultado = multiplo * exp
    
    print(resultado)
