# Não consegue passar no Beecrowd

def subString(palavra_teste):
    soma = 0
    for i in range(1, len(palavra_teste)+1):
        conjunto = set()
        for j in range(len(palavra_teste)):
            if len(palavra_teste) >= j+i:
                letra = palavra_teste[j:j+i]
                conjunto.add(letra)
        soma += len(conjunto)   
    return soma
while True:
    try:
        palavras = input().split('?')
        palavras.pop()
        palavra_anterior = ''
        for palavra in palavras:
          palavra_anterior = palavra + palavra_anterior
          print(subString(palavra_anterior))
    except EOFError:
        break
