from sys import stdin

number_test = int(stdin.readline())
for _ in range(number_test):
    price = int(stdin.readline())
    prices = {}
    for i in range(price):
        frunt = stdin.readline().split()
        prices[frunt[0]] = float(frunt[1])
    shops = int(stdin.readline())
    shopping = 0
    for i in range(shops):
        frunt = stdin.readline().split()
        shopping += int(frunt[1]) * prices[frunt[0]]
    print(f'R$ {shopping:.2f}')