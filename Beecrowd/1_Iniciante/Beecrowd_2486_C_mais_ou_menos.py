alimentos = {'suco de laranja':120, 'morango fresco':85, 'mamao':85, 'goiaba vermelha':70, 'manga':56, 'laranja':50, 'brocolis':34}

while True:
    vitaminaC = 0
    quantidade = int(input())
    if quantidade == 0:
        break
    
    for i in range(quantidade):
        alimento = input().split()
        fruta = ' '.join(alimento[1:])
        vitaminaC += int(alimento[0]) * alimentos[fruta]
    
    if vitaminaC > 130:
        print(f'Menos {vitaminaC - 130} mg')
    elif vitaminaC < 110:
        print(f'Mais {110 - vitaminaC} mg')
    else:
        print(f'{vitaminaC} mg')
