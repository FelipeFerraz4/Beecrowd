
valores = input().split()
distancia = int(valores[0])
velocidade = int(valores[1])
tempo = ((distancia / velocidade) + 19) % 24

hora = int(tempo)
minuto = int((tempo % 1) * 60)
print(f'{hora:02}:{minuto:02}')
