def points(play, other_play1, other_play2):
    if (play == 'papel' and (other_play1 ==  other_play2 == 'pedra')):
        return 1
    elif (play == 'pedra' and (other_play1 == other_play2 == 'tesoura')):
        return 1
    elif (play == 'tesoura' and (other_play1 == other_play2 == 'papel')):
        return 1
    else:
        return 0

while True:
    try:
        values = input().split()
        dodo = points(str(values[0]), str(values[1]), str(values[2]))
        leo = points(str(values[1]), str(values[0]), str(values[2]))
        pepper = points(str(values[2]), str(values[1]), str(values[0]))
        
        if ((dodo + leo + pepper) != 1):
            print('Putz vei, o Leo ta demorando muito pra jogar...')
        elif (dodo == 1):
            print('Os atributos dos monstros vao ser inteligencia, sabedoria...')
        elif (leo == 1):
            print('Iron Maiden\'s gonna get you, no matter how far!')
        else:
            print('Urano perdeu algo muito precioso...')
    except EOFError:
        break