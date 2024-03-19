times = int(input())
valores = input().split()

multiplo = [0, 0, 0, 0]

for numero in valores:
    if int(numero) % 2 == 0:
        multiplo[0] += 1
    if int(numero) % 3 == 0:
        multiplo[1] += 1
    if int(numero) % 4 == 0:
        multiplo[2] += 1
    if int(numero) % 5 == 0:
        multiplo[3] += 1

print(f'{multiplo[0]} Multiplo(s) de 2')
print(f'{multiplo[1]} Multiplo(s) de 3')
print(f'{multiplo[2]} Multiplo(s) de 4')
print(f'{multiplo[3]} Multiplo(s) de 5')
