# Maratona de Programação da SBC – ICPC – 2020 
#Problema F -> Fastminton
jogadas = str(input())

sacando = 1
jogador1_pontos = 0
jogador2_pontos = 0
jogador1_games = 0
jogador2_games = 0
jogadorVencedor = 0

for jogada in jogadas:
    
    if jogada == 'S':
        if sacando == 1:
            jogador1_pontos += 1
        else:
            jogador2_pontos += 1
    elif jogada == 'R':
        if sacando == 1:
            jogador2_pontos += 1
            sacando = 2
        else:
            jogador1_pontos += 1
            sacando = 1
    else:
        if jogadorVencedor == 0:
            if sacando == 1:
                print(f'{jogador1_games} ({jogador1_pontos}*) - {jogador2_games} ({jogador2_pontos})')
            else:
                print(f'{jogador1_games} ({jogador1_pontos}) - {jogador2_games} ({jogador2_pontos}*)')
        elif jogadorVencedor == 1:
            print(f'{jogador1_games} (winner) - {jogador2_games}')
        else:
            print(f'{jogador1_games} - {jogador2_games} (winner)')
    

    if (jogador1_pontos > 4 and (jogador1_pontos - jogador2_pontos) > 1) or jogador1_pontos == 10:
        jogador1_games += 1
        jogador1_pontos = 0
        jogador2_pontos = 0
        sacando = 1
        
    if (jogador2_pontos > 4 and (jogador2_pontos - jogador1_pontos) > 1) or jogador2_pontos == 10:
        jogador2_games += 1
        jogador2_pontos = 0
        jogador1_pontos = 0
        sacando = 2
        
    if (jogador1_games - jogador2_games > 1):
        jogadorVencedor = 1
    
    if (jogador2_games - jogador1_games > 1):
        jogadorVencedor = 2
