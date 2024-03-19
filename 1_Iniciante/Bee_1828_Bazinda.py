times = int(input())

for x in range(times):
    jogo = input().lower().split()
    sheldon = jogo[0]
    raj = jogo[1]
    
    option = ['pedra', 'papel', 'tesoura', 'lagarto', 'spock']
    reposta = 1
    
    
    if sheldon == 'pedra':
        if raj == 'lagarto' or raj == 'tesoura' :
            reposta = 1
        elif raj == 'pedra':
            reposta = 2
        else:
            reposta = 3
    elif sheldon == 'papel':
        if raj == 'pedra' or raj == 'spock' :
            reposta = 1
        elif raj == 'papel':
            reposta = 2
        else:
            reposta = 3
    elif sheldon == 'tesoura':
        if raj == 'lagarto' or raj == 'papel' :
            reposta = 1
        elif raj == 'tesoura':
            reposta = 2
        else:
            reposta = 3
    elif sheldon == 'lagarto':
        if raj == 'spock' or raj == 'papel' :
            reposta = 1
        elif raj == 'lagarto':
            reposta = 2
        else:
            reposta = 3
    else:
        if raj == 'tesoura' or raj == 'pedra' :
            reposta = 1
        elif raj == 'spock':
            reposta = 2
        else:
            reposta = 3


    if reposta == 1:
        print(f'Caso #{x+1}: Bazinga!')
    elif reposta == 2:
        print(f'Caso #{x+1}: De novo!')
    else:
        print(f'Caso #{x+1}: Raj trapaceou!')