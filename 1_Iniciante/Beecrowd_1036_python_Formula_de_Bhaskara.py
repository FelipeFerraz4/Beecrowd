value = input().split()
a, b, c = float(value[0]), float(value[1]), float(value[2])

delta = (b**2) - (4.0 * a * c)

if delta >= 0 and a != 0:
    delta = delta ** 0.5
    root1 = (-b + delta)/(2.0 * a)
    root2 = (-b - delta)/(2.0 * a)

    print(f'R1 = {root1:.5f}')
    print(f'R2 = {root2:.5f}')

else:
    print('Impossivel calcular')
