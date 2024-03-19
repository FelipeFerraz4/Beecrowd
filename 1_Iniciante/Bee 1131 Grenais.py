grenais = 0
inter = 0
gremio = 0
empate = 0
state = 0

while state != 1:
    value = input().split()
    number1 = int(value[0])
    number2 = int(value[1])

    grenais += 1
    if number1 > number2:
        inter += 1
    elif number2 > number1:
        gremio += 1
    else:
        empate += 1

    new_state = 0
    while new_state != 1 and new_state != 2:
        print('Novo grenal (1-sim 2-nao)')
        new_state = int(input())

    if new_state == 2:
        break

print(f'{grenais} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')

if inter > gremio:
    print('Inter venceu mais')
elif gremio > inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
