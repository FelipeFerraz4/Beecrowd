numbers_test = int(input())
for i in range(numbers_test):
    options = input().split()
    option1 = options[0]
    option2 = options[1]
    
    if option1 == option2:
        print('empate')
    elif (option1 == 'tesouro' and option2 == 'papel') or (option1 == 'papel' and option2 == 'pedra') or (option1 == 'pedra' and option2 == 'lagarto') or (option1 == 'lagarto' and option2 == 'spock') or (option1 == 'spock' and option2 == 'tesoura') or (option1 == 'tesoura' and option2 == 'lagarto') or (option1 == 'lagarto' and option2 == 'papel') or (option1 == 'papel' and option2 == 'spock') or (option1 == 'spock' and option2 == 'pedra') or (option1 == 'pedra' and option2 == 'tesoura'):
        print('rajesh')
    else:
        print('sheldon')        