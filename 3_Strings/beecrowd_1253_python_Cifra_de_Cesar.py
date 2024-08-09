quantidade_teste = int(input())
for i in range(quantidade_teste):
    cifra = input()
    passo = int(input())
    for j in range(len(cifra)):
        cifragem = ord(cifra[j]) - passo
        if cifragem < 65:
            cifragem = 91 - (65 - cifragem)
        print(chr(cifragem), end='')
    print()
