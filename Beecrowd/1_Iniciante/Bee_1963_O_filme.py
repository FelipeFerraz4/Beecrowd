valores = input().split()
bilheteAntigo = float(valores[0])
bilheteAtual = float(valores[1])

aumento = ((bilheteAtual-bilheteAntigo)/bilheteAntigo) * 100

print(f'{aumento:.2f}%')
