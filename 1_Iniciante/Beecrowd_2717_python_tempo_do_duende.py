minute = int(input())
present = input().split()

if int(present[0]) + int(present[1]) > minute:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')
