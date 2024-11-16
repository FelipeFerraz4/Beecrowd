date = list(map(int, input().split()))
if date[1] < date[0]:
    print('Eu odeio a professora!')
elif date[1] - date[0] >= 3:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    if date[0] + 2 < 24:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')