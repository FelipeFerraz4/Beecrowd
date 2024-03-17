import math

while True:
    valores = input().split()
    medidaCasaA = int(valores[0])
    
    if medidaCasaA == 0:
      break
    
    medidaCasaB = int(valores[1])
    maximoLiberado = int(valores[2])
    
    areaTotal = (medidaCasaA*medidaCasaB) * (100/maximoLiberado)
    ladoTerreno = math.trunc((areaTotal)**(1/2))
    
    print(ladoTerreno)
