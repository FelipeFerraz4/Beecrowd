valores = input().split()

abas = int(valores[0])

for i in range(int(valores[1])):
    acao = input()
    
    if acao == 'fechou':
        abas += 1
    else:
        abas -= 1

print(abas)
