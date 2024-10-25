run = True
while run:
    tests = int(input())
    
    if tests == 0:
        run = False
        break
    
    player = [0, 0]
    
    for item in range(tests):
        number_players = list(map(int, input().split()))
        if number_players[0] > number_players[1]:
            player[0] += 1
        elif number_players[0] < number_players[1]:
            player[1] += 1
    print(f'{player[0]} {player[1]}')