porcoes = [300, 1500, 600, 1000, 150]

mandiocas = 225 

for i in range(5):
    valor = int(input())
    mandiocas += porcoes[i] * valor

print(mandiocas)
