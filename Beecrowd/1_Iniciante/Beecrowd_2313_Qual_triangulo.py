valores = input().split()
lado1 = int(valores[0])
lado2 = int(valores[1])
lado3 = int(valores[2])

if (abs(lado2 - lado3) < lado1 < lado2 + lado3) and (abs(lado1 - lado3) < lado2 < lado1 + lado3) and (abs(lado1 - lado2) < lado3 < lado1 + lado2):
    if lado1 == lado2 == lado3:
        print('Valido-Equilatero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Valido-Isoceles')
    else:
        print('Valido-Escaleno')
    
    if (lado1 % 3 == 0 and lado2 % 4 == 0 and lado3 % 5 == 0) or (lado1 % 3 == 0 and lado3 % 4 == 0 and lado2 % 5 == 0) or (lado2 % 3 == 0 and lado1 % 4 == 0 and lado3 % 5 == 0) or (lado2 % 3 == 0 and lado3 % 4 == 0 and lado1 % 5 == 0) or (lado3 % 3 == 0 and lado2 % 4 == 0 and lado1 % 5 == 0) or (lado3 % 3 == 0 and lado1 % 4 == 0 and lado2 % 5 == 0):
        print('Retangulo: S')
    else:
        print('Retangulo: N')
else:
    print('Invalido')
