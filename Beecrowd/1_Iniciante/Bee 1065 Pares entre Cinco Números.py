par = 0
impar = 0
positivo = 0
negativo = 0

for i in range(0, 5):
    value = float(input())
    if value % 2 == 0:
        par += 1
    
    if value % 2 == 1:
        impar += 1

    if value > 0:
        positivo += 1
    
    if value < 0:
        negativo += 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
