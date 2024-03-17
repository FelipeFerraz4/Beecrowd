times = int(input())

valores = input().split()
anterior = int(valores[0])
resultado = 0
count = 0
for x in valores:
    if anterior > int(x):
        resultado = count + 1
        break
    
    anterior = int(x)
    count += 1

print(resultado)
        