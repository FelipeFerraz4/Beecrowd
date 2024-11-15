number = int(input())
squares = number * number
if squares % 2 == 0: 
    print(f'{squares//2} casas brancas e {squares//2} casas pretas')
else:
    print(f'{squares//2 + 1} casas brancas e {squares//2} casas pretas')