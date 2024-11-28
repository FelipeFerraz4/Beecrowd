from sys import stdin
from bisect import bisect_left
count = 1
while True:
    number_marble = list(map(int, stdin.readline().split()))
    if sum(number_marble) == 0:
        break
    
    marbles = []
    for i in range(number_marble[0]):
        marbles.append(int(stdin.readline()))
    marbles.sort()
    print(f'CASE# {count}:')
    for i in range(number_marble[1]):
        search = int(stdin.readline())
        position = bisect_left(marbles, search)
        if position < len(marbles) and marbles[position] == search:
            print(f'{search} found at {position+1}')
        else:
            print(f'{search} not found')
    count += 1