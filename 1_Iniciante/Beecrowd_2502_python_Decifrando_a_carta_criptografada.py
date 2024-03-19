while True:
    try:
        valores = input().split()
        times = int(valores[1])
        cifra1 = str(input())
        cifra2 = str(input())
        minuscula = []
        maiuscula = []
        for i in range(int(valores[0])):
            minuscula.append([cifra1[i].lower(), cifra2[i].lower()])
            minuscula.append([cifra2[i].lower(), cifra1[i].lower()])
            maiuscula.append([cifra1[i].upper(), cifra2[i].upper()])
            maiuscula.append([cifra2[i].upper(), cifra1[i].upper()])
        for x in range(times):
            newCifra = []
            cifra = str(input())
            for i in range(len(cifra)):
                letra = cifra[i]
                for j in range(len(minuscula)):
                    if letra == minuscula[j][0]:
                        letra = minuscula[j][1]
                        break
                    elif letra == maiuscula[j][0]:
                        letra = maiuscula[j][1]
                        break
                newCifra.append(letra)
            print(''.join(newCifra))
        print()
    except EOFError:
        break