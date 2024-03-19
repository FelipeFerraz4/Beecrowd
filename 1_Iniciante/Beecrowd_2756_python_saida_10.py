letra = ['A', 'B', 'C', 'D', 'E']
contador1 = 7
contador2 = 1

for i in range(5):
    print(' ' * contador1 + letra[i], end='')
    if letra[i] != 'A':
        print(' ' * contador2 + letra[i])
        contador2 += 2
    else:
        print()
    contador1 -= 1

contador1 += 2
contador2 -= 4
for i in range(4):
    print(' ' * contador1 + letra[4 - i - 1], end='')
    if letra[4 - i - 1] != 'A':
        print(' ' * contador2 + letra[4 - i - 1])
        contador2 -= 2
    else:
        print()
    contador1 += 1
