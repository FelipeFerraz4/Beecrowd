number_test = int(input())
hobbits = 0
humans = 0
elves = 0
dwarves = 0
wizard = 0
for _ in range(number_test):
    text = input().split()
    
    if text[1] == 'A':
        dwarves += 1
    elif text[1] == 'E':
        elves += 1
    elif text[1] == 'H':
        humans += 1
    elif text[1] == 'M':
        wizard += 1
    elif text[1] == 'X':
        hobbits += 1
print(f'{hobbits} Hobbit(s)')
print(f'{humans} Humano(s)')
print(f'{elves} Elfo(s)')
print(f'{dwarves} Anao(oes)')
print(f'{wizard} Mago(s)')