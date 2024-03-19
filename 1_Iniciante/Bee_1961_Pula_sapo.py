respostas = ['YOU WIN', 'GAME OVER']

dadoJogo = input().split()
puloDoSapo = int(dadoJogo[0])
times = int(dadoJogo[1])

dadosCanos = input().split()
canoAtual = int(dadosCanos[0])

resposta = 0

for x in dadosCanos:
  if abs(canoAtual-(int(x))) > puloDoSapo:
      resposta = 1
  canoAtual = int(x)

print(respostas[resposta])
