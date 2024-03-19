message = []
sizeLinha = 0

for item in range(4):
    linha = []
    valores = str(input())
    sizeLinha = len(valores)
    for i in range(sizeLinha):
        linha.append(valores[i])
    message.append(linha)

messageNumber = []
for i in range(sizeLinha):
    coluna = []
    for j in range(4):
        coluna.append(message[j][i])
    messageNumber.append(int(''.join(coluna)))

for i in range(1, sizeLinha-1):
    letra = (messageNumber[0] * messageNumber[i] + messageNumber[sizeLinha-1]) % 257
    letra = chr(letra)
    print(letra, end='')
print()
    