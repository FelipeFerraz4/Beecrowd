valores = input().split()

p = int(valores[0])
j1 = int(valores[1])
j2 = int(valores[2])
r = int(valores[3])
a = int(valores[4])

respostas = ['Jogador 1 ganha!', 'Jogador 2 ganha!']
resposta = 0

if r == a == 1:
    resposta = 1
    
if r == a == 0:
    if (j1 + j2) % 2 == 0:
        if p == 0:
            resposta = 1
    else:
        if p == 1:
            resposta = 1
            
print(respostas[resposta])
