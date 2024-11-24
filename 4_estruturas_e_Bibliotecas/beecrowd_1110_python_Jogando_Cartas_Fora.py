from sys import stdin
from collections import deque

while True:
    number = int(stdin.readline())
    
    if number == 0:
        break

    cards = deque(range(1, number + 1))
    discarded = []
    
    while len(cards) > 1:
        discarded.append(cards.popleft()) 
        cards.append(cards.popleft())     
    
    if discarded:
        print('Discarded cards: ', end='')
        print(', '.join(map(str, discarded)))
    else:
        print('Discarded cards: ')
    
    print(f'Remaining card: {cards[0]}')
