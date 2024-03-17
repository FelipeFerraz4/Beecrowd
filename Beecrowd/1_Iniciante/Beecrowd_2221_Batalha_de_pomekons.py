def valorGolpe(ataque, defesa, level, bonus):
    golpe = (ataque + defesa) / 2
    if level % 2 == 0:
        golpe += bonus
    return golpe
    

times = int(input())
for i in range(times):
    bonus = int(input())
    Dabriel = input().split()
    Guarte = input().split()
    dabriel = valorGolpe(int(Dabriel[0]), int(Dabriel[1]), int(Dabriel[2]), bonus)
    guarte = valorGolpe(int(Guarte[0]), int(Guarte[1]), int(Guarte[2]), bonus) 

    if guarte > dabriel:
        print('Guarte')
    elif guarte < dabriel:
        print('Dabriel')
    else:
        print('Empate')
