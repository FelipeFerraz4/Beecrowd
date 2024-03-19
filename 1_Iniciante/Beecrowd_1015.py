ponto1 = input().split()
ponto2 = input().split()

X1, Y1 = float(ponto1[0]), float(ponto1[1])
X2, Y2 = float(ponto2[0]), float(ponto2[1])

distancia = (((X1-X2)**2) + ((Y1-Y2)**2))**0.5

print(f'{distancia:.4f}')
