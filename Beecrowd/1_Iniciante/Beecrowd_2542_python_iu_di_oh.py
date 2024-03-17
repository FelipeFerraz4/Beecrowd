while True:
    try:
        numeroatributos = int(input())
        
        numeroCarta = input().split()
        numeroCartaMarcos = int(numeroCarta[0])
        numeroCartaLeonardo = int(numeroCarta[1])
        
        cartasMarcos = []
        
        for x in range(numeroCartaMarcos):
            carta = []
            atributos = input().split()
            for i in range(numeroatributos):
                carta.append(int(atributos[i]))
            cartasMarcos.append(carta)
        
        cartasLeonardo = []
        for x in range(numeroCartaLeonardo):
            carta = []
            atributos = input().split()
            for i in range(numeroatributos):
                carta.append(int(atributos[i]))
            cartasLeonardo.append(carta)
        
        cartas = input().split()
        cartaMarco = int(cartas[0]) - 1 
        cartaLeonardo = int(cartas[1]) - 1
        
        atributo = int(input()) - 1
        
        diferenca = cartasMarcos[cartaMarco][atributo] - cartasLeonardo[cartaLeonardo][atributo]
        
        if diferenca > 0:
            print("Marcos")
        elif diferenca < 0:
            print("Leonardo")
        else:
            print("Empate")
        
    except EOFError:
      break