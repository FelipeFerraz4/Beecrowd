from sys import stdin
cards = list(map(int, stdin.readline().split()))
order = []
previus_card = cards[0]
for card in cards[1:]:
    if card > previus_card:
        order.append(1)
    elif card < previus_card:
        order.append(-1)
    previus_card = card
if sum(order) + 1 == len(cards):
    print('C')
elif sum(order) - 1== len(cards) * -1:
    print('D')
else:
    print('N')