times = int(input())
valores = input().split()
if times == 2 and int(valores[0]) == int(valores[1]):
    resposta = 0
else:
    resposta = 1
    lista = []
    for x in range(times-1):
        if int(valores[x]) < int(valores[x+1]):
            lista.append(1)
        elif int(valores[x]) > int(valores[x+1]):
            lista.append(0)
        else:
            lista.append(3)

    for x in range(len(lista)-1):
        if lista[x] == lista[x+1] or lista[x] == 3 or lista[x+1] == 3:
            resposta = 0
print(resposta)
