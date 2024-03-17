valores = input().split()
quantidadeCompetidores = int(valores[0])
quantidadeFolhas = int(valores[1])
quantidadeJuizes = int(valores[2])

if quantidadeFolhas >= quantidadeCompetidores * quantidadeJuizes:
    print('S')
else:
    print('N')
