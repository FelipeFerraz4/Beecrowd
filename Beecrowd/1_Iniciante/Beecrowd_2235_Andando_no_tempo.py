valores = input().split()

credito1 = int(valores[0])
credito2 = int(valores[1])
credito3 = int(valores[2])

resposta = 'N'

if credito1 == credito2 or credito1 == credito3 or credito3 == credito2:
    resposta = 'S'
elif credito1+credito2 == credito3 or credito1+credito3 == credito2 or credito3+credito2 == credito1:
    resposta = 'S'

print(resposta)
