from sys import stdin
number_test = int(stdin.readline())
for _ in range(number_test):
    cards = stdin.readline()
    if 'Q' in cards and 'J' in cards and 'K' in cards and 'A' in cards:
        print('Aaah muleke')
    else:
        print('Ooo raca viu')