import math


while True:
    try:
      valores = input().split()
      
      xFiddlesticks = int(valores[0])
      yFiddlesticks = int(valores[1])
      xInvasor = int(valores[2])
      yInvasor = int(valores[3])
      velocidadeInvasor = int(valores[4])
      raioUltimate = int(valores[5])
      raioCorvos = int(valores[6])
      
      distancia = math.sqrt((xFiddlesticks - xInvasor)**2 + (yFiddlesticks - yInvasor)**2)
      
      distancia += 1.5 * velocidadeInvasor
      
      if distancia > (raioUltimate + raioCorvos):
          print('N')
      else:
          print('Y')
      
    except EOFError:
      break
