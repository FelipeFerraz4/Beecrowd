valores = input().split()

hora = int(valores[0]) + int(valores[1]) + int(valores[2])

if hora >= 24:
    hora -= 24
    
if hora < 0:
    hora += 24

print(hora)
