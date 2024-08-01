valores = input().split()
n = int(valores[0])
m = int(valores[1])
colar = str(input())
fim_antecipado = False
inicio = 0
fim = m
contasPretas = []

for i in range(n):
    bloco = colar[inicio:fim]
    contasPreta = bloco.count('1')
    print(f'{bloco} > {inicio} - {fim}')
    if contasPreta in contasPretas:
        fim_antecipado = True
        break
    contasPretas.append(contasPreta)
    inicio += m
    fim += m

if fim_antecipado:
    print('N')
else:
    print('S')
