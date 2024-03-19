times = int(input())
for x in range(times):
    texto = input()
    frase = []

    for i in range(len(texto)):
        simbolo = texto[i]
        if(simbolo.isalpha()):
            simbolo = chr(ord(texto[i]) + 3)
        frase.append(simbolo)
    texto = ''.join(frase)

    texto = texto[::-1]
    frase = []

    for i in range(len(texto)):
        simbolo = texto[i]
        if(i >= len(texto)//2):
            simbolo = chr(ord(texto[i]) - 1)
        frase.append(simbolo)
    texto = ''.join(frase)

    print(texto)