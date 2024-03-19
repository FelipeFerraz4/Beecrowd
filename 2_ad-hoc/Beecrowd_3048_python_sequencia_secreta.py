tamanhoSequencia = int(input())

sequencia = []

for i in range(tamanhoSequencia):
    valor = int(input())
    sequencia.append(valor)

valorAtual = 1
contador = 1
for item in sequencia:
    if item != valorAtual:
        contador += 1
        valorAtual = item
        
print(contador) 