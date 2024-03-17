times = int(input())
dados = []
for i in range(times):
    info = []
    nome = str(input())
    grau = float(input())
    valores = input().split()
    notas = []
    for i in valores:
        notas.append(float(i))
    menorNota =  min(notas)
    maiorNota =  max(notas)
    notas.remove(menorNota)
    notas.remove(maiorNota)
    pontos = sum(notas) * grau
    info = [nome, pontos]
    dados.append(info)

for i in range(times):
    print(f'{dados[i][0]} {dados[i][1]:.2f}')
