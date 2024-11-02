quantidadeIntervalo = int(input())

distanciaTotal = 0

for i in range(quantidadeIntervalo):
    valores = input().split()
    tempo = int(valores[0])
    velocidade = int(valores[1])
    
    distancia = tempo * velocidade
    
    distanciaTotal += distancia
    
print(distanciaTotal)
