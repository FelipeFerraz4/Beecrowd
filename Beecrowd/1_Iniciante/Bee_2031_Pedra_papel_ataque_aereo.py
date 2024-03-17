respostas = ['Jogador 1 venceu', 'Jogador 2 venceu', 'Ambos venceram', 'Sem ganhador', 'Aniquilacao mutua']

times = int(input())

for x in range(times):
    jogador1 = input()
    jogador2 = input()
    resposta = 4

    if jogador1 == jogador2:
        if jogador1 == 'papel':
            resposta = 2
        elif jogador1 == 'pedra':
            resposta = 3
        else:
            resposta = 4
    elif jogador1 == 'ataque':
        resposta = 0
    elif jogador2 == 'ataque':
        resposta = 1
    elif jogador1 == 'pedra':
        resposta = 0
    elif jogador2 == 'pedra':
        resposta = 1

    print(respostas[resposta])
